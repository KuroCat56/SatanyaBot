import discord, platform
import config
from discord.ext import commands
from datetime import datetime
import psutil
from os import getpid
import pkg_resources
import time
import main

def lines_of_code():
    """
    I did not write this code.
    This code was taken off of a tag in discord.gg/dpy owned by Dutchy#6127
    I don't know if this is licensed
    but alas
    :return:
    """
    import pathlib
    p = pathlib.Path('./')
    cm = cr = fn = cl = ls = fc = 0
    for f in p.rglob('*.py'):
        if str(f).startswith("venv"):
            continue
        fc += 1
        with f.open() as of:
            for l in of.readlines():
                l = l.strip()
                if l.startswith('class'):
                    cl += 1
                if l.startswith('def'):
                    fn += 1
                if l.startswith('async def'):
                    cr += 1
                if '#' in l:
                    cm += 1
                ls += 1
    return {
        "comments": cm,
        "coroutine": cr,
        "functions": fn,
        "classes": cl,
        "lines": ls,
        "files": fc
    }

lines = lines_of_code()

class general(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 10, commands.BucketType.user)}):
  """
  Comandos generales y comunes que todo bot tiene comúnmente.
  Nada fuera de lo común.
  
  Cooldown: 10s per command
  """
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  #Comando de test/ping
  @commands.command(name="ping")
  async def ping(self, ctx: commands.Context):
        """
        ¡Pong!
        """
        start_time = time.time()
        
        message = await ctx.send("<a:dscrd_loading:866731675547336721> Probando ping...")
        
        typings = time.monotonic()
        await ctx.trigger_typing()
        typinge = time.monotonic()
        typingms = round((typinge - typings) * 1000)
        
        end_time = time.time()
        #await message.edit(content=f"Pong! {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms\n Typing: {typingms}")
        await message.edit(content="<a:gab_yawning:869405640215375972> Ping terminado.")
        embed = discord.Embed(
          title="🏓 Pong",
            description=(f'<a:dscrd_loading:866731675547336721> Ping: **{round(self.bot.latency * 1000)}ms**\n<a:clyde:846625894395412480> API: **{round((end_time - start_time) * 1000)}ms**\n<a:dscrd_typing:862837114240237599> Escribiendo: **{typingms}ms**'),
            color=0xfbf9fa
            #timestamp=datetime.utcnow()
        )
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/829223734559637545/859941157944557588/headAsset_214x-8.png?width=465&height=473")
        await ctx.send(embed=embed)
  
  @commands.command(name="git")
  async def git(self, ctx: commands.Context):
        """
        Código fuente de SatanyaBot
        """
        await ctx.send("Puedes revisar mi código fuente en https://github.com/KuroCat56/SatanyaBot")
  
  @commands.command(name="invite")
  async def invite(self, ctx: commands.Context):
      """
      Links de invitación de SatanyaBot y al server
      """
      embed = discord.Embed(
          title="¿Quieres agregarme a tu servidor o unirte al mío?",
          description="Aquí tienes los enlaces para unirte a mi servidor o invitarme al tuyo.",
          color=0xfbf9fa,
      )
      embed.add_field(
          name="<:join:847940361937879051> Link de server",
          value="[「SatanyaBot」](https://discord.gg/bqcdKxuW3X)",
          inline=True
      )
      embed.add_field(
          name="<:join:847940361937879051> Link SatanyaBot",
          value="[Invítame](https://discord.com/oauth2/authorize?client_id=805589802484760577&scope=bot&permissions=641723511)",
          inline=True
      )
      embed.set_image(url="https://media.discordapp.net/attachments/829223734559637545/859608410537459752/bannerSatanyaBot_Logotipo4x.png?width=1024&height=290"
      )
      await ctx.send("<:okay:846612389046386689> Te he enviado mis enlaces de invitación", delete_after = 10)
      await ctx.author.send(embed=embed)
  
  @commands.command(name="about")
  async def about(self, context):
        """
        Información útil (y no tan útil) del bot.
        """
        #Permite determinar el tiempo que lleva desde su primer proceso activo
        delta_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        uptime = (f"{days}d, {hours}h, {minutes}m, {seconds}s")
        
        block = "`"*3

        cpuUsage = psutil.cpu_percent(1)
        ramUsage = psutil.virtual_memory()[2]

        embed = discord.Embed(
        title="¡Hola, soy SatanyaBot!",
        description="🌸 SatanyaBot - la primer bot de Discord **open source y en español** desarrollada en Python.\n\nSatanyaBot nació con la idea de crear una alternativa de código abierto a los bots en español de Discord como Chocolat, Nekotina, Ruka y otros.\n\nRecuerda que si quieres ver mis comandos usa **nya>help**",
        color=0xfbf9fa,
        timestamp=datetime.utcnow()
        )
        embed.set_author(
        name=f"SatanyaBot | v{config.VERSION}",
        icon_url = "https://media.discordapp.net/attachments/829223734559637545/859941157944557588/headAsset_214x-8.png?width=465&height=473")
        
        embed.add_field(
        name="Noticias:",
        value=f"{block}fix\nPrueba los comandos de traducir, roll y 8ball ヽ(*・ω・)ﾉ\n{block}",
        inline=False
        )
        embed.add_field(
        name="Creador y Colaboradores:",
        value="[KuroCat#4816](https://linktr.ee/KuroCat56)",
        inline=False
        )
        embed.add_field(
        name="Mi versión de Python:",
        value=f"{platform.python_version()}",
        inline=True
        )
        embed.add_field(
        name="Encendida desde hace:",
        value=f"{uptime}",
        inline=True
        )
        embed.add_field(
        name="Uso de recursos:",
        value=f"{ramUsage} % RAM\n{cpuUsage}% CPU", #RAM
        inline=True
        )
        embed.add_field(
        name="Prefijo:",
        value=f"{config.PREFIX}",
        inline=True
        )
        embed.add_field(
        name= "# Comandos:",
        value=f"{len([x.name for x in self.bot.commands])}",
        inline=True
        )
        embed.add_field(
        name= "# Líneas:",
        value=f"{lines.get('lines'):,}", #Líneas escritas de todo el proyecto
        inline=True
        )
        embed.add_field(
        name= "# Servers:",
        value=f"{len(self.bot.guilds)}",
        inline=True
        )
        # statistics - Extraído de https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/stats.py#L216-L263
        total_members = 0
        #total_unique = len(self.bot.users)

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

        embed.add_field(name='# Miembros', value=f'{total_members} totales', inline=True)
        embed.add_field(name='# Canales', value=f'{text + voice} totales', inline=True)
        embed.add_field(
        name= "Cumpleaños 🍰",
        value="31/01/2021 | 09:50 AM",
        inline=False
        )
        embed.add_field(
        name= "Donaciones <a:cutestars:846625824538886214>",
        value="[Ko-fi](https://ko-fi.com/kurocat56)",
        inline=True
        ) 
        embed.add_field(
        name= "Top.gg <:wumpus_star:846611108784504872>",
        value="[Próximamente](https://top.gg/)",
        inline=True
        )
        embed.add_field(
        name="Enlaces",
        value="[Github](https://github.com/KuroCat56/SatanyaBot) **|** [Servidor de Soporte](https://discord.gg/bqcdKxuW3X) **|** [Invítame](https://discord.com/oauth2/authorize?client_id=805589802484760577&scope=bot&permissions=641723511)",
        inline=False
        )
        version = pkg_resources.get_distribution('discord.py').version
        embed.set_footer(
        text=f"Desarrollada en discord.py v{version}",
        icon_url='http://i.imgur.com/5BFecvA.png'
        )
        embed.set_image(url="https://media.discordapp.net/attachments/829223734559637545/859608410537459752/bannerSatanyaBot_Logotipo4x.png?width=1024&height=290"
        )
        await context.send(embed=embed)

  @commands.command(aliases=['si', 'server']) #Extraído de https://github.com/cree-py/RemixBot/blob/master/cogs/info.py
  async def serverinfo(self, ctx):
        '''Información básica del servidor.'''
        guild = ctx.guild
        guild_age = (ctx.message.created_at - guild.created_at).days
        created_at = f"Servidor creado {guild.created_at.strftime('%b %d %Y │ %H:%M')}.\n¡Eso fue hace {guild_age} días!"

        em = discord.Embed(description=created_at, color=0xfbf9fa)
        em.add_field(name='Owner', value=guild.owner, inline=False)
        em.add_field(name='Miembros', value=len(guild.members), inline=False)
        em.add_field(name='Roles', value=len(guild.roles))
        em.add_field(name='<:dscrd_channel:851449868722896936> Canales de texto', value=len(guild.text_channels))
        em.add_field(name='<:dscrd_voice:862873567204212776> Canales de voz', value=len(guild.voice_channels))


        em.set_thumbnail(url=None or guild.icon_url)
        em.set_author(name=guild.name, icon_url=None or guild.icon_url)
        await ctx.send(embed=em)

  @commands.command(name="opensource", aliases=["open"])
  async def opensource(self, ctx):
    embed = discord.Embed(
        title="SatanyaBot apoya el open source y tú también deberías",
        description="Soy una bot open source así que todo mi desarrollo está sostenido gracias al apoyo de otros desarrolladores y demás proyectos open source.\n\n<:satan_yeih:846553057999454219> Si deseas aportar ayuda y apoyo al proyecto revisa los siguientes enlaces: ",
        color=0xfbf9fa
      )
    embed.add_field(
        name="Desarrollo",
        value="[Github](https://github.com/KuroCat56/SatanyaBot) **|** [Servidor de Soporte](https://discord.gg/bqcdKxuW3X) **|** [Trello](https://trello.com/b/Z432JC83)",
        inline=False
        )
    embed.add_field(
        name="Donaciones <a:cutestars:846625824538886214>",
        value="[Ko-fi](https://ko-fi.com/kurocat56)",
        inline=False
        )
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/829223734559637545/859941157944557588/headAsset_214x-8.png?width=465&height=473")
    await ctx.send(embed=embed)

  @commands.command(aliases=["dn", "donation"])
  async def donate(self, ctx: commands.Context):
      """
      Links de invitación de SatanyaBot y al server
      """
      embed = discord.Embed(
          title="¿Te gustaría apoyar el desarrollo del proyecto?",
          description="Todo el dinero que se invierte va directamente para mantener el VPS donde SatanyaBot se mantiene activa. Aportando tan poco como $1 ayudas a mantener a flote el proyecto.",
          color=0xfbf9fa,
      )
      embed.add_field(
          name="<:join:847940361937879051> Enlaces de donaciones",
          value="[Ko-fi](https://ko-fi.com/kurocat56)",
          inline=True
      )
      embed.set_image(url="https://media.discordapp.net/attachments/829223734559637545/859608410537459752/bannerSatanyaBot_Logotipo4x.png?width=1024&height=290"
      )
      await ctx.send("<:okay:846612389046386689> Te he enviado mis enlaces de donación", delete_after = 10)
      await ctx.author.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(general(bot))