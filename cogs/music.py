#Extraído de https://github.com/Daishiky/music-discord/blob/main/cogs/music.py
import asyncio
import functools
import itertools
import math
import random
import urllib
import discord
from humanize.time import precisedelta
import youtube_dl
from async_timeout import timeout
from discord.ext import commands
import re
import humanize
import datetime

youtube_dl.utils.bug_reports_message = lambda: ''


class VoiceError(Exception):
    pass


class YTDLError(Exception):
    pass


class YTDLSource(discord.PCMVolumeTransformer):
    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
    }

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }

    ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)

    def __init__(self, ctx: commands.Context, source: discord.FFmpegPCMAudio, *, data: dict, volume: float = 0.5):
        super().__init__(source, volume)

        self.requester = ctx.author
        self.channel = ctx.channel
        self.data = data

        self.uploader = data.get('uploader')
        self.uploader_url = data.get('uploader_url')
        date = data.get('upload_date')
        self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
        self.title = data.get('title')
        self.thumbnail = data.get('thumbnail')
        self.description = data.get('description')
        self.duration = self.parse_duration(int(data.get('duration')))
        self.tags = data.get('tags')
        self.url = data.get('webpage_url')
        self.views = data.get('view_count')
        self.likes = data.get('like_count')
        self.dislikes = data.get('dislike_count')
        self.stream_url = data.get('url')

    def __str__(self):
        return '**`{0.title}`** by **`{0.uploader}`**'.format(self)

    @classmethod
    async def create_source(cls, ctx: commands.Context, search: str, *, loop: asyncio.BaseEventLoop = None):
        loop = loop or asyncio.get_event_loop()

        partial = functools.partial(cls.ytdl.extract_info, search, download=False, process=False)
        data = await loop.run_in_executor(None, partial)

        if data is None:
            raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        if 'entries' not in data:
            process_info = data
        else:
            process_info = None
            for entry in data['entries']:
                if entry:
                    process_info = entry
                    break

            if process_info is None:
                raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        webpage_url = process_info['webpage_url']
        partial = functools.partial(cls.ytdl.extract_info, webpage_url, download=False)
        processed_info = await loop.run_in_executor(None, partial)

        if processed_info is None:
            raise YTDLError('Couldn\'t fetch `{}`'.format(webpage_url))

        if 'entries' not in processed_info:
            info = processed_info
        else:
            info = None
            while info is None:
                try:
                    info = processed_info['entries'].pop(0)
                except IndexError:
                    raise YTDLError('Couldn\'t retrieve any matches for `{}`'.format(webpage_url))

        return cls(ctx, discord.FFmpegPCMAudio(info['url'], **cls.FFMPEG_OPTIONS), data=info)

    @staticmethod
    def parse_duration(duration: int):
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        duration = []
        if days > 0:
            duration.append('{} days'.format(days))
        if hours > 0:
            duration.append('{} hours'.format(hours))
        if minutes > 0:
            duration.append('{} minutes'.format(minutes))
        if seconds > 0:
            duration.append('{} seconds'.format(seconds))
        else:
            duration.append('LIVE STREAMING')

        return ', '.join(duration)


class Song:
    __slots__ = ('source', 'requester')

    def __init__(self, source: YTDLSource):
        self.source = source
        self.requester = source.requester

    def create_embed(self):
        em = (discord.Embed(description='```css\n{0.source.title}\n```'.format(self), color=discord.Color.blurple())
                 .add_field(name='⏱️ Duración', value=f"`{self.source.duration}`", inline = True)
                 .add_field(name='👤 Solicitado por', value=self.requester.mention, inline = True)
                 .add_field(name='🎵 Artista', value='[{0.source.uploader}]({0.source.uploader_url})'.format(self))
                 .add_field(name="👀 Total Views", value ="`{}`".format(humanize.intword(self.source.views)))
                 .add_field(name="👍 Total Likes", value ="`{}`".format(humanize.intword(self.source.likes)))
                 .add_field(name="👎 Total Dislikes", value ="`{}`".format(humanize.intword(self.source.dislikes)))
                 .set_thumbnail(url=self.source.thumbnail)
                 .set_footer(text=f"Solicitado por {self.requester.name} (In streaming)", icon_url=f"{self.requester.avatar_url}"))

        return em


