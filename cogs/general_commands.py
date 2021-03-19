import discord, platform
import config
from discord.ext import commands

class general(commands.Cog):

  def __init__(self, client: commands.Bot):
    self.client = client

  #Comando de test/ping
  @commands.command(name="ping")
  async def ping(self, ctx: commands.Context):
        """
        ¡Pong!
        """
        await ctx.send(f'Pong {round(self.client.latency * 1000)}ms')
  
  @commands.command(name="info", aliases=["botinfo"])
  async def info(self, context):
        """
        Información útil (y no tan útil) del bot.
        """
        embed = discord.Embed(
            description=f"SatanyaBot v{config.VERSION}",
            color=0xffffff
        )
        embed.set_author(
            name="Información del bot"
        )
        embed.add_field(
            name="Creador:",
            value="KuroCat#4816",
            inline=True
        )
        embed.add_field(
            name="Python Version:",
            value=f"{platform.python_version()}",
            inline=True
        )
        embed.add_field(
            name="Prefijo:",
            value=f"{config.PREFIX}",
            inline=False
        )
        embed.set_footer(
            text=f"Solicitado por {context.message.author}"
        )
        await context.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(general(client))