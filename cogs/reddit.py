import random
from os import environ

import asyncpraw as praw
import discord
from discord.ext import commands

# API de Reddit
reddit_api = praw.Reddit(
    client_id=environ['REDDIT_CLIENT_ID'],
    client_secret=environ['REDDIT_CLIENT_SECRET'],
    username=environ['REDDIT_USERNAME'],
    password=environ['REDDIT_PASSWORD'],
    user_agent=environ['REDDIT_USER_AGENT'],
)


class Reddit(
    commands.Cog,
    command_attrs={
        'cooldown': commands.CooldownMapping.from_cooldown(
            1, 5, commands.BucketType.user
        )
    },
):
    """
    Comandos referentes a subreddits.
    Obtén los posts más interesantes de alguna subreddit.
    Si alguna imagen no carga es porque es demasiado grande y Discord no es capaz de mostrarla.

    Si te gustaría que se agregase una subreddit adicional contacta a mi creador o únete a mi servidor (nya>invite).

    Cooldown: 5s per command
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Comandos que envían memes

    # Construcción para comando nya>meme
    @commands.hybrid_command(name='meme', description="Obtén un meme de r/memes")
    async def meme(self, ctx: commands.Context):
        async with ctx.typing():
            subreddit = await reddit_api.subreddit('memes')
            async for submission in subreddit.hot(limit=3):
                embed = discord.Embed(color=0xED2DC0)
                embed.set_image(url=submission.url)
                embed.set_footer(
                    text=f'r/memes | {submission.score} votos | {submission.num_comments} comentarios',
                )
                await ctx.send(embed=embed)

    # Construcción para comando nya>animeme
    @commands.hybrid_command(name='animeme', description="Enviaré un meme otaku de r/animemes")
    async def animeme(self, ctx: commands.Context):
        async with ctx.typing():
            subreddit = await reddit_api.subreddit('animemes')
            async for submission in subreddit.hot(limit=3):
                embed = discord.Embed(color=0xED2DC0)
                embed.set_image(url=submission.url)
                embed.set_footer(
                    text=f'r/animemes | {submission.score} votos | {submission.num_comments} comentarios',
                )
                await ctx.send(embed=embed)

    # Construcción para comando nya>antimeme
    @commands.hybrid_command(name='antimeme', description="Kappa")
    async def antimeme(self, ctx: commands.Context):
        async with ctx.typing():
            subreddit = await reddit_api.subreddit('antimeme')
            async for submission in subreddit.hot(limit=3):
                embed = discord.Embed(color=0xED2DC0)
                embed.set_image(url=submission.url)
                embed.set_footer(
                    text=f'r/antimeme | {submission.score} votos | {submission.num_comments} comentarios',
                )
                await ctx.send(embed=embed)

    # Construcción para comando nya>hmmm
    @commands.hybrid_command(name='hmmm', description="Hmmm...")
    async def hmmm(self, ctx: commands.Context):
        async with ctx.typing():
            subreddit = await reddit_api.subreddit('hmmm')
            async for submission in subreddit.hot(limit=3):
                embed = discord.Embed(color=0xED2DC0)
                embed.set_image(url=submission.url)
                embed.set_footer(
                    text=f'r/hmmm | {submission.score} votos | {submission.num_comments} comentarios',
                )
                await ctx.send(embed=embed)

    # Construcción para comando nya>dank
    @commands.command(name='dank', description="Memes densos de r/dankmemes")
    async def dank(self, ctx: commands.Context):
        async with ctx.typing():
            subreddit = await reddit_api.subreddit('dankmemes')
            async for submission in subreddit.hot(limit=3):
                embed = discord.Embed(color=0xED2DC0)
                embed.set_image(url=submission.url)
                embed.set_footer(
                    text=f'r/dankmemes | {submission.score} votos | {submission.num_comments} comentarios',
                )
                await ctx.send(embed=embed)

    # Construcción para comando nya>chantext
    @commands.hybrid_command(name='chantext', description="Extractos de 4chan en r/greentext")
    async def chantext(self, ctx: commands.Context):
        async with ctx.typing():
            subreddit = await reddit_api.subreddit('greentext')
            async for submission in subreddit.hot(limit=3):
                embed = discord.Embed(color=0xED2DC0)
                embed.set_image(url=submission.url)
                embed.set_footer(
                    text=f'r/greentext | {submission.score} votos | {submission.num_comments} comentarios',
                )
                await ctx.send(embed=embed)

    # Construcción para comando nya>shower
    @commands.hybrid_command(name='shower', description="Frases célebres de r/ShowerThoughts")
    async def shower(self, ctx: commands.Context):
        async with ctx.typing():
            subreddit = await reddit_api.subreddit('ShowerThoughts')
            async for submission in subreddit.hot(limit=3):
                embed = discord.Embed(color=0xED2DC0)
                embed.set_author(name=submission.title)
                embed.set_image(url=submission.url)
                embed.set_footer(
                    text=f'r/ShowerThoughts | {submission.score} votos | {submission.num_comments} comentarios',
                )
                await ctx.send(embed=embed)

    # Construcción para comando nya>hispameme
    @commands.command(name='hispameme', description="Memes hispanos")
    async def hispameme(self, ctx: commands.Context):
        async with ctx.typing():
            subreddit = await reddit_api.subreddit('SpanishMeme')
            async for submission in subreddit.hot(limit=3):
                embed = discord.Embed(color=0xED2DC0)
                embed.set_image(url=submission.url)
                embed.set_footer(
                    text=f'r/SpanishMeme | {submission.score} votos | {submission.num_comments} comentarios',
                )
                await ctx.send(embed=embed)

    # Construcción para comando nya>wholesome
    @commands.command(name='wholesome', description="Un poquito del lado bueno de internet.")
    async def wholesome(self, ctx: commands.Context):
        async with ctx.typing():
            subreddit = await reddit_api.subreddit('wholesomememes')
            async for submission in subreddit.hot(limit=3):
                embed = discord.Embed(color=0xED2DC0)
                embed.set_image(url=submission.url)
                embed.set_footer(
                    text=f'r/wholesomememes | {submission.score} votos | {submission.num_comments} comentarios',
                )
                await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Reddit(bot))