class SongQueue(asyncio.Queue):
    def __getitem__(self, item):
        if isinstance(item, slice):
            return list(itertools.islice(self._queue, item.start, item.stop, item.step))
        else:
            return self._queue[item]

    def __iter__(self):
        return self._queue.__iter__()

    def __len__(self):
        return self.qsize()

    def clear(self):
        self._queue.clear()

    def shuffle(self):
        random.shuffle(self._queue)

    def remove(self, index: int):
        del self._queue[index]


class VoiceState:
    def __init__(self, bot: commands.Bot, ctx: commands.Context):
        self.bot = bot
        self._ctx = ctx

        self.current = None
        self.voice = None
        self.next = asyncio.Event()
        self.songs = SongQueue()

        self._loop = False
        self._volume = 0.5
        self.skip_votes = set()

        self.audio_player = bot.loop.create_task(self.audio_player_task())

    def __del__(self):
        self.audio_player.cancel()

    @property
    def loop(self):
        return self._loop

    @loop.setter
    def loop(self, value: bool):
        self._loop = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value: float):
        self._volume = value

    @property
    def is_playing(self):
        return self.voice and self.current

    async def audio_player_task(self):
        while True:
            self.next.clear()

            if not self.loop:
                try:
                    async with timeout(180):  # 3 minutes
                        self.current = await self.songs.get()
                except asyncio.TimeoutError:
                    self.bot.loop.create_task(self.stop())
                    return

            self.current.source.volume = self._volume
            self.voice.play(self.current.source, after=self.play_next_song)
            await self.current.source.channel.send(embed=self.current.create_embed())

            await self.next.wait()

    def play_next_song(self, error=None):
        if error:
            raise VoiceError(str(error))

        self.next.set()

    def skip(self):
        self.skip_votes.clear()

        if self.is_playing:
            self.voice.stop()

    async def stop(self):
        self.songs.clear()

        if self.voice:
            await self.voice.disconnect()
            self.voice = None


class music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.voice_states = {}


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Music Loaded")


    def get_voice_state(self, ctx: commands.Context):
        state = self.voice_states.get(ctx.guild.id)
        if not state:
            state = VoiceState(self.bot, ctx)
            self.voice_states[ctx.guild.id] = state

        return state

    def cog_unload(self):
        for state in self.voice_states.values():
            self.bot.loop.create_task(state.stop())

    def cog_check(self, ctx: commands.Context):
        if not ctx.guild:
            raise commands.NoPrivateMessage('This command can\'t be used in DM channels.')

        return True

    async def cog_before_invoke(self, ctx: commands.Context):
        ctx.voice_state = self.get_voice_state(ctx)

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('An error occurred: {}'.format(str(error)))

    @commands.command(help="Hazme unir a un canal de voz.", name="join", aliases = ["j"], invoke_without_subcommand=True)
    async def _join(self, ctx: commands.Context):

        destination = ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)          

        ctx.voice_state.voice = await destination.connect()

        em = discord.Embed(title=f"✅ Me he conectado en {destination}", color = ctx.author.color)
        em.set_footer(text=f"Solicitado por {ctx.author.name}")  
        await ctx.send(embed=em)

    @commands.command(help="Invócame en un canal de voz", name="summon", aliases = ["s"])
    async def _summon(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None):

        if not channel and not ctx.author.voice:
            raise VoiceError('No estás conectado a ningún canal de voz / no especificaste a que canal unirme.')

        destination = channel or ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            em = discord.Embed(title=f"✅ He sido invocada en {destination}", color = ctx.author.color)
            em.set_footer(text=f"Solicitado por {ctx.author.name}")
            await ctx.send(embed=em)

        ctx.voice_state.voice = await destination.connect()

    @commands.command(help="Hazme salir de un canal de voz.", name="leave", aliases = ["l"])
    async def _leave(self, ctx: commands.Context):

        if not ctx.voice_state.voice:
            return await ctx.send('No estoy conectada a ningún canal de voz.')

        if ctx.author.voice.channel != ctx.guild.me.voice.channel:
            return await ctx.send("No estás conectado a ningún canal.")

        dest = ctx.author.voice.channel
        await ctx.voice_state.stop()
        del self.voice_states[ctx.guild.id]
        em = discord.Embed(title=f":zzz: Desconectada de {dest}", color = ctx.author.color)
        em.set_footer(text=f"Solicitado por {ctx.author.name}")            
        await ctx.send(embed=em)


