import random
import aiohttp
import discord
from discord.ext import commands
import typing as t


async def get_sub_images(subreddit) -> t.Tuple[discord.Embed, discord.ui.View]:
    posts = []
    async with aiohttp.ClientSession(headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',
        'Accept': 'application/json'
    }).get(f'https://www.reddit.com/r/{subreddit}/.json') as response:
        data = await response.json()
        for i in data['data']['children']:
            if i['data'].get('url'):
                print("aaa")
                posts.append(i['data'])

    subreddit = random.choice(posts)

    embed = discord.Embed(color=0xED2DC0)
    embed.title = f"{subreddit['title']}"
    embed.set_image(url=subreddit['url'])
    embed.set_footer(
        text=f"r/memes | {subreddit['score']} votos | {subreddit['num_comments']} comentarios",
    )
    view = discord.ui.View()
    btn = discord.ui.Button(style=discord.ButtonStyle.url, url=('https://reddit.com' + subreddit['permalink']),
                            label="Ver post original")
    view.add_item(btn)
    return embed, view


class Reddit(
    commands.GroupCog,
    group_name="reddit",
    command_attrs={
        'cooldown': commands.CooldownMapping.from_cooldown(
            1, 5, commands.BucketType.user
        )
    },
):
    """
    Comandos referentes a subreddits.
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Comandos que envían memes

    # Construcción para comando nya>meme

    # Construcción para comando nya>animeme
    @commands.hybrid_command(name='animeme', description="Enviaré un meme otaku de r/animemes")
    async def animeme(self, ctx: commands.Context):
        async with ctx.typing():
            embed, view = await get_sub_images('animemes')
            await ctx.send(embed=embed, view=view)

    # Construcción para comando nya>antimeme
    @commands.hybrid_command(name='antimeme', description="Kappa")
    async def antimeme(self, ctx: commands.Context):
        async with ctx.typing():
            embed, view = await get_sub_images('antimeme')
            await ctx.send(embed=embed, view=view)

    # Construcción para comando nya>hmmm
    @commands.hybrid_command(name='hmmm', description="Hmmm...")
    async def hmmm(self, ctx: commands.Context):
        async with ctx.typing():
            embed, view = await get_sub_images('hmmm')
            await ctx.send(embed=embed, view=view)

    # Construcción para comando nya>chantext
    @commands.hybrid_command(name='chantext', description="Extractos de 4chan en r/greentext")
    async def chantext(self, ctx: commands.Context):
        async with ctx.typing():
            embed, view = await get_sub_images('greentext')
            await ctx.send(embed=embed, view=view)

    # Construcción para comando nya>hispameme
    @commands.command(name='hispameme', description="Memes hispanos")
    async def hispameme(self, ctx: commands.Context):
        async with ctx.typing():
            embed, view = await get_sub_images('SpanishMeme')
            await ctx.send(embed=embed, view=view)

    # Construcción para comando nya>wholesome
    @commands.command(name='wholesome', description="Un poquito del lado bueno de internet.")
    async def wholesome(self, ctx: commands.Context):
        async with ctx.typing():
            embed, view = await get_sub_images('wholesomememes')
            await ctx.send(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(Reddit(bot))