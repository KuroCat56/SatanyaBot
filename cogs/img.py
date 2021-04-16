from discord.ext import commands
import discord
from asyncdagpi import Client, ImageFeatures
import os

dagpi = Client(os.getenv('Dagpi'))

class img(commands.Cog):
  """Modificadores de imágenes"""
  
  def __init__(self, bot: commands.Bot):
    self.bot = bot

    @bot.command()
    async def pixel(ctx, member: discord.Member):
      url = str(member.avatar_url_as(static_format="png", size=1024))
      img = await dagpi.image_process(ImageFeatures.pixel(), url)
      file = discord.File(fp=img.image,filename=f"pixel.{img.format}")
      await ctx.send(file=file)


def setup(bot: commands.Bot):
    bot.add_cog(img(bot))