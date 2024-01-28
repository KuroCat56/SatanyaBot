import wavelink
import discord
from discord.ext import commands
import typing as t
import asyncio
import os


class Player(wavelink.Player):
    track_queue: t.List[wavelink.YouTubeTrack] = []
    invoked_at: discord.TextChannel = None
    player_message: discord.Message = None
    in_loop: bool = None
    current_index = 0

    async def play(self):
        await super().play(self.track_queue[self.current_index])
        if not self.in_loop:
            self.current_index += 1

    async def skip(self):
        await self.play()

    async def prev_song(self):
        self.current_index -= 2
        await self.play()


class MusicButtons(discord.ui.View):
    def __init__(self, player: Player):
        self.player = player
        super().__init__(timeout=None)
        if player.current_index >= 2:
            self.previous_song.disabled = False

    @discord.ui.button(emoji="🟰", style=discord.ButtonStyle.gray, disabled=False)
    async def list_queue(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.user.voice:
            return await interaction.response.send_message("No estas conectado a ningún canal de voz.", ephemeral=True)
        elif interaction.user.voice.channel != interaction.guild.me.voice.channel:
            return await interaction.response.send_message("No estas conectado a mi canal de voz.", ephemeral=True)

        player = self.player
        if len(player.track_queue) > 0:
            total = []
            for index, item in enumerate(player.track_queue):
                if index + 1 == player.current_index:
                    total.append(f"🎵 {index + 1}.- {item.title}")
                else:
                    total.append(f"{index + 1}.- {item.title}")

            embed = discord.Embed(color=0xC39BD3)
            embed.title = "Lista de reproducción"
            res = "\n".join(total)
            embed.description = f"""```yaml\n{res}```"""
            return await interaction.response.send_message(embed=embed)
        await interaction.response.send_message("Queue is empty", ephemeral=True)

    @discord.ui.button(emoji="⏮️", style=discord.ButtonStyle.gray, disabled=True)
    async def previous_song(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.user.voice:
            return await interaction.response.send_message("No estas conectado a ningún canal de voz.", ephemeral=True)
        elif interaction.user.voice.channel != interaction.guild.me.voice.channel:
            return await interaction.response.send_message("No estas conectado a mi canal de voz.", ephemeral=True)

        await self.player.prev_song()

    @discord.ui.button(emoji="⏸️", style=discord.ButtonStyle.green, disabled=False)
    async def resume_or_pause(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.user.voice:
            return await interaction.response.send_message("No estas conectado a ningún canal de voz.", ephemeral=True)
        elif interaction.user.voice.channel != interaction.guild.me.voice.channel:
            return await interaction.response.send_message("No estas conectado a mi canal de voz.", ephemeral=True)

        if not self.player.is_paused():
            button.emoji = "▶️"
            await self.player.pause()
        else:
            button.emoji = "⏸️"
            await self.player.resume()
        await interaction.response.edit_message(view=self)

    @discord.ui.button(emoji="⏭️", style=discord.ButtonStyle.gray, disabled=False)
    async def next_song(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.user.voice:
            return await interaction.response.send_message("No estas conectado a ningún canal de voz.", ephemeral=True)
        elif interaction.user.voice.channel != interaction.guild.me.voice.channel:
            return await interaction.response.send_message("No estas conectado a mi canal de voz.", ephemeral=True)

        if self.player.current_index + 1 > len(self.player.track_queue):
            await interaction.response.send_message("No hay mas canciones!")
            button.disabled = True
            await self.player.player_message.edit(view=self)
            return
        await self.player.skip()

    @discord.ui.button(emoji="♾️", style=discord.ButtonStyle.gray, disabled=True)
    async def infinite_queue(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.user.voice:
            return await interaction.response.send_message("No estas conectado a ningún canal de voz.", ephemeral=True)
        elif interaction.user.voice.channel != interaction.guild.me.voice.channel:
            return await interaction.response.send_message("No estas conectado a mi canal de voz.", ephemeral=True)
        await interaction.response.send_message("Not implemented.", ephemeral=True)


async def leave(player: Player):
    await asyncio.sleep(60)
    if not player.is_playing and len(player.track_queue) < 1:
        vc = player.guild.voice_client
        await vc.disconnect(force=True)


class Music(commands.GroupCog, name='music'):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        bot.loop.create_task(self.connect_nodes())

    async def connect_nodes(self):
        """Connect to our Lavalink nodes."""
        await self.bot.wait_until_ready()
        node: wavelink.Node = wavelink.Node(uri=os.getenv("LAVALINK_HOST"), password=os.getenv("LAVALINK_PASSWORD"),
                                            secure=os.getenv("LAVALINK_SSL") == "true")
        await wavelink.NodePool.connect(client=self.bot, nodes=[node])

    @commands.Cog.listener()
    async def on_wavelink_track_start(self, payload: wavelink.TrackEventPayload):
        player: Player = payload.player
        embed = discord.Embed(color=0xC39BD3)
        embed.set_author(name="Reproduciendo...", icon_url="https://media.tenor.com/B-pEg3SWo7kAAAAi/disk.gif")
        embed.description = f"[{payload.track.title}]({payload.track.uri})"
        message = await player.invoked_at.send(embed=embed, view=MusicButtons(payload.player))
        player.player_message = message

    @commands.Cog.listener()
    async def on_wavelink_track_end(self, payload: wavelink.TrackEventPayload):
        player: Player = payload.player
        if payload.reason == "REPLACED":
            pass
        else:
            if len(player.track_queue) > 0:
                await player.play()
            else:
                await self.bot.loop.create_task(leave(player))

        await player.player_message.delete()

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        print(f'Node: <{node.id}> is ready!')

    @commands.hybrid_command(name="connect")
    async def _join_voice(self, ctx: commands.Context):
        if not ctx.voice_client:
            vc: Player = await ctx.author.voice.channel.connect(cls=Player)
            vc.invoked_at = ctx.channel
            return await ctx.send(f"Conectado a {vc.channel.mention}", delete_after=3)
        elif not ctx.author.voice:
            return await ctx.send("No estas en un canal de voz!")
        elif ctx.author.voice.channel != ctx.guild.me.voice.channel:
            return await ctx.send("No estamos en el mismo canal de voz!")
        await ctx.send("Already in audio!")

    @commands.hybrid_command(name='play')
    async def _play(self, ctx: commands.Context, *, search: wavelink.YouTubeTrack):
        """Añade una canción a la lista"""
        if not ctx.voice_client:
            vc: Player = await ctx.author.voice.channel.connect(cls=Player)
            vc.invoked_at = ctx.channel
            await ctx.send(f"Conectado a {vc.channel.mention}", delete_after=3)
            vc: Player = ctx.voice_client
        elif not ctx.author.voice:
            return await ctx.send("No estas en un canal de voz!")
        elif ctx.author.voice.channel != ctx.guild.me.voice.channel:
            return await ctx.send("No estamos en el mismo canal de voz!")
        else:
            vc: Player = ctx.voice_client

        vc.track_queue.append(search)
        await ctx.send("Added to queue: `{}`".format(search.title), delete_after=3)
        if not vc.is_playing():
            await vc.play()

    @commands.hybrid_command(name="skip")
    async def _skip_song(self, ctx: commands.Context):
        """Salta una canción"""
        if not ctx.voice_client:
            return await ctx.send("I'm not in a voice channel")
        elif not ctx.author.voice:
            return await ctx.send("No estas en un canal de voz!")
        elif ctx.author.voice.channel != ctx.guild.me.voice.channel:
            return await ctx.send("No estamos en el mismo canal de voz!")
        else:
            vc: Player = ctx.voice_client
        if vc.current_index + 1 > len(vc.track_queue):
            return await ctx.reply("No hay mas canciones!")
        await vc.skip()
        if ctx.message:
            return await ctx.message.add_reaction("⏭️")

    @commands.hybrid_command(name="remove")
    async def _remove_from_queue(self, ctx: commands.Context, index: int):
        """Elimina una canción de la lista"""
        if not ctx.voice_client:
            return await ctx.send("No estoy en un canal de voz")
        elif not ctx.author.voice:
            return await ctx.send("No estas en un canal de voz!")
        elif ctx.author.voice.channel != ctx.guild.me.voice.channel:
            return await ctx.send("No estamos en el mismo canal de voz!")
        else:
            vc: Player = ctx.voice_client
        await ctx.send("Removed {}".format(vc.track_queue[index - 1]))
        vc.track_queue.pop(index - 1)

    @commands.hybrid_command(name="pause")
    async def _pause(self, ctx: commands.Context):
        """Pausa el reproductor"""
        if not ctx.voice_client:
            return await ctx.send("No estoy en un canal de voz")
        elif not ctx.author.voice:
            return await ctx.send("No estas en un canal de voz!")
        elif ctx.author.voice.channel != ctx.guild.me.voice.channel:
            return await ctx.send("No estamos en el mismo canal de voz!")
        else:
            vc: Player = ctx.voice_client
        await vc.pause()
        if ctx.message:
            return await ctx.message.add_reaction("⏸️")

    @commands.hybrid_command(name="resume")
    async def _resume(self, ctx: commands.Context):
        """Continua el reproductor"""
        if not ctx.voice_client:
            return await ctx.send("No estoy en un canal de voz")
        elif not ctx.author.voice:
            return await ctx.send("No estas en un canal de voz!")
        elif ctx.author.voice.channel != ctx.guild.me.voice.channel:
            return await ctx.send("No estamos en el mismo canal de voz!")
        else:
            vc: Player = ctx.voice_client
        await vc.resume()
        if ctx.message:
            return await ctx.message.add_reaction("⏸️")

    @commands.hybrid_command(name="stop")
    async def _stop(self, ctx: commands.Context):
        """Deten el reproductor"""
        if not ctx.voice_client:
            return await ctx.send("No estoy en un canal de voz")
        elif not ctx.author.voice:
            return await ctx.send("No estas en un canal de voz!")
        elif ctx.author.voice.channel != ctx.guild.me.voice.channel:
            return await ctx.send("No estamos en el mismo canal de voz!")
        else:
            vc: Player = ctx.voice_client
        vc.track_queue.clear()
        vc.cleanup()
        await vc.stop()
        if ctx.message:
            return await ctx.message.add_reaction("⏸️")

    @commands.hybrid_command(name="queue")
    async def _queue(self, ctx: commands.Context):
        """Lista de reproducción"""
        if not ctx.voice_client:
            return await ctx.send("I'm not in a voice channel")
        elif not ctx.author.voice:
            return await ctx.send("No estas en un canal de voz!")
        elif ctx.author.voice.channel != ctx.guild.me.voice.channel:
            return await ctx.send("No estamos en el mismo canal de voz!")
        else:
            vc: Player = ctx.voice_client
        queue = vc.track_queue
        if len(queue) > 0:
            total = []
            for index, item in enumerate(queue):
                if index + 1 == vc.current_index:
                    total.append(f"🎵 {index + 1}.- {item.title}")
                else:
                    total.append(f"{index + 1}.- {item.title}")

            embed = discord.Embed(color=0xC39BD3)
            embed.title = "Lista de reproducción:"
            res = "\n".join(total)
            embed.description = f"""```yaml\n{res}```"""
            return await ctx.send(embed=embed)
        await ctx.send("Queue is empty")

    @commands.hybrid_command(name="disconnect")
    async def _disconnect(self, ctx: commands.Context):
        """Desconéctame del canal de voz"""
        if not ctx.voice_client:
            return await ctx.send("I'm not in a voice channel")
        else:
            vc: Player = ctx.voice_client
        await leave(vc)


async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot))
