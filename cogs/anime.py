from datetime import datetime

import animec
import discord
import waifuim
from discord.ext import commands


class anime(
    commands.Cog,
    command_attrs={
        'cooldown': commands.CooldownMapping.from_cooldown(
            1, 10, commands.BucketType.user
        )
    },
):
    """
    Comandos relacionados a cosas de anime.

    Cooldown: 10s per command
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.waifu = waifuim.WaifuAioClient()

    @commands.command(aliases=['anisearch', 'animesearch'])
    # @commands.is_nsfw()
    async def anime(self, ctx, *, name):
        """
        Búsqueda rápida de un anime.
        Asegúrate de escribir bien el nombre de lo que buscas.
        """
        async with ctx.typing():
            try:
                anime = animec.Anime(name)
            except:
                await ctx.send(
                    embed=discord.Embed(
                        description='<:notlikethis:868575058283597904> No encontré el anime que estás buscando.',
                        color=discord.Color.red(),
                    )
                )
                return
        if anime.is_nsfw():
            await ctx.send(
                embed=discord.Embed(
                    description='🔞 No puedes buscar animes nsfw con este comando.',
                    color=discord.Color.red(),
                )
            )
        else:
            embed = discord.Embed(
                title=f'{anime.title_jp} / {anime.title_english}',
                url=anime.url,
                description=f'{anime.description[:300]}...',
                color=discord.Color.random(),
            )
            # embed.add_field(name="#️⃣ Episodios:", value=(anime.episodes))
            embed.add_field(name='👉 Clasificación:', value=str(anime.rating))
            # embed.add_field(name="📊 Posición:", value=str(anime.ranked))
            embed.add_field(name='🔎 Estado:', value=str(anime.status))
            embed.add_field(
                name='🏷️ Géneros:',
                value=', '.join((anime.genres)) or 'No tiene géneros.',
            )
            embed.add_field(name='📺 Tipo:', value=str(anime.type))

            embed.set_thumbnail(url=anime.poster)
            await ctx.send(embed=embed)

    @commands.command(aliases=['anichar', 'animecharacter'])
    async def character(self, ctx, *, name):
        """
        Búsqueda rápida de un personaje de anime.
        Asegúrate de escribir bien el nombre de lo que buscas.
        """
        async with ctx.typing():
            try:
                char = animec.Charsearch(name)
            except:
                await ctx.send(
                    embed=discord.Embed(
                        description='<:notlikethis:868575058283597904> No encontré al personaje que estás buscando.',
                        color=discord.Color.red(),
                    )
                )
                return
            embed = discord.Embed(
                title=char.title, url=char.url, color=discord.Color.random()
            )
            embed.set_image(url=char.image_url)
            embed.set_footer(text=', '.join(list(char.references.keys())[:2]))
            await ctx.send(embed=embed)

    @commands.command(aliases=['animenews'])
    async def aninews(self, ctx, amount: int = 3):
        """
        Las noticias más nuevas del mundo del anime.
        """
        news = animec.Aninews(amount)
        links = news.links
        titles = news.titles
        descriptions = news.description

        embed = discord.Embed(
            title='Noticias más recientes de anime',
            color=discord.Color.random(),
            timestamp=datetime.utcnow(),
        )
        embed.set_thumbnail(url=news.images[0])
        embed.set_footer(
            text='Powered by Animec',
            icon_url='https://animec.readthedocs.io/en/latest/_static/animec.png',
        )

        for i in range(amount):
            embed.add_field(
                name=f'{i+1}) {titles[i]}',
                value=f'{descriptions[i][:200]}...\n[Link]({links[i]})',
                inline=False,
            )

        await ctx.send(embed=embed)

    @commands.command(name='waifu')
    async def waifu(self, ctx: commands.Context):
        """
        Imágenes aleatorias de waifus. ✨
        """
        waifu = await self.waifu.random(
            selected_tags=['waifu'], is_nsfw=['False'], many=False
        )
        embed = discord.Embed(color=discord.Color.random())
        embed.set_image(url=waifu)
        embed.set_footer(text='✨ Powered by waifu.im')
        await ctx.reply(embed=embed)

    @commands.command(name='maid')
    async def maid(self, ctx: commands.Context):
        """
        Imágenes aleatorias de maids. 🎀
        """
        maid = await self.waifu.random(
            selected_tags=['maid'], is_nsfw=['False'], many=False
        )
        embed = discord.Embed(color=discord.Color.random())
        embed.set_image(url=maid)
        embed.set_footer(text='🎀 Powered by waifu.im')
        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(anime(bot))
