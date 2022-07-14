import os
import platform
import secrets
import time
from datetime import datetime

import alexflipnote
import discord
import pkg_resources
import psutil
from discord.ext import commands


class general(
    commands.Cog,
    command_attrs={
        'cooldown': commands.CooldownMapping.from_cooldown(
            1, 10, commands.BucketType.user
        )
    },
):
    """
    Comandos generales y comunes que todo bot tiene comúnmente.
    Nada fuera de lo común.

    Cooldown: 10s per command
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.alex = alexflipnote.Client()

    # Comando de test/ping
    @commands.command(name='ping')
    async def ping(self, ctx):
        """
        ¡Pong!
        """
        start_time = time.time()

        message = await ctx.send(
            '<a:dscrd_loading:866731675547336721> Probando ping...'
        )

        end_time = time.time()
        await message.edit(
            content='<a:gab_yawning:869405640215375972> Ping terminado.'
        )
        embed = discord.Embed(
            title='🏓 Pong',
            description=(
                f'<a:dscrd_loading:866731675547336721> Ping: **{round(self.bot.latency * 1000)}ms**\n<a:clyde:846625894395412480> API: **{round((end_time - start_time) * 1000)}ms**'
            ),
            color=0xFBF9FA,
        )
        embed.set_thumbnail(
            url='https://media.discordapp.net/attachments/829223734559637545/859941157944557588/headAsset_214x-8.png'
        )
        await ctx.send(embed=embed)

    @commands.command(name='git')
    async def git(self, ctx):
        """
        Código fuente de SatanyaBot
        """
        await ctx.send(
            f'Puedes revisar mi código fuente en {os.environ["GIT"]}'
        )

    @commands.command(name='reverse')
    async def reverse(self, ctx, *, text: str):
        """
        asrever ne otxeT
        """
        reverse = text[::-1]
        await ctx.reply(f'{reverse}')

    @commands.command(name='invite')
    async def invite(self, ctx: commands.Context):
        """
        Links de invitación de SatanyaBot y al server
        """
        embed = discord.Embed(
            title='¿Quieres agregarme a tu servidor o unirte al mío?',
            description='Aquí tienes los enlaces para unirte a mi servidor o invitarme al tuyo.',
            color=0xFBF9FA,
        )
        embed.add_field(
            name='<:join:847940361937879051> Link de server',
            value='[「SatanyaBot」](https://discord.gg/bqcdKxuW3X)',
            inline=True,
        )
        embed.add_field(
            name='<:join:847940361937879051> Link SatanyaBot',
            value=f'[Invítame]({discord.utils.oauth_url(self.bot.user.id, permissions=discord.Permissions(137442610369))})',
            inline=True,
        )
        embed.set_image(
            url='https://media.discordapp.net/attachments/829223734559637545/859608410537459752/bannerSatanyaBot_Logotipo4x.png'
        )
        await ctx.send(
            '<:okay:846612389046386689> Te he enviado mis enlaces de invitación',
            delete_after=10,
        )
        await ctx.author.send(embed=embed)

    @commands.command(name='about')
    async def about(self, context):
        """
        Información útil (y no tan útil) del bot.
        """
        # Permite determinar el tiempo que lleva desde su primer proceso activo
        delta_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        uptime = f'{days}d, {hours}h, {minutes}m, {seconds}s'

        block = '`' * 3

        cpuUsage = psutil.cpu_percent(1)
        ramUsage = psutil.virtual_memory()[2]

        # se que esto puede q sea malo pero meh, es por si se llega a cambiar uno de los tags y no se actualiza manualmente
        kuro = await self.bot.fetch_user(457574130401804288)
        igna = await self.bot.fetch_user(996175229393059930)

        embed = discord.Embed(
            title='¡Hola, soy SatanyaBot!',
            description='🌸 SatanyaBot - la primer bot de Discord **open source y en español** desarrollada en Python.\n\nSatanyaBot nació con la idea de crear una alternativa de código abierto a los bots en español de Discord como Chocolat, Nekotina, Ruka y otros.\n\nRecuerda que si quieres ver mis comandos usa **nya>help**',
            color=0xFBF9FA,
            timestamp=datetime.utcnow(),
        )
        embed.set_author(
            name=f'SatanyaBot | v{os.environ["VERSION"]}',
            icon_url='https://media.discordapp.net/attachments/829223734559637545/859941157944557588/headAsset_214x-8.png',
        )

        embed.add_field(
            name='Noticias:',
            value=f'{block}fix\n📰 ¡Ahora puedes encontrarme en top.gg! nya>vote(〃＾▽＾〃)\n{block}',
            inline=False,
        )
        embed.add_field(
            name='Creador y Colaboradores:',
            value=f'[**{kuro}**](https://linktr.ee/KuroCat56) | [**{igna}**](https://www.igna.lol)',
            inline=False,
        )
        embed.add_field(
            name='Mi versión de Python:',
            value=f'{platform.python_version()}',
            inline=True,
        )
        embed.add_field(
            name='Encendida desde hace:', value=f'{uptime}', inline=True
        )
        embed.add_field(
            name='Uso de recursos:',
            value=f'{ramUsage}% RAM\n{cpuUsage}% CPU',  # RAM
            inline=True,
        )
        embed.add_field(
            name='Prefijo:', value=f'{os.environ["PREFIX"]}', inline=True
        )
        embed.add_field(
            name='# Comandos:',
            value=f'{len([x.name for x in self.bot.commands])}',
            inline=True,
        )
        embed.add_field(
            name='# Servers:', value=f'{len(self.bot.guilds)}', inline=True
        )
        # statistics - Extraído de https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/stats.py#L216-L263
        total_members = 0
        # total_unique = len(self.bot.users)

        text = 0
        voice = 0
        guilds = 0
        for guild in self.bot.guilds:
            guilds += 1
            if guild.unavailable:
                continue

            total_members += guild.member_count
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    text += 1
                elif isinstance(channel, discord.VoiceChannel):
                    voice += 1

        embed.add_field(
            name='# Miembros', value=f'{total_members} totales', inline=True
        )
        embed.add_field(
            name='# Canales', value=f'{text + voice} totales', inline=True
        )
        embed.add_field(
            name='Cumpleaños 🍰', value='31/01/2021 | 18:06', inline=False
        )
        embed.add_field(
            name='Donaciones <a:cutestars:846625824538886214>',
            value='[Ko-fi](https://ko-fi.com/kurocat56)',
            inline=True,
        )
        embed.add_field(
            name='Top.gg <:wumpus_star:846611108784504872>',
            value='[Vota por mi](https://top.gg/bot/805589802484760577)',
            inline=True,
        )
        embed.add_field(
            name='Enlaces',
            value='[Github](https://github.com/KuroCat56/SatanyaBot) **|** [Servidor de Soporte](https://discord.gg/bqcdKxuW3X) **|** [Invítame](https://discord.com/oauth2/authorize?client_id=805589802484760577&scope=bot&permissions=137442610369)',
            inline=False,
        )
        version = pkg_resources.get_distribution('discord.py').version
        embed.set_footer(
            text=f'Desarrollada en discord.py v{version}',
            icon_url='http://i.imgur.com/5BFecvA.png',
        )
        embed.set_image(
            url='https://media.discordapp.net/attachments/829223734559637545/859608410537459752/bannerSatanyaBot_Logotipo4x.png'
        )
        await context.send(embed=embed)

    @commands.command(
        aliases=['si', 'server']
    )  # Extraído de https://github.com/cree-py/RemixBot/blob/master/cogs/info.py
    async def serverinfo(self, ctx):
        """Información básica del servidor."""
        guild = ctx.guild
        guild_age = (ctx.message.created_at - guild.created_at).days
        created_at = f"Servidor creado {guild.created_at.strftime('%b %d %Y │ %H:%M')}.\n¡Eso fue hace {guild_age} días!"

        em = discord.Embed(description=created_at, color=0xFBF9FA)
        em.add_field(name='Owner', value=guild.owner, inline=False)
        em.add_field(name='Miembros', value=len(guild.members), inline=False)
        em.add_field(name='Roles', value=len(guild.roles))
        em.add_field(
            name='<:dscrd_channel:851449868722896936> Canales de texto',
            value=len(guild.text_channels),
        )
        em.add_field(
            name='<:dscrd_voice:862873567204212776> Canales de voz',
            value=len(guild.voice_channels),
        )
        if guild.icon:
            em.set_thumbnail(url=guild.icon.url)
            em.set_author(name=guild.name, icon_url=guild.icon.url)

        em.set_author(name=guild.name)

        await ctx.send(embed=em)

    @commands.command(name='opensource', aliases=['open'])
    async def opensource(self, ctx):
        embed = discord.Embed(
            title='SatanyaBot apoya el open source y tú también deberías',
            description='Soy una bot open source así que todo mi desarrollo está sostenido gracias al apoyo de otros desarrolladores y demás proyectos open source.\n\n<:satan_yeih:846553057999454219> Si deseas aportar ayuda y apoyo al proyecto revisa los siguientes enlaces: ',
            color=0xFBF9FA,
        )
        embed.add_field(
            name='Desarrollo',
            value=f'[Github]({os.environ["GIT"]}) **|** [Servidor de Soporte](https://discord.gg/bqcdKxuW3X) **|** [Trello](https://trello.com/b/Z432JC83)',
            inline=False,
        )
        embed.add_field(
            name='Donaciones <a:cutestars:846625824538886214>',
            value='[Ko-fi](https://ko-fi.com/kurocat56)',
            inline=False,
        )
        embed.set_thumbnail(
            url='https://media.discordapp.net/attachments/829223734559637545/859941157944557588/headAsset_214x-8.png'
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['dn', 'donation'])
    async def donate(self, ctx: commands.Context):
        """
        Links de invitación de SatanyaBot y al server
        """
        embed = discord.Embed(
            title='¿Te gustaría apoyar el desarrollo del proyecto?',
            description='Todo el dinero que se invierte va directamente para mantener el VPS donde SatanyaBot se mantiene activa. Aportando tan poco como $1 ayudas a mantener a flote el proyecto.',
            color=0xFBF9FA,
        )
        embed.add_field(
            name='<:join:847940361937879051> Enlaces de donaciones',
            value='[Ko-fi](https://ko-fi.com/kurocat56)',
            inline=True,
        )
        embed.set_image(
            url='https://media.discordapp.net/attachments/829223734559637545/859608410537459752/bannerSatanyaBot_Logotipo4x.png'
        )
        await ctx.send(
            '<:okay:846612389046386689> Te he enviado mis enlaces de donación',
            delete_after=10,
        )
        await ctx.author.send(embed=embed)

    @commands.command(aliases=['topgg'])
    async def vote(self, ctx: commands.Context):
        """
        Perfil de SatanyaBot en top.gg
        """
        embed = discord.Embed(
            title='¡Ayúdame a crecer en top.gg',
            description='Si te gustaría ayudar al proyecto más allá de aportar donaciones puedes ayudar a calificar a SatanyaBot en la plataforma de top.gg para que sea mucho más conocida.',
            color=0xFBF9FA,
        )
        embed.add_field(
            name='<:wumpus_star:846611108784504872> SatanyaBot en top.gg',
            value=f'[Top.gg](https://top.gg/bot/{self.bot.user.id})',
            inline=True,
        )
        embed.set_image(
            url='https://media.discordapp.net/attachments/829223734559637545/859608410537459752/bannerSatanyaBot_Logotipo4x.png'
        )
        await ctx.send(
            '<:okay:846612389046386689> Te he enviado mi perfil de top.gg',
            delete_after=10,
        )
        await ctx.author.send(embed=embed)

    @commands.command(name='randomcolor', aliases=['racolor'])
    async def randomcolor(self, ctx: commands.Context):
        """
        ¿Buscas colores? Toma uno
        """
        async with ctx.typing():
            hex = secrets.token_hex(3)
            color = await self.alex.colour(colour=hex)

            embed = discord.Embed(
                title=f'🎨 Color aleatorio elegido: {color.name} | {color.hex}'
            )
            embed.set_image(url=color.image)
            embed.set_footer(text='🎨 Powered by api.alexflipnote.dev')
        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(general(bot))
