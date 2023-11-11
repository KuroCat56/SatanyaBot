import os
from typing import Union
import discord
from asyncdagpi import Client, ImageFeatures
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

dagpi = Client(os.environ['DAGPI'])


class Image(
    commands.Cog,
    group_name="img",
    command_attrs={
        'cooldown': commands.CooldownMapping.from_cooldown(
            1, 10, commands.BucketType.user
        )
    },
):
    """
    Filtros y modificadores divertidos de imágenes. ¡Descubre cada uno de ellos!
    Etiqueta a otro usuario para aplicarle el filtro a su perfil.

    Si algún comando no funciona con tu perfil es posible que la imagen sea demasiado grande como para enviarse.

    Cooldown: 10s per command
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(description='Checa el perfil de un usuario.', aliases=['av'])
    async def avatar(
            self, ctx, member: Union[discord.Member, discord.User] = None
    ):
        if not member or member == ctx.author:
            member = ctx.author
        avatar = str(member.avatar.replace(static_format='png', size=1024))
        embed = discord.Embed(
            title=f'Foto de perfil de {member.display_name}',
            color=ctx.author.color,
        )
        embed.set_image(url=avatar)
        embed.set_footer(text=f'Solicitado por {ctx.message.author}')
        await ctx.reply(embed=embed)

    @commands.hybrid_command(description="Censura el perfil de otro, porque sí.")
    async def pixel(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_pxl = await dagpi.image_process(
                ImageFeatures.pixel(), member.avatar.url
            )
            file_pxl = discord.File(
                fp=img_pxl.image, filename=f'pixel.{img_pxl.format}'
            )
            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://pixel.{img_pxl.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_pxl, embed=embed)

    @commands.hybrid_command(description="Hazle un patpat a un miembro.")
    async def pet(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_ptpt = await dagpi.image_process(
                ImageFeatures.petpet(), member.avatar.url
            )
            file_ptpt = discord.File(
                fp=img_ptpt.image, filename=f'pet.{img_ptpt.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://pet.{img_ptpt.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_ptpt, embed=embed)

    @commands.command(aliases=['trigger'], description="T R I G G E R E D")
    async def triggered(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_trgg = await dagpi.image_process(
                ImageFeatures.triggered(), member.avatar.url
            )
            file_trgg = discord.File(
                fp=img_trgg.image, filename=f'triggered.{img_trgg.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://triggered.{img_trgg.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_trgg, embed=embed)

    @commands.hybrid_command(description="URSS")
    async def urss(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_urss = await dagpi.image_process(
                ImageFeatures.communism(), member.avatar.url
            )
            file_urss = discord.File(
                fp=img_urss.image, filename=f'urss.{img_urss.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://urss.{img_urss.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_urss, embed=embed)

    @commands.command(description="Analiza los colores de la foto de perfil de alguien.")
    async def colors(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_clrs = await dagpi.image_process(
                ImageFeatures.colors(), member.avatar.url
            )
            file_clrs = discord.File(
                fp=img_clrs.image, filename=f'colors.{img_clrs.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://colors.{img_clrs.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_clrs, embed=embed)

    @commands.hybrid_command(description="#Pride")
    async def gay(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_gy = await dagpi.image_process(
                ImageFeatures.gay(), member.avatar.url
            )
            file_gy = discord.File(
                fp=img_gy.image, filename=f'gay.{img_gy.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://gay.{img_gy.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_gy, embed=embed)

    @commands.hybrid_command(description="Ma'lady")
    async def fedora(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_fdr = await dagpi.image_process(
                ImageFeatures.fedora(), member.avatar.url
            )
            file_fdr = discord.File(
                fp=img_fdr.image, filename=f'fedora.{img_fdr.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://fedora.{img_fdr.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_fdr, embed=embed)

    @commands.hybrid_command(description="Para mandar a cualquiera a la carcel")
    async def jail(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_jl = await dagpi.image_process(
                ImageFeatures.jail(), member.avatar.url
            )
            file_jl = discord.File(
                fp=img_jl.image, filename=f'jail.{img_jl.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://jail.{img_jl.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_jl, embed=embed)

    @commands.hybrid_command(description="¿Alguien anda horny?")
    async def bonk(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_bnk = await dagpi.image_process(
                ImageFeatures.bonk(), member.avatar.url
            )
            file_bnk = discord.File(
                fp=img_bnk.image, filename=f'bonk.{img_bnk.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://bonk.{img_bnk.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_bnk, embed=embed)

    @commands.hybrid_command(description="Borra a alguien de la existencia")
    async def delete(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_dlt = await dagpi.image_process(
                ImageFeatures.delete(), member.avatar.url
            )
            file_dlt = discord.File(
                fp=img_dlt.image, filename=f'delete.{img_dlt.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://delete.{img_dlt.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_dlt, embed=embed)

    @commands.hybrid_command(description="KABOOM!")
    async def kaboom(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_bmb = await dagpi.image_process(
                ImageFeatures.bomb(), member.avatar.url
            )
            file_bmb = discord.File(
                fp=img_bmb.image, filename=f'bomb.{img_bmb.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://bomb.{img_bmb.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_bmb, embed=embed)

    @commands.command(description="Porque todo es más bonito con el neón")
    async def neon(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_nn = await dagpi.image_process(
                ImageFeatures.neon(), member.avatar.url
            )
            file_nn = discord.File(
                fp=img_nn.image, filename=f'neon.{img_nn.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://neon.{img_nn.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_nn, embed=embed)

    @commands.hybrid_command(description="El más buscado por la ley")
    async def wanted(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_wntd = await dagpi.image_process(
                ImageFeatures.wanted(), member.avatar.url
            )
            file_wtnd = discord.File(
                fp=img_wntd.image, filename=f'wanted.{img_wntd.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://wanted.{img_wntd.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_wtnd, embed=embed)

    @commands.hybrid_command(description="RIP")
    async def wasted(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_wstd = await dagpi.image_process(
                ImageFeatures.wasted(), member.avatar.url
            )
            file_wstd = discord.File(
                fp=img_wstd.image, filename=f'wasted.{img_wstd.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://wasted.{img_wstd.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_wstd, embed=embed)

    @commands.hybrid_command(description="Capitalismo FTW")
    async def america(self, ctx: commands.Context, member: discord.Member = None):
        if member is None:
            member = ctx.author
        async with ctx.typing():
            img_mrc = await dagpi.image_process(
                ImageFeatures.america(), member.avatar.url
            )
            file_mrc = discord.File(
                fp=img_mrc.image, filename=f'america.{img_mrc.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://america.{img_mrc.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_mrc, embed=embed)

    @commands.hybrid_command(description="Pásale un filtro invertido a esa imagen de perfil")
    async def invert(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_nvrt = await dagpi.image_process(
                ImageFeatures.invert(), member.avatar.url
            )
            file_nvrt = discord.File(
                fp=img_nvrt.image, filename=f'invert.{img_nvrt.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://invert.{img_nvrt.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_nvrt, embed=embed)

    @commands.command(description="Detectando bordes desde 1969")
    async def sobel(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_sbl = await dagpi.image_process(
                ImageFeatures.sobel(), member.avatar.url
            )
            file_sbl = discord.File(
                fp=img_sbl.image, filename=f'sobel.{img_sbl.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://sobel.{img_sbl.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_sbl, embed=embed)

    @commands.hybrid_command(description="A veces hay que censurar, por si acaso")
    async def blur(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_blr = await dagpi.image_process(
                ImageFeatures.blur(), member.avatar.url
            )
            file_blr = discord.File(
                fp=img_blr.image, filename=f'blur.{img_blr.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://blur.{img_blr.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_blr, embed=embed)

    @commands.command(description="Extrae la información RGB de un perfil")
    async def rgb(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_rgb = await dagpi.image_process(
                ImageFeatures.rgb(), member.avatar.url
            )
            file_rgb = discord.File(
                fp=img_rgb.image, filename=f'rgb.{img_rgb.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://rgb.{img_rgb.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_rgb, embed=embed)

    @commands.hybrid_command(description="¿Te gustan las papas fritas?")
    async def deepfry(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_dpfr = await dagpi.image_process(
                ImageFeatures.deepfry(), member.avatar.url
            )
            file_dpfr = discord.File(
                fp=img_dpfr.image, filename=f'deepfry.{img_dpfr.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://deepfry.{img_dpfr.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_dpfr, embed=embed)

    @commands.hybrid_command(description="A S C I I")
    async def ascii(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_sc = await dagpi.image_process(
                ImageFeatures.ascii(), member.avatar.url
            )
            file_sc = discord.File(
                fp=img_sc.image, filename=f'ascii.{img_sc.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://ascii.{img_sc.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_sc, embed=embed)

    @commands.hybrid_command(description="El típico y ya conocido filtro sepia")
    async def sepia(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_sp = await dagpi.image_process(
                ImageFeatures.sepia(), member.avatar.url
            )
            file_sp = discord.File(
                fp=img_sp.image, filename=f'sepia.{img_sp.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://sepia.{img_sp.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_sp, embed=embed)

    # @commands.command()
    # async def glitch(self, ctx, member: discord.Member=None):
    #   """
    #   Cool glitch B)
    #   """
    #   if member is None:
    #     member = ctx.author
    #   async with ctx.typing():
    #     url_gltch = str(member.avatar.replace(static_format="png", size=1024))
    #     img_gltch = await dagpi.image_process(ImageFeatures.glitch(), url_gltch)
    #     file_gltch = discord.File(fp=img_gltch.image,filename=f"glitch.{img_gltch.format}")

    #     embed = discord.Embed(color=ctx.author.color)
    #     embed.set_image(url=f"attachment://glitch.{img_gltch.format}")
    #     embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar.url)
    #     await ctx.reply(file=file_gltch, embed=embed)

    @commands.hybrid_command(description="Imprime esa imagen de perfil en una fotografía")
    async def polaroid(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_plrd = await dagpi.image_process(
                ImageFeatures.polaroid(), member.avatar.url
            )
            file_plrd = discord.File(
                fp=img_plrd.image, filename=f'polaroid.{img_plrd.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://polaroid.{img_plrd.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_plrd, embed=embed)

    @commands.command(description="Vamos a deformar un poco")
    async def swirl(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_swrl = await dagpi.image_process(
                ImageFeatures.swirl(), member.avatar.url
            )
            file_swrl = discord.File(
                fp=img_swrl.image, filename=f'swirl.{img_swrl.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://swirl.{img_swrl.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_swrl, embed=embed)

    @commands.hybrid_command(description="El arte es subjetivo")
    async def paint(self, ctx: commands.Context, member: discord.Member = None):
        if member is None:
            member = ctx.author
        async with ctx.typing():
            img_pnt = await dagpi.image_process(
                ImageFeatures.paint(), member.avatar.url
            )
            file_pnt = discord.File(
                fp=img_pnt.image, filename=f'paint.{img_pnt.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://paint.{img_pnt.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_pnt, embed=embed)

    @commands.command(description="¿Cómo sería si te dibujase un artista?")
    async def sketch(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_sktch = await dagpi.image_process(
                ImageFeatures.sketch(), member.avatar.url
            )
            file_sktch = discord.File(
                fp=img_sktch.image, filename=f'sketch.{img_sktch.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://sketch.{img_sktch.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_sktch, embed=embed)

    @commands.hybrid_command(description="You spin me right round, baby")
    async def spin(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_spn = await dagpi.image_process(
                ImageFeatures.spin(), member.avatar.url
            )
            file_spn = discord.File(
                fp=img_spn.image, filename=f'spin.{img_spn.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://spin.{img_spn.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_spn, embed=embed)

    # @commands.command(aliases=["snap"])
    # async def dissolve(self, ctx, member: discord.Member=None):
    #   """
    #   Thanos snap
    #   """
    #   if member is None:
    #     member = ctx.author
    #   async with ctx.typing():
    #     url_dsslv = str(member.avatar.replace(static_format="png", size=1024))
    #     img_dsslv = await dagpi.image_process(ImageFeatures.dissolve(), url_dsslv)
    #     file_dsslv = discord.File(fp=img_dsslv.image,filename=f"dissolve.{img_dsslv.format}")

    #     embed = discord.Embed(color=ctx.author.color)
    #     embed.set_image(url=f"attachment://dissolve.{img_dsslv.format}")
    #     embed.set_footer(text=f"Solicitado por {ctx.message.author} │ dagpi.xyz", icon_url=member.avatar.url)
    #     await ctx.reply(file=file_dsslv, embed=embed)

    @commands.hybrid_command(description="Usa este con cuidado")
    async def magik(self, ctx: commands.Context, member: discord.Member = None):
        if not member:
            member = ctx.author
        async with ctx.typing():
            img_mgk = await dagpi.image_process(
                ImageFeatures.magik(), member.avatar.url
            )
            file_mgk = discord.File(
                fp=img_mgk.image, filename=f'magik.{img_mgk.format}'
            )

            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=f'attachment://magik.{img_mgk.format}')
            embed.set_footer(
                text=f'Solicitado por {ctx.message.author} │ dagpi.xyz',
                icon_url=member.avatar.url,
            )
            await ctx.reply(file=file_mgk, embed=embed)

    # @commands.command()
    # async def hearts(self, ctx, member: discord.Member=None):
    #   """
    #   <3
    #   """
    #   if member is None:
    #     member = ctx.author
    #   async with ctx.typing():
    #     url_hrts = str(member.avatar.replace(static_format="png", size=1024))

    #     embed = discord.Embed(color=ctx.author.color)
    #     embed.set_image(url=f"https://api.devs-hub.xyz/hearts?image={url_hrts}")
    #     embed.set_footer(text=f"Solicitado por {ctx.message.author} │ api.devs-hub.xyz", icon_url=member.avatar.url)
    #     await ctx.reply(embed=embed)

    # @commands.command()
    # async def simp(self, ctx, member: discord.Member=None):
    #   """
    #   Certified simp moment
    #   """
    #   if member is None:
    #     member = ctx.author
    #   async with ctx.typing():
    #     url_smp = str(member.avatar.replace(static_format="png", size=1024))

    #     embed = discord.Embed(color=ctx.author.color)
    #     embed.set_image(url=f"https://api.devs-hub.xyz/simp?image={url_smp}")
    #     embed.set_footer(text=f"Solicitado por {ctx.message.author} │ api.devs-hub.xyz", icon_url=member.avatar.url)
    #     await ctx.reply(embed=embed)

    # @commands.command()
    # async def like(self, ctx, member: discord.Member=None):
    #   """
    #   [Everyone liked that]
    #   """
    #   if member is None:
    #     member = ctx.author
    #   async with ctx.typing():
    #     url_lk = str(member.avatar.replace(static_format="png", size=1024))

    #     embed = discord.Embed(color=ctx.author.color)
    #     embed.set_image(url=f"https://api.devs-hub.xyz/like?image={url_lk}")
    #     embed.set_footer(text=f"Solicitado por {ctx.message.author} │ api.devs-hub.xyz", icon_url=member.avatar.url)
    #     await ctx.reply(embed=embed)

    # @commands.command()
    # async def joke(self, ctx, member: discord.Member=None):
    #   """
    #   Joke over your head
    #   """
    #   if member is None:
    #     member = ctx.author
    #   async with ctx.typing():
    #     url_jk = str(member.avatar.replace(static_format="png", size=1024))

    #     embed = discord.Embed(color=ctx.author.color)
    #     embed.set_image(url=f"https://api.devs-hub.xyz/joke-over-head?image={url_jk}")
    #     embed.set_footer(text=f"Solicitado por {ctx.message.author} │ api.devs-hub.xyz", icon_url=member.avatar.url)
    #     await ctx.reply(embed=embed)

    # @commands.command()
    # async def beautiful(self, ctx, member: discord.Member=None):
    #   """
    #   Oh this, this is beautiful
    #   """
    #   if member is None:
    #     member = ctx.author
    #   async with ctx.typing():
    #     url_btfl = str(member.avatar.replace(static_format="png", size=1024))

    #     embed = discord.Embed(color=ctx.author.color)
    #     embed.set_image(url=f"https://api.devs-hub.xyz/beautiful?image={url_btfl}")
    #     embed.set_footer(text=f"Solicitado por {ctx.message.author} │ api.devs-hub.xyz", icon_url=member.avatar.url)
    #     await ctx.reply(embed=embed)

    # @commands.command()
    # async def gun(self, ctx, member: discord.Member=None):
    #   """
    #   Plomo o plata
    #   """
    #   if member is None:
    #     member = ctx.author
    #   async with ctx.typing():
    #     url_gn = str(member.avatar.replace(static_format="png", size=1024))

    #     embed = discord.Embed(color=ctx.author.color)
    #     embed.set_image(url=f"https://api.popcat.xyz/gun?image={url_gn}")
    #     embed.set_footer(text=f"Solicitado por {ctx.message.author} │ Pop Cat API", icon_url=member.avatar.url)
    #     await ctx.reply(embed=embed)

    # @commands.command()
    # async def grab(self, ctx, member: discord.Member=None):
    #   """
    #   ¡Ven aquí!
    #   """
    #   if member is None:
    #     member = ctx.author
    #   async with ctx.typing():
    #     url_grb = str(member.avatar.replace(static_format="png", size=1024))

    #     embed = discord.Embed(color=ctx.author.color)
    #     embed.set_image(url=f"https://api.devs-hub.xyz/grab?image={url_grb}")
    #     embed.set_footer(text=f"Solicitado por {ctx.message.author} │ api.devs-hub.xyz", icon_url=member.avatar.url)
    #     await ctx.reply(embed=embed)

    # @commands.command()
    # async def rip(self, ctx, member: discord.Member=None):
    #   """
    #   Rest in Peace
    #   """
    #   if member is None:
    #     member = ctx.author
    #   async with ctx.typing():
    #     url_rp = str(member.avatar.replace(static_format="png", size=1024))

    #     embed = discord.Embed(color=ctx.author.color)
    #     embed.set_image(url=f"https://api.devs-hub.xyz/rip?image={url_rp}")
    #     embed.set_footer(text=f"Solicitado por {ctx.message.author} │ api.devs-hub.xyz", icon_url=member.avatar.url)
    #     await ctx.reply(embed=embed)

    # @commands.command()
    # async def horny(self, ctx, member: discord.Member=None):
    #   """
    #   Licencia para estar horny
    #   """
    #   if member is None:
    #     member = ctx.author
    #   async with ctx.typing():
    #     url_hrn = str(member.avatar.replace(static_format="png", size=1024))

    #     embed = discord.Embed(color=ctx.author.color)
    #     embed.set_image(url=f"https://some-random-api.ml/canvas/horny?avatar={url_hrn}")
    #     embed.set_footer(text=f"Solicitado por {ctx.message.author} │ some-random-api.ml", icon_url=member.avatar.url)
    #     await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Image(bot))
