import datetime
from pathlib import WindowsPath
from discord.ext import commands
import discord
from asyncdagpi import Client, ImageFeatures
import os
from dotenv import load_dotenv
load_dotenv()

dagpi = Client(os.getenv('Dagpi'))

class img(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 10, commands.BucketType.user)}):
  """Modificadores de imágenes"""
  
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command(help ="Checa el perfil de un usuario.", aliases=["av"])
  async def avatar(self, ctx, member: discord.Member=None):
    if member is None:
      member = ctx.author
    avatar= str(member.avatar_url_as(static_format="png", size=1024))
    embed = discord.Embed(
      title= f"Foto de perfil de {member}",
      color=ctx.author.color
    )
    embed.set_image(url=avatar)
    embed.set_footer(text=f"Solicitado por {ctx.message.author}")
    await ctx.reply(embed=embed, mention_author=False)

  @commands.command()
  async def pixel(self, ctx, member: discord.Member=None):
    """
    Censura el perfil de otro, porque sí.
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_pxl = str(member.avatar_url_as(static_format="png", size=1024))
      img_pxl = await dagpi.image_process(ImageFeatures.pixel(), url_pxl)
      file_pxl = discord.File(fp=img_pxl.image,filename=f"pixel.{img_pxl.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://pixel.{img_pxl.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_pxl, embed=embed, mention_author=False)

  @commands.command()
  async def pet(self, ctx, member: discord.Member=None):
    """
    Hazle un patpat a un miembro.
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_ptpt = str(member.avatar_url_as(static_format="png", size=1024))
      img_ptpt = await dagpi.image_process(ImageFeatures.petpet(), url_ptpt)
      file_ptpt = discord.File(fp=img_ptpt.image,filename=f"pet.{img_ptpt.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://pet.{img_ptpt.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_ptpt, embed=embed, mention_author=False)

  
  @commands.command(aliases=["trigger"])
  async def triggered(self, ctx, member: discord.Member=None):
    """
    T R I G G E R E D
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_trgg = str(member.avatar_url_as(static_format="png", size=1024))
      img_trgg = await dagpi.image_process(ImageFeatures.triggered(), url_trgg)
      file_trgg = discord.File(fp=img_trgg.image,filename=f"triggered.{img_trgg.format}")
      
      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://triggered.{img_trgg.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_trgg, embed=embed, mention_author=False)

  @commands.command()
  async def urss(self, ctx, member: discord.Member=None):
    """
    URSS
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_urss = str(member.avatar_url_as(static_format="png", size=1024))
      img_urss = await dagpi.image_process(ImageFeatures.communism(), url_urss)
      file_urss = discord.File(fp=img_urss.image,filename=f"urss.{img_urss.format}")
      
      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://urss.{img_urss.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_urss, embed=embed, mention_author=False)

  @commands.command()
  async def colors(self, ctx, member: discord.Member=None):
    """
    Analiza los colores de la foto de perfil de alguien.
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_clrs = str(member.avatar_url_as(static_format="png", size=1024))
      img_clrs = await dagpi.image_process(ImageFeatures.colors(), url_clrs)
      file_clrs = discord.File(fp=img_clrs.image,filename=f"colors.{img_clrs.format}")
      
      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://colors.{img_clrs.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_clrs, embed=embed, mention_author=False)

  @commands.command()
  async def gay(self, ctx, member: discord.Member=None):
    """
    #Pride
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_gy = str(member.avatar_url_as(static_format="png", size=1024))
      img_gy = await dagpi.image_process(ImageFeatures.gay(), url_gy)
      file_gy = discord.File(fp=img_gy.image,filename=f"gay.{img_gy.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://gay.{img_gy.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_gy, embed=embed, mention_author=False)

  @commands.command()
  async def fedora(self, ctx, member: discord.Member=None):
    """
    Ma'lady
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_fdr = str(member.avatar_url_as(static_format="png", size=1024))
      img_fdr = await dagpi.image_process(ImageFeatures.fedora(), url_fdr)
      file_fdr = discord.File(fp=img_fdr.image,filename=f"fedora.{img_fdr.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://fedora.{img_fdr.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_fdr, embed=embed, mention_author=False)

  @commands.command()
  async def jail(self, ctx, member: discord.Member=None):
    """
    Para mandar a cualquiera a la carcel
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_jl = str(member.avatar_url_as(static_format="png", size=1024))
      img_jl = await dagpi.image_process(ImageFeatures.jail(), url_jl)
      file_jl = discord.File(fp=img_jl.image,filename=f"jail.{img_jl.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://jail.{img_jl.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_jl, embed=embed, mention_author=False)

  @commands.command()
  async def bonk(self, ctx, member: discord.Member=None):
    """
    ¿Alguien anda horny?
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_bnk= str(member.avatar_url_as(static_format="png", size=1024))
      img_bnk = await dagpi.image_process(ImageFeatures.bonk(), url_bnk)
      file_bnk = discord.File(fp=img_bnk.image,filename=f"bonk.{img_bnk.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://bonk.{img_bnk.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_bnk, embed=embed, mention_author=False)

  @commands.command()
  async def delete(self, ctx, member: discord.Member=None):
    """
    Borra a alguien de la existencia
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_dlt= str(member.avatar_url_as(static_format="png", size=1024))
      img_dlt = await dagpi.image_process(ImageFeatures.delete(), url_dlt)
      file_dlt = discord.File(fp=img_dlt.image,filename=f"delete.{img_dlt.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://delete.{img_dlt.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_dlt, embed=embed, mention_author=False)

  @commands.command()
  async def kaboom(self, ctx, member: discord.Member=None):
    """
    KABOOM!
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_bmb= str(member.avatar_url_as(static_format="png", size=1024))
      img_bmb = await dagpi.image_process(ImageFeatures.bomb(), url_bmb)
      file_bmb = discord.File(fp=img_bmb.image,filename=f"bomb.{img_bmb.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://bomb.{img_bmb.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_bmb, embed=embed, mention_author=False)

  @commands.command()
  async def neon(self, ctx, member: discord.Member=None):
    """
    Porque todo es más bonito con el neón
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_nn= str(member.avatar_url_as(static_format="png", size=1024))
      img_nn = await dagpi.image_process(ImageFeatures.neon(), url_nn)
      file_nn = discord.File(fp=img_nn.image,filename=f"neon.{img_nn.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://neon.{img_nn.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_nn, embed=embed, mention_author=False)

  @commands.command()
  async def wanted(self, ctx, member: discord.Member=None):
    """
    El más buscado por la ley
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_wntd = str(member.avatar_url_as(static_format="png", size=1024))
      img_wntd = await dagpi.image_process(ImageFeatures.wanted(), url_wntd)
      file_wtnd = discord.File(fp=img_wntd.image,filename=f"wanted.{img_wntd.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://wanted.{img_wntd.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_wtnd, embed=embed, mention_author=False)

  @commands.command()
  async def wasted(self, ctx, member: discord.Member=None):
    """
    RIP
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_wstd = str(member.avatar_url_as(static_format="png", size=1024))
      img_wstd = await dagpi.image_process(ImageFeatures.wasted(), url_wstd)
      file_wstd = discord.File(fp=img_wstd.image,filename=f"wasted.{img_wstd.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://wasted.{img_wstd.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_wstd, embed=embed, mention_author=False)

def setup(bot: commands.Bot):
    bot.add_cog(img(bot))