# Search whatever u want on youtube!
    @commands.command(help="Busca algo en Youtube", name="search", aliases= ["syt"])
    async def syt(self, ctx, *, search):

        query_string = urllib.parse.urlencode({
                "search_query": search
        })
        html_content = urllib.request.urlopen(
            "http://youtube.com/results?" + query_string
        )
    
        search_content = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
        em = discord.Embed(title = ":bulb: **Search Result**", description = "http://youtube.com/watch?v=" + search_content[0], color = ctx.author.color)
        em.set_thumbnail(url="https://media.discordapp.net/attachments/829223734559637545/829344812913655878/SatanyaBot.png?width=431&height=473")
        em.set_footer(text=f"Solicitado por {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
        await ctx.send(embed=em)



    @commands.command(help="Ajusta el volumen de mi reproducción.", name="volume", aliases = ["vol"])
    async def _volume(self, ctx: commands.Context, *, volume:int):

        if not ctx.author.voice or not ctx.author.voice.channel:
            return await ctx.send('No estás conectado a ningún canal.')

        if not ctx.voice_state.is_playing:
            return await ctx.send('No estoy reproduciendo nada en estos momentos.')

        if ctx.author.voice.channel != ctx.guild.me.voice.channel:
            return await ctx.send("No estás en mi canal de voz.")

        if volume > 150:
            return await ctx.send(':x: El volumen debe de ser entre **0 y 150**')

        ctx.voice_client.source.volume = volume / 150
        em = discord.Embed(title=f"Volumen ajustado a **`{volume}%`**", color = ctx.author.color)
        em.set_footer(text=f"Solicitado por {ctx.author.name}")    
        await ctx.send(embed=em)

    @commands.command(help="Mira que se está reproduciendo actualmente.", aliases=['n', 'now', 'current', 'playing'])
    async def _now(self, ctx: commands.Context):

        await ctx.send(embed=ctx.voice_state.current.create_embed())

    @commands.command(name='pause', help='Pausa la reproducción.', aliases=["pa"])
    async def _pause(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client

        if ctx.author.voice.channel != ctx.guild.me.voice.channel:
            return await ctx.send("No estás en mi canal de voz.")

        voice_channel.pause()
        await ctx.message.add_reaction('⏯')

    @commands.command(name='resume', help="Reanuda la reproducción pausada.", aliases=["r"])
    async def _resume(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client

        if ctx.author.voice.channel != ctx.guild.me.voice.channel:
            return await ctx.send("No estás en mi canal de voz.")


        voice_channel.resume()
        await ctx.message.add_reaction('⏯')

    @commands.command(name="stop", help="Detén la lista de reproducción.", aliases=["st"])
    async def _stop(self, ctx):

        if not ctx.author.voice or not ctx.author.voice.channel:
            return await ctx.send('No estás conectado a ningún canal de voz.')

        if ctx.author.voice.channel != ctx.guild.me.voice.channel:
            return await ctx.send("No estás en mi canal de voz.")

        em = discord.Embed(title=f"🛑 Vale, ya no reproduciré nada más.", color = ctx.author.color)
        em.set_footer(text=f"Solicitado por {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
        await ctx.send(embed=em)
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        voice.stop()

    @commands.command(name='skip', help="Salta la canción actual.", aliases=["sk"])
    async def _skip(self, ctx: commands.Context):

        if not ctx.author.voice or not ctx.author.voice.channel:
            return await ctx.send('No estás conectado a ningún canal de voz.')

        if not ctx.voice_state.is_playing:
            return await ctx.send('No estoy reproduciendo nada...')

        if ctx.author.voice.channel != ctx.guild.me.voice.channel:
            return await ctx.send("No estás en mi canal de voz.")

        voter = ctx.message.author
        if voter == ctx.voice_state.current.requester:
            await ctx.message.add_reaction('⏭')
            ctx.voice_state.skip()

        elif voter.id != ctx.voice_state.current.requester:
            if ctx.voice_state.current.requester not in ctx.author.voice.channel.members:
                await ctx.message.add_reaction('⏭')
                ctx.voice_state.skip()

        elif voter.id not in ctx.voice_state.skip_votes:
            ctx.voice_state.skip_votes.add(voter.id)
            total_votes = len(ctx.voice_state.skip_votes)

            if total_votes >= 3:
                await ctx.message.add_reaction('⏭')
                ctx.voice_state.skip()
            else:
                await ctx.send('Skip vote added, currently at **{}/3**'.format(total_votes))

        else:
            await ctx.send('You have already voted to skip this song.')

    @commands.command(name='queue', help="Mira la lista de reproducción actual.", aliases=["q"])
    async def _queue(self, ctx: commands.Context, *, page: int = 1):

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('La lista está vacía.')

        items_per_page = 10
        pages = math.ceil(len(ctx.voice_state.songs) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue = ''
        for i, song in enumerate(ctx.voice_state.songs[start:end], start=start):
            queue += '`{0}.` [**{1.source.title}**]({1.source.url})\n`{1.source.duration}`\n\n'.format(i + 1, song)

        embed = (discord.Embed(description='**{} Tracks:**\n\n{}'.format(len(ctx.voice_state.songs), queue))
                 .set_footer(text='Viendo página {}/{}'.format(page, pages)))
        await ctx.send(embed=embed)

    @commands.command(name='shuffle', help="Aleatoriza la lista de reproducción.", aliases=["sh"])
    async def _shuffle(self, ctx: commands.Context):


        if ctx.author.voice.channel != ctx.guild.me.voice.channel:
            return await ctx.send("No estás en mi canal de voz.")

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Lista vacía.')

        ctx.voice_state.songs.shuffle()
        await ctx.message.add_reaction('✅')

    @commands.command(name='remove', help="Remueve una canción de la lista", aliases=["re"])
    async def _remove(self, ctx: commands.Context, index: int):


        if ctx.author.voice.channel != ctx.guild.me.voice.channel:
            return await ctx.send("No estás en mi canal de voz.")

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Lista vacía.')

        ctx.voice_state.songs.remove(index - 1)
        await ctx.message.add_reaction('✅')
        

    @commands.command(name='play', help="Reproduce una canción.", aliases=["p"])
    async def _play(self, ctx: commands.Context, *, search: str):

        if not ctx.voice_state.voice:
            await ctx.invoke(self._join)

        async with ctx.typing():
            try:
                source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop)
            except YTDLError as e:
                await ctx.send('**`ERROR`**: {}'.format(str(e)))
            else:
                song = Song(source)

                await ctx.voice_state.songs.put(song)
                await ctx.send(':headphones: Agregado a la lista {}'.format(str(source)))

    @_join.before_invoke
    @_play.before_invoke
    async def ensure_voice_state(self, ctx: commands.Context):
        if not ctx.author.voice or not ctx.author.voice.channel:
            raise commands.CommandError('No estás a ningún canal de voz.')

        if ctx.voice_client:
            if ctx.voice_client.channel != ctx.author.voice.channel:
                raise commands.CommandError("Ya estoy en un cnaal de voz.")


def setup(bot):
    bot.add_cog(music(bot))
