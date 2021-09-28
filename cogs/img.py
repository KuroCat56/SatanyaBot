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
  """
  Filtros y modificadores divertidos de imágenes. ¡Descubre cada uno de ellos!
  Etiqueta a otro usuario para aplicarle el filtro a su perfil.
  
  Si algún comando no funciona con tu perfil es posible que la imagen sea demasiado grande como para enviarse.

  Cooldown: 10s per command
  """
  
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

  # @commands.command(aliases=["trigger"])
  # async def triggered(self, ctx, member: discord.Member=None):
  #   """
  #   T R I G G E R E D
  #   """
  #   if member is None:
  #     member = ctx.author
  #   async with ctx.typing():
  #     url_trgg = str(member.avatar_url_as(static_format="png", size=1024))
  #     img_trgg = await dagpi.image_process(ImageFeatures.triggered(), url_trgg)
  #     file_trgg = discord.File(fp=img_trgg.image,filename=f"triggered.{img_trgg.format}")
      
  #     embed = discord.Embed(color=ctx.author.color)
  #     embed.set_image(url=f"attachment://triggered.{img_trgg.format}")
  #     embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
  #     await ctx.reply(file=file_trgg, embed=embed, mention_author=False)

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

  @commands.command()
  async def america(self, ctx, member: discord.Member=None):
    """
    Capitalismo FTW
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_mrc = str(member.avatar_url_as(static_format="png", size=1024))
      img_mrc = await dagpi.image_process(ImageFeatures.america(), url_mrc)
      file_mrc = discord.File(fp=img_mrc.image,filename=f"america.{img_mrc.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://america.{img_mrc.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_mrc, embed=embed, mention_author=False)

  @commands.command()
  async def invert(self, ctx, member: discord.Member=None):
    """
    Pásale un filtro invertido a esa imagen de perfil
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_nvrt = str(member.avatar_url_as(static_format="png", size=1024))
      img_nvrt = await dagpi.image_process(ImageFeatures.invert(), url_nvrt)
      file_nvrt = discord.File(fp=img_nvrt.image,filename=f"invert.{img_nvrt.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://invert.{img_nvrt.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_nvrt, embed=embed, mention_author=False)

  @commands.command()
  async def sobel(self, ctx, member: discord.Member=None):
    """
    Detectando bordes desde 1968
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_sbl = str(member.avatar_url_as(static_format="png", size=1024))
      img_sbl = await dagpi.image_process(ImageFeatures.sobel(), url_sbl)
      file_sbl = discord.File(fp=img_sbl.image,filename=f"sobel.{img_sbl.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://sobel.{img_sbl.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_sbl, embed=embed, mention_author=False)

  @commands.command()
  async def blur(self, ctx, member: discord.Member=None):
    """
    A veces hay que censurar, por si acaso
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_blr = str(member.avatar_url_as(static_format="png", size=1024))
      img_blr = await dagpi.image_process(ImageFeatures.blur(), url_blr)
      file_blr = discord.File(fp=img_blr.image,filename=f"blur.{img_blr.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://blur.{img_blr.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_blr, embed=embed, mention_author=False)

  @commands.command()
  async def rgb(self, ctx, member: discord.Member=None):
    """
    Extrae la información RGB de un perfil
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_rgb = str(member.avatar_url_as(static_format="png", size=1024))
      img_rgb = await dagpi.image_process(ImageFeatures.rgb(), url_rgb)
      file_rgb = discord.File(fp=img_rgb.image,filename=f"rgb.{img_rgb.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://rgb.{img_rgb.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_rgb, embed=embed, mention_author=False)

  @commands.command()
  async def deepfry(self, ctx, member: discord.Member=None):
    """
    ¿Te gustan las papas fritas?
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_dpfr = str(member.avatar_url_as(static_format="png", size=1024))
      img_dpfr = await dagpi.image_process(ImageFeatures.deepfry(), url_dpfr)
      file_dpfr = discord.File(fp=img_dpfr.image,filename=f"deepfry.{img_dpfr.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://deepfry.{img_dpfr.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_dpfr, embed=embed, mention_author=False)

  @commands.command()
  async def ascii(self, ctx, member: discord.Member=None):
    """
    A S C I I
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_sc = str(member.avatar_url_as(static_format="png", size=1024))
      img_sc = await dagpi.image_process(ImageFeatures.ascii(), url_sc)
      file_sc = discord.File(fp=img_sc.image,filename=f"ascii.{img_sc.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://ascii.{img_sc.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_sc, embed=embed, mention_author=False)

  @commands.command()
  async def sepia(self, ctx, member: discord.Member=None):
    """
    El típico y ya conocido filtro sepia
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_sp = str(member.avatar_url_as(static_format="png", size=1024))
      img_sp = await dagpi.image_process(ImageFeatures.sepia(), url_sp)
      file_sp = discord.File(fp=img_sp.image,filename=f"sepia.{img_sp.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://sepia.{img_sp.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_sp, embed=embed, mention_author=False)

  # @commands.command()
  # async def glitch(self, ctx, member: discord.Member=None):
  #   """
  #   Cool glitch B)
  #   """
  #   if member is None:
  #     member = ctx.author
  #   async with ctx.typing():
  #     url_gltch = str(member.avatar_url_as(static_format="png", size=1024))
  #     img_gltch = await dagpi.image_process(ImageFeatures.glitch(), url_gltch)
  #     file_gltch = discord.File(fp=img_gltch.image,filename=f"glitch.{img_gltch.format}")

  #     embed = discord.Embed(color=ctx.author.color)
  #     embed.set_image(url=f"attachment://glitch.{img_gltch.format}")
  #     embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
  #     await ctx.reply(file=file_gltch, embed=embed, mention_author=False)

  @commands.command()
  async def polaroid(self, ctx, member: discord.Member=None):
    """
    Imprime esa imagen de perfil en una fotografía
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_plrd = str(member.avatar_url_as(static_format="png", size=1024))
      img_plrd = await dagpi.image_process(ImageFeatures.polaroid(), url_plrd)
      file_plrd = discord.File(fp=img_plrd.image,filename=f"polaroid.{img_plrd.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://polaroid.{img_plrd.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_plrd, embed=embed, mention_author=False)

  @commands.command()
  async def swirl(self, ctx, member: discord.Member=None):
    """
    Vamos a deformar un poco
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_swrl = str(member.avatar_url_as(static_format="png", size=1024))
      img_swrl = await dagpi.image_process(ImageFeatures.swirl(), url_swrl)
      file_swrl = discord.File(fp=img_swrl.image,filename=f"swirl.{img_swrl.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://swirl.{img_swrl.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_swrl, embed=embed, mention_author=False)

  @commands.command()
  async def paint(self, ctx, member: discord.Member=None):
    """
    El arte es subjetivo
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_pnt = str(member.avatar_url_as(static_format="png", size=1024))
      img_pnt = await dagpi.image_process(ImageFeatures.paint(), url_pnt)
      file_pnt = discord.File(fp=img_pnt.image,filename=f"paint.{img_pnt.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://paint.{img_pnt.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_pnt, embed=embed, mention_author=False)

  @commands.command()
  async def sketch(self, ctx, member: discord.Member=None):
    """
    ¿Cómo sería si te dibujase un artista?
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_sktch = str(member.avatar_url_as(static_format="png", size=1024))
      img_sktch = await dagpi.image_process(ImageFeatures.sketch(), url_sktch)
      file_sktch = discord.File(fp=img_sktch.image,filename=f"sketch.{img_sktch.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://sketch.{img_sktch.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_sktch, embed=embed, mention_author=False)

  @commands.command()
  async def spin(self, ctx, member: discord.Member=None):
    """
    You spin me right round, baby
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_spn = str(member.avatar_url_as(static_format="png", size=1024))
      img_spn = await dagpi.image_process(ImageFeatures.spin(), url_spn)
      file_spn = discord.File(fp=img_spn.image,filename=f"spin.{img_spn.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://spin.{img_spn.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_spn, embed=embed, mention_author=False)

  # @commands.command(aliases=["snap"])
  # async def dissolve(self, ctx, member: discord.Member=None):
  #   """
  #   Thanos snap
  #   """
  #   if member is None:
  #     member = ctx.author
  #   async with ctx.typing():
  #     url_dsslv = str(member.avatar_url_as(static_format="png", size=1024))
  #     img_dsslv = await dagpi.image_process(ImageFeatures.dissolve(), url_dsslv)
  #     file_dsslv = discord.File(fp=img_dsslv.image,filename=f"dissolve.{img_dsslv.format}")

  #     embed = discord.Embed(color=ctx.author.color)
  #     embed.set_image(url=f"attachment://dissolve.{img_dsslv.format}")
  #     embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
  #     await ctx.reply(file=file_dsslv, embed=embed, mention_author=False)

  @commands.command()
  async def magik(self, ctx, member: discord.Member=None):
    """
    Usa este con cuidado
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_mgk = str(member.avatar_url_as(static_format="png", size=1024))
      img_mgk = await dagpi.image_process(ImageFeatures.magik(), url_mgk)
      file_mgk = discord.File(fp=img_mgk.image,filename=f"magik.{img_mgk.format}")

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"attachment://magik.{img_mgk.format}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar_url)
      await ctx.reply(file=file_mgk, embed=embed, mention_author=False)

  @commands.command()
  async def hearts(self, ctx, member: discord.Member=None):
    """
    <3
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_hrts = str(member.avatar_url_as(static_format="png", size=1024))

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"https://api.devs-hub.xyz/hearts?image={url_hrts}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ api.devs-hub.xyz", icon_url=member.avatar_url)
      await ctx.reply(embed=embed, mention_author=False)

  @commands.command()
  async def simp(self, ctx, member: discord.Member=None):
    """
    Certified simp moment
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_smp = str(member.avatar_url_as(static_format="png", size=1024))

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"https://api.devs-hub.xyz/simp?image={url_smp}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ api.devs-hub.xyz", icon_url=member.avatar_url)
      await ctx.reply(embed=embed, mention_author=False)

  @commands.command()
  async def simp(self, ctx, member: discord.Member=None):
    """
    Certified simp moment
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_smp = str(member.avatar_url_as(static_format="png", size=1024))

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"https://api.devs-hub.xyz/simp?image={url_smp}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ api.devs-hub.xyz", icon_url=member.avatar_url)
      await ctx.reply(embed=embed, mention_author=False)

  @commands.command()
  async def like(self, ctx, member: discord.Member=None):
    """
    [Everyone liked that]
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_lk = str(member.avatar_url_as(static_format="png", size=1024))

      embed = discord.Embed(color=ctx.author.color)
      embed.set_image(url=f"https://api.devs-hub.xyz/like?image={url_lk}")
      embed.set_footer(text=f"Solicitado por {ctx.message.author} │ api.devs-hub.xyz", icon_url=member.avatar_url)
      await ctx.reply(embed=embed, mention_author=False)


def setup(bot: commands.Bot):
    bot.add_cog(img(bot))
