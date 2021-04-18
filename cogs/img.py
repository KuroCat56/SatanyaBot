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
      url_pxl = str(member.avatar_url_as(static_format="png", size=1024))
      img_pxl = await dagpi.image_process(ImageFeatures.pixel(), url_pxl)
      file_pxl = discord.File(fp=img_pxl.image,filename=f"pixel.{img_pxl.format}")
      await ctx.send(file=file_pxl)

    @bot.command()
    async def pet(ctx, member: discord.Member):
      url_ptpt = str(member.avatar_url_as(static_format="png", size=1024))
      img_ptpt = await dagpi.image_process(ImageFeatures.petpet(), url_ptpt)
      file_ptpt = discord.File(fp=img_ptpt.image,filename=f"pet.{img_ptpt.format}")
      await ctx.send(file=file_ptpt)
    
    @bot.command()
    async def rainbow(ctx, member: discord.Member):
      url_rnbw = str(member.avatar_url_as(static_format="png", size=1024))
      img_rnbw = await dagpi.image_process(ImageFeatures.rainbow(), url_rnbw)
      file_rnbw = discord.File(fp=img_rnbw.image,filename=f"rainbow.{img_rnbw.format}")
      await ctx.send(file=file_rnbw)

def setup(bot: commands.Bot):
    bot.add_cog(img(bot))