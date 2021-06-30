import discord, platform
import config
from discord.ext import commands
from datetime import datetime
from psutil import Process
from os import getpid

class general(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 10, commands.BucketType.user)}):

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  #Comando de test/ping
  @commands.command(name="ping")
  async def ping(self, ctx: commands.Context):
        """
        ¡Pong!
        """
        embed = discord.Embed(
          title="🏓 Pong",
            description=(f'📨 Envío de mensajes: **{round(self.bot.latency * 1000)}ms**'),
            color=0xfbf9fa,
            timestamp=datetime.utcnow()
        )
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
          description="Enlaces útiles de invitación",
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
      embed.add_field(
          name="<a:cutestars:846625824538886214> Donaciones",
          value="[Ko-fi](https://ko-fi.com/kurocat56)",
          inline=False
      )
      embed.add_field(
          name="<:wumpus_star:846611108784504872> Califícame en top.gg",
          value="[Próximamente](https://top.gg/)",
          inline=False
      )
      embed.set_image(url="https://media.discordapp.net/attachments/829223734559637545/859608410537459752/bannerSatanyaBot_Logotipo4x.png?width=1024&height=290"
      )
      await ctx.send("Te he enviado mis enlaces de invitación <:SatanyaBot:858480664143331338>")
      await ctx.author.send(embed=embed)
  
  @commands.command(name="info", aliases=["botinfo"])
  async def info(self, context):
        """
        Información útil (y no tan útil) del bot.
        """
        #Implementación directa de main.py
        delta_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        uptime = (f"{days}d, {hours}h, {minutes}m, {seconds}s")

        embed = discord.Embed(
          title="¡Hola, soy SatanyaBot!",
            description="Gracias por dejarme estar en tu servidor. Recuerda que si quieres ver mis comandos usa **nya>help**",
            color=0xfbf9fa,
            timestamp=datetime.utcnow()
        )
        embed.set_author(
            name=f"SatanyaBot | v{config.VERSION}",
            icon_url = "https://media.discordapp.net/attachments/829223734559637545/829344812913655878/SatanyaBot.png?width=431&height=473"
        )
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/819972811799265315/822718490300514314/SatanyaBotspam.png?width=431&height=473"
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
            name="Uso de memoria actual:",
            value=f"{round(Process(getpid()).memory_info().rss/1024/1024, 2)} MB",
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
          name= "# Servers:",
          value=f"{len(self.bot.guilds)}",
          inline=True
        )
        embed.add_field(
          name= "Cumpleaños 🍰",
          value="31/01/2021 | 09:50 AM",
          inline=False
        )
        embed.add_field(
          name= "Donaciones 🤍",
          value="[Ko-fi](https://ko-fi.com/kurocat56)",
          inline=True
        ) 
        embed.add_field(
          name= "Top.gg",
          value="[Próximamente](https://top.gg/)",
          inline=True
        )
        embed.add_field(
            name="Enlaces",
            value="[Github](https://github.com/KuroCat56/SatanyaBot) | [Servidor de Soporte](https://discord.gg/bqcdKxuW3X) | [Invítame](https://discord.com/oauth2/authorize?client_id=805589802484760577&scope=bot&permissions=641723511)",
            inline=False
        )
        embed.set_footer(
            text=f"Solicitado por {context.message.author}"
        )
        embed.set_image(url="https://media.discordapp.net/attachments/829223734559637545/859608410537459752/bannerSatanyaBot_Logotipo4x.png?width=1024&height=290"
        )
        await context.send(embed=embed)

  @commands.command(name="server")
  async def server(self, context):
        """
        Información útil (y no tan útil) del servidor.
        """
        server = context.message.guild
        roles = [x.name for x in server.roles]
        role_length = len(roles)
        if role_length > 50:
            roles = roles[:50]
            roles.append(f">>>> Desplegando[50/{len(roles)}] Roles")
        roles = ", ".join(roles)
        channels = len(server.channels)
        time = str(server.created_at)
        time = time.split(" ")
        time = time[0]

        embed = discord.Embed(
            title="**Servidor:**",
            description=f"{server}",
            color=0xfbf9fa
        )
        embed.set_thumbnail(
            url=server.icon_url
        )
        embed.add_field(
            name="Propietario",
            value=f"{server.owner}"
        )
        embed.add_field(
            name="Server ID",
            value=server.id
        )
        embed.add_field(
            name="Miembros",
            value=server.member_count
        )
        embed.add_field(
            name="Canales texto/voz",
            value=f"{channels}"
        )
        embed.add_field(
            name=f"Roles ({role_length})",
            value=roles
        )
        embed.set_footer(
            text=f"Creado el {time}"
        )
        await context.send(embed=embed)

  @commands.command(name="apis")
  async def apis(self, ctx):

    await ctx.send("Soy una bot de código abierto")

def setup(bot: commands.Bot):
    bot.add_cog(general(bot))