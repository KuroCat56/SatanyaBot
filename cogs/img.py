from discord.ext import commands
import discord
from asyncdagpi import Client, ImageFeatures
import os
from dotenv import load_dotenv
load_dotenv()

dagpi = Client(os.getenv('Dagpi'))

class img(commands.Cog):
  """Modificadores de imágenes"""
  
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command()
  async def pixel(self, ctx, member: discord.Member):
    """
    Censura el perfil de otro, porque sí.
    """
    async with ctx.typing():
      url_pxl = str(member.avatar_url_as(static_format="png", size=1024))
      img_pxl = await dagpi.image_process(ImageFeatures.pixel(), url_pxl)
      file_pxl = discord.File(fp=img_pxl.image,filename=f"pixel.{img_pxl.format}")
      await ctx.send(file=file_pxl)

  @commands.command()
  async def pet(self, ctx, member: discord.Member):
    """
    Hazle un patpat a un miembro.
    """
    async with ctx.typing():
      url_ptpt = str(member.avatar_url_as(static_format="png", size=1024))
      img_ptpt = await dagpi.image_process(ImageFeatures.petpet(), url_ptpt)
      file_ptpt = discord.File(fp=img_ptpt.image,filename=f"pet.{img_ptpt.format}")
      await ctx.send(file=file_ptpt)
  
  @commands.command()
  async def triggered(self, ctx, member: discord.Member):
    """
    T R I G G E R E D
    """
    async with ctx.typing():
      url_trgg = str(member.avatar_url_as(static_format="png", size=1024))
      img_trgg = await dagpi.image_process(ImageFeatures.triggered(), url_trgg)
      file_trgg = discord.File(fp=img_trgg.image,filename=f"triggered.{img_trgg.format}")
      await ctx.send(file=file_trgg)

  # @commands.command()
  # async def ussr(self, ctx, member: discord.Member):
  #   """
  #   USSR
  #   """
  #   async with ctx.typing():
  #     url_ussr = str(member.avatar_url_as(static_format="png", size=1024))
  #     img_ussr = await dagpi.image_process(ImageFeatures.communism(), url_ussr)
  #     file_ussr = discord.File(fp=img_ussr.image,filename=f"ussr.{img_ussr.format}")
  #     await ctx.send(file=file_ussr)

  @commands.command()
  async def colors(self, ctx, member: discord.Member):
    """
    Analiza los colores de la foto de perfil de alguien.
    """
    async with ctx.typing():
      url_clrs = str(member.avatar_url_as(static_format="png", size=1024))
      img_clrs = await dagpi.image_process(ImageFeatures.colors(), url_clrs)
      file_clrs = discord.File(fp=img_clrs.image,filename=f"colors.{img_clrs.format}")
      await ctx.send(file=file_clrs)

  @commands.command()
  async def gay(self, ctx, member: discord.Member):
    """
    #Pride
    """
    async with ctx.typing():
      url_gy = str(member.avatar_url_as(static_format="png", size=1024))
      img_gy = await dagpi.image_process(ImageFeatures.gay(), url_gy)
      file_gy = discord.File(fp=img_gy.image,filename=f"gay.{img_gy.format}")
      await ctx.send(file=file_gy)

  @commands.command()
  async def fedora(self, ctx, member: discord.Member):
    """
    Ma'lady
    """
    async with ctx.typing():
      url_fdr = str(member.avatar_url_as(static_format="png", size=1024))
      img_fdr = await dagpi.image_process(ImageFeatures.fedora(), url_fdr)
      file_fdr = discord.File(fp=img_fdr.image,filename=f"fedora.{img_fdr.format}")
      await ctx.send(file=file_fdr)

  @commands.command()
  async def jail(self, ctx, member: discord.Member):
    """
    Para mandar a cualquiera a la carcel
    """
    async with ctx.typing():
      url_jl = str(member.avatar_url_as(static_format="png", size=1024))
      img_jl = await dagpi.image_process(ImageFeatures.jail(), url_jl)
      file_jl = discord.File(fp=img_jl.image,filename=f"jail.{img_jl.format}")
      await ctx.send(file=file_jl)

  @commands.command()
  async def bonk(self, ctx, member: discord.Member):
    """
    ¿Alguien anda horny?
    """
    async with ctx.typing():
      url_bnk= str(member.avatar_url_as(static_format="png", size=1024))
      img_bnk = await dagpi.image_process(ImageFeatures.bonk(), url_bnk)
      file_bnk = discord.File(fp=img_bnk.image,filename=f"bonk.{img_bnk.format}")
      await ctx.send(file=file_bnk)

  @commands.command()
  async def test(self, ctx, member: discord.Member):
    """
    Test
    """
    async with ctx.typing():
      url_test= str(member.avatar_url_as(static_format="png", size=1024))
      img_test = await dagpi.image_process(ImageFeatures.bomb(), url_test)
      file_test = discord.File(fp=img_test.image,filename=f"test.{img_test.format}")
      await ctx.send(file=file_test)

def setup(bot: commands.Bot):
    bot.add_cog(img(bot))
