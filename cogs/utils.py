import asyncio
import inspect
import math
from typing import Union
import re
import discord
from aiohttp import ClientSession
from discord.ext import commands
from googlesearch import search


class Utils(
    commands.Cog,
    command_attrs={
        'cooldown': commands.CooldownMapping.from_cooldown(
            1, 15, commands.BucketType.user
        )
    },
):
    """
    Comando útiles (y no tan útiles)

    Cooldown: 15s per command
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.session = ClientSession()

    async def translate(self, source, target, text):
        """
        Traduce un texto a un idioma especifico
        """
        url = f'https://translate.igna.ooo/api/v1/{source}/{target}/{text}'
        async with self.session.get(url) as resp:
            data = await resp.json()
        return data['translation']

    # Estraído de https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/meta.py#L557
    async def say_permissions(
            self,
            ctx,
            member: discord.Member,
            channel: Union[discord.abc.GuildChannel, discord.Thread],
    ):
        permissions = channel.permissions_for(member)
        e = discord.Embed(colour=member.colour)
        avatar = member.display_avatar.with_static_format('png')
        e.set_author(name=str(member), url=avatar)
        allowed, denied = [], []
        for name, value in permissions:
            name = name.replace('_', ' ').replace('guild', 'server').title()
            if value:
                allowed.append(name)
            else:
                denied.append(name)

        e.add_field(name='Permitido', value='\n'.join(allowed))
        e.add_field(name='Denegado', value='\n'.join(denied))
        await ctx.send(embed=e)

    def is_guild_owner():
        def predicate(ctx):
            return (
                    ctx.guild is not None and ctx.guild.owner_id == ctx.author.id
            )

        return commands.check(predicate)

    @commands.hybrid_command(name="remind", description="(BETA)Intentaré recordarte cualquier cosa que necesites.")
    async def remind(self, ctx, time, *, task):
        def convert(_time: str):
            pattern = r'((\d+)d)?((\d+)h)?((\d+)m)?((\d+)s)?'
            matches = re.match(pattern, _time)
            if matches:
                days = int(matches.group(2) or 0)
                hours = int(matches.group(4) or 0)
                minutes = int(matches.group(6) or 0)
                seconds = int(matches.group(8) or 0)
                total = seconds + (minutes * 60) + (hours * 3600) + (days * 86400)
                return total
            return None

        converted_time = convert(time)

        if converted_time == -1:
            await ctx.send('Comando inválido')
            return
        if converted_time == -2:
            await ctx.send('Debes de especificar usando enteros')
            return

        await ctx.send(
            f'⏱️ {ctx.author.mention}, tu recordatorio para **{task}** fue activado y serás recordado en **{time}**'
        )

        await asyncio.sleep(converted_time)
        await ctx.send(
            f'⏰ {ctx.author.mention}, tu recordatorio por **{task}** ha terminado.'
        )

    @commands.command(name='prefix')
    async def prefix(self, ctx):
        """
        Tengo varios prefijos, prueba a usar el que más te guste.
        """
        await ctx.send(
            f'Actualmente mis prefijos son `nya>`, `nya `, `>>` y `@{self.bot.user.name}` ♪└( ＾ω＾ )」'
        )

    @commands.command()
    async def poll(self, ctx, *, poll_title=None):
        """
        Crea una mini encuesta para lo que gustes
        """
        if poll_title is None:
            await ctx.send('¡Debes especificar un título! (。﹏。)')
        else:
            embed = discord.Embed(
                title=f'📊 {poll_title}',
                color=0xFBF9FA,
            )
            embed.set_footer(
                text=f'Encuesta por: {ctx.message.author} - ¡Reacciona para votar!'
            )
            embed_message = await ctx.send(embed=embed)
            await embed_message.add_reaction('👍')
            await embed_message.add_reaction('👎')
            await embed_message.add_reaction('🤷')

    @commands.command()  # Extraído de https://github.com/cree-py/RemixBot/blob/master/cogs/utility.py
    async def source(self, ctx, command):
        """Get the source code for any command."""
        source = inspect.getsource(self.bot.get_command(command).callback)
        if not source:
            return await ctx.send(f'{command} is not a valid command.')
        try:
            await ctx.send(f'```py\n{source}\n```')
        except:
            await ctx.send(
                'El bloque de código es demasiado largo como para enviarlo. Será mejor que uses `nya>git` para buscar el apartado por tu cuenta. <:doki_hmm:846549184807043133>'
            )

    @commands.command(aliases=['botperms'])
    @commands.guild_only()
    @commands.check_any(commands.is_owner(), is_guild_owner())
    async def botpermissions(
            self,
            ctx,
            *,
            channel: Union[discord.abc.GuildChannel, discord.Thread] = None,
    ):
        """
        Muestra los permisos del bot en un canal específico o en el actual.
        Esta es una buena manera para checar si el bot tiene los permisos necesarios para ejecutar ciertos comandos.
        """
        channel = channel or ctx.channel
        member = ctx.guild.me
        await self.say_permissions(ctx, member, channel)

    @commands.command(aliases=['perms'])
    @commands.guild_only()
    async def permissions(
            self,
            ctx,
            member: discord.Member = None,
            channel: Union[discord.abc.GuildChannel, discord.Thread] = None,
    ):
        """
        Muestra los permisos de un usuario en un canal específico o en el actual.
        """
        channel = channel or ctx.channel
        if member is None:
            member = ctx.author

        await self.say_permissions(ctx, member, channel)

    @commands.command()
    async def trello(self, ctx):
        """
        Tablero oficial de Trello para checar los avances.
        """
        embed = discord.Embed(
            title='¿Qué hay pendiente en la lista?',
            description='🌸 SatanyaBot siempre está en desarrollo agregando nuevas características y arreglando otras.\n🍒 Si te da curiosidad saber en qué se está trabajando checa el link de abajo.',
            color=0xFBF9FA,
        )
        embed.add_field(
            name='Tablero oficial de SatanyaBot',
            value='[Trello](https://trello.com/b/Z432JC83)',
        )
        embed.set_thumbnail(
            url='https://media.discordapp.net/attachments/829223734559637545/859941157944557588/headAsset_214x-8.png'
        )
        embed.set_image(
            url='https://images.unsplash.com/photo-1555231955-348aa2312e19'
        )
        await ctx.send(embed=embed)

    #    @commands.command()
    #    @commands.check_any(commands.is_owner(), is_guild_owner())
    #    async def giveaway(self, ctx):
    #        """
    #        ¿Quieres hacer un giveaway? Responde estas simples preguntas.
    #
    #        Solo el propietario del servidor puede realizar los giveaway.
    #        """

    #        def convert(time):
    #            pos = ['s', 'm', 'h', 'd']
    #            time_dict = {'s': 1, 'm': 60, 'h': 3600, 'd': 3600 * 24}
    #            unit = time[-1]
    #
    #            if unit not in pos:
    #                return -1
    #            try:
    #                val = int(time[:-1])
    #            except:
    #                return -2
    #            return val * time_dict[unit]

    #        await ctx.send(
    #            'Por favor responde a estas preguntas para empezar el giveaway.\n**Sólo tienes 15 segundos para responder cada pregunta.**'
    #        )

    #        questions = [
    #            '1. **¿En qué canal se hará el giveaway?**',
    #            '2. **¿Cuál será la duración del giveaway?** (Ejemplo: 30s, 5h, 3d)',
    #            '3. **¿Qué es el premio que se sorteará?**',
    #        ]

    #        answers = []

    #        def check(m):
    #            return m.author.id == ctx.author.id and m.channel == ctx.channel

    #        for i in questions:
    #            await ctx.send(i)

    #            try:
    #                msg = await self.bot.wait_for(
    #                    'message', timeout=15.0, check=check
    #                )
    #            except asyncio.TimeoutError:
    #                await ctx.send(
    #                    '⌛ Tardaste más de 15 segundos en responder la pregunta. Vuelve a intentarlo pero sé más rápido.'
    #                )
    #                return
    #            else:
    #                answers.append(msg.content)

    #        try:
    #            c_id = int(answers[0][2:-1])
    #        except:
    #            await ctx.send(
    #                f'<:nope:846611758445625364> Hubo un problema con el canal mencionado. Intenta de nuevo mencionando el canal así: {ctx.channel.mention}'
    #            )
    #            return

    #        channel = self.bot.get_channel(c_id)

    #        time = convert(answers[1])
    #        if time == -1:
    #            await ctx.send(
    #                f'<:nope:846611758445625364> Hubo un problema con el tiempo ingresado. Intenta de nuevo usando formato correcto. (*s, m, h* o *d*)'
    #            )
    #            return
    #        elif time == -2:
    #            await ctx.send(
    #                '<:nope:846611758445625364> El tiempo ingresado no es un entero. Intenta de nuevo usando un número entero.'
    #            )
    #            return

    #        prize = answers[2]
    #        await ctx.send(
    #            f'El giveaway se realizará en {channel.mention} y durará {answers[1]}'
    #        )

    #        embed = discord.Embed(
    #            title='**¡GIVEAWAY!**',
    #            description=(f'{prize}'),
    #            color=ctx.author.color,
    #        )
    #        embed.add_field(name='Organizado por:', value=ctx.author.mention)
    #        embed.set_thumbnail(
    #            url='https://emoji.gg/assets/emoji/7825_blurple_tada.png'
    #        )
    #        embed.set_footer(text=f'Termina en {answers[1]} a partir de ahora.')

    #        my_msg = await channel.send(embed=embed)
    #        await my_msg.add_reaction('🎉')
    #        await asyncio.sleep(time)

    #        for reaction in my_msg.reactions:
    #           users = [user async for user in reaction.users()]
    #           users.pop(users.index(self.bot.user))
    #            winner = random.choice(users)
    #            await channel.send(
    #                f'🎉 ¡Felicidades! El usuario {winner.mention} ganó **{prize}** 🎉'
    #            )

    @commands.command(aliases=['ggl'])
    async def google(self, ctx, *, google):
        """
        Muestra los primeros tres resultados de una búsqueda en Google.
        """
        try:
            results = search(f'{google}', num_results=3, lang='es')
            embed = discord.Embed(
                title=f'Esto es lo que he encontrado en Google sobre:\n__{google}__',
                description=f'1️⃣ {results[0]}\n\n2️⃣ {results[1]}\n\n3️⃣ {results[2]}',
                color=ctx.author.color,
            )
            await ctx.send(embed=embed)
        except:
            await ctx.send('Parece que hubo un error.')

    @commands.command()
    async def jumbo(self, ctx, emoji: discord.PartialEmoji):
        """
        Deja te paso ese emoji para que lo veas mejor.
        """
        embed = discord.Embed(
            title=emoji.name,
            url=emoji.url,
            colour=discord.Color.random(),
        )
        embed.set_image(url=emoji.url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['traducir', 'traductor'])
    async def translate(self, ctx, target, source, *, text):
        """
        Traducción rápida usando el traductor de Google.
        """
        block = '`' * 3
        try:
            async with self.session.get(
                    f'https://translate.igna.ooo/api/v1/{source}/{target}/{text}'
            ) as r:
                data = await r.json()
                text2 = data['translation']
            embed = discord.Embed(
                description=f'Traducción de __{target}__ a __{source}__:',
                color=ctx.author.color,
            )
            embed.add_field(
                name='Texto ingresado:',
                value=f'{block}\n{text}\n{block}',
                inline=False,
            )
            embed.add_field(
                name='Texto traducido:',
                value=f'{block}\n{text2}\n{block}',
                inline=False,
            )
            embed.set_footer(
                text=f'Pedido por {ctx.author.name}',
            )
            await ctx.reply(embed=embed)
        except:
            embed = discord.Embed(
                description=f'**Parece que hubo un error:**\n1️⃣ Es probable que debas de checar si el lenguaje que escibiste (**`{target}`** y **`{source}`**) esté bien escrito.\nPuedes comprobarlo aquí: http://www.lingoes.net/en/translator/langcode.htm \n2️⃣ Es probable que el lenguaje que escribiste (**`{target}`** o **`{source}`** no esté disponible.)',
                color=ctx.author.color,
            )
            await ctx.send(embed=embed)

    @commands.command()
    @commands.check_any(
        commands.is_owner(), commands.has_permissions(manage_messages=True)
    )
    async def clear(self, ctx, number: int):
        """
        Borra todos mis mensajes en el canal actual.
        """
        counter = 0
        async for message in ctx.channel.history(limit=250):
            if message.author.id == ctx.bot.user.id:
                await message.delete()
                counter += 1
            if counter >= number:
                break
        embed = discord.Embed(
            title=f'🧹 He borrado `{number}` de mis mensajes en este canal',
            color=ctx.author.color,
        )
        await ctx.send(embed=embed, delete_after=10)

    @commands.command(name='purge', aliases=['pu'])
    @commands.check_any(
        commands.is_owner(), commands.has_permissions(manage_messages=True)
    )
    async def purge(self, ctx, *, amount: int):
        """
        Borra x cantidad de mensajes en el canal actual.
        """
        embed = discord.Embed(
            color=ctx.author.color, timestamp=ctx.message.created_at
        )
        if amount > 50:
            embed.title = 'No puedo borrar +50 de mensajes.'
            return await ctx.send(embed=embed, delete_after=5)
        embed.title = f'Borrados {amount} mensajes en este canal.'
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(embed=embed, delete_after=5)

    @commands.command(name='suma', aliases=['add'])
    async def suma(self, ctx, left: float, right: float):
        """
        Suma dos números entre si.
        """
        result = left + right
        embed = discord.Embed(
            description=result, color=discord.Colour.random()
        )
        await ctx.reply(embed=embed)

    @commands.command(name='resta', aliases=['substract'])
    async def resta(self, ctx, left: float, right: float):
        """
        Resta de dos números entre si.
        """
        result = left - right
        embed = discord.Embed(
            description=result, color=discord.Colour.random()
        )
        await ctx.reply(embed=embed)

    @commands.command(name='multiplicar', aliases=['mult', 'multiply'])
    async def multiplicar(self, ctx, left: float, right: float):
        """
        Multipla dos números entre si.
        """
        result = left * right
        embed = discord.Embed(
            description=result, color=discord.Colour.random()
        )
        await ctx.reply(embed=embed)

    @commands.command(name='dividir', aliases=['divide'])
    async def dividir(self, ctx, left: float, right: float):
        """
        Divide entre dos números entre si.
        """
        result = left / right
        embed = discord.Embed(
            description=result, color=discord.Colour.random()
        )
        await ctx.reply(embed=embed)

    @commands.command(name='square', aliases=['cuadrado'])
    async def square(self, ctx, number):
        """
        Cuadrado de un número.
        """
        result = float(number) * float(number)
        embed = discord.Embed(
            description=result, color=discord.Colour.random()
        )
        await ctx.reply(embed=embed)

    @commands.command(name='squareroot', aliases=['raíz'])
    async def squareroot(self, ctx, number: float):
        """
        Raíz cuadrada de un número.
        """
        result = math.sqrt(number)
        embed = discord.Embed(
            description=result, color=discord.Colour.random()
        )
        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Utils(bot))