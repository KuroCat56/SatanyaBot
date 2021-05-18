import discord, platform
import config
from discord.ext import commands
from datetime import datetime

class general(commands.Cog):

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
          name="Link de server:",
          value="[「SatanyaBot」](https://discord.gg/bqcdKxuW3X)",
          inline=False
      )
      embed.add_field(
          name="Link SatanyaBot:",
          value="[Invítame](https://discord.com/oauth2/authorize?client_id=805589802484760577&scope=bot&permissions=641723511)",
          inline=False
      )
      embed.set_image(url="https://media.discordapp.net/attachments/829223734559637545/832458242806120499/bannerSatanyaBot_Logotipo3x.png?width=1024&height=291"
      )
      await ctx.send("Te he enviado mis enlaces de invitación <:SatanyaBot:832392370472484875>")
      await ctx.author.send(embed=embed)
  
  @commands.command(name="info", aliases=["botinfo"])
  async def info(self, context):
        """
        Información útil (y no tan útil) del bot.
        """
        embed = discord.Embed(
          title="¡Hola, soy SatanyaBot!",
            description="Gracias por dejarme estar en tu servidor. Recuerda que si quieres ver mis comandos usa **nya>help**",
            color=0xfbf9fa,
            timestamp=datetime.utcnow()
        )
        embed.set_author(
            name=f"SatanyaBot | v{config.VERSION}",
            icon_url = "https://media.discordapp.net/attachments/819972811799265315/822706553815171142/Nya-Dark.png?width=472&height=472"
        )
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/819972811799265315/822718490300514314/SatanyaBotspam.png?width=431&height=473"
        )
        embed.add_field(
            name="Creador y Colaboradores:",
            value="KuroCat#4816",
            inline=False
        )
        embed.add_field(
            name="Mi versión de Python:",
            value=f"{platform.python_version()}",
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
            name="Mi código fuente:",
            value="[Github](https://github.com/KuroCat56/SatanyaBot)",
            inline=True
        )
        embed.set_footer(
            text=f"Solicitado por {context.message.author}"
        )
        embed.set_image(url="https://media.discordapp.net/attachments/829223734559637545/832458242806120499/bannerSatanyaBot_Logotipo3x.png?width=1024&height=291"
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

def setup(bot: commands.Bot):
    bot.add_cog(general(bot))