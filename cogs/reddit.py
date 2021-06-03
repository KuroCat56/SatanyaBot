from discord.ext import commands
import discord
import praw
import private.reddit
import random

#API de Reddit
reddit_api = praw.Reddit(client_id = private.reddit.client_id,
                    client_secret = private.reddit.secret,
                    username = private.reddit.username,
                    password = private.reddit.password,
                    user_agent = private.reddit.user_agent,
                    check_for_async=False)

class reddit(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 5, commands.BucketType.user)}):
  """Comandos que requieren de alguna API"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot

#Comandos que envían memes

#Construcción para comando nya>meme
  @commands.command(name="meme")
  async def meme(self, ctx: commands.Context):
    """
    Obtén un meme de r/memes
    """
    async with ctx.typing():
      submissions = reddit_api.subreddit("memes").hot()
      post = random.randint(1,30)
      ran_submission = (x for x in submissions if not x.stickied)
      for x in range (post): #Creación del embed
        url_memes = next(ran_submission).url
        em_memes = discord.Embed(color = 0xeded2d)
        em_memes.set_image(url = url_memes)
        em_memes.set_footer(text= "r/memes")
    await ctx.send(embed = em_memes)

#Construcción para comando nya>animeme
  @commands.command(name="animeme")
  async def animeme(self, ctx: commands.Context):
    """
    Enviaré un meme otaku de r/animemes
    """
    async with ctx.typing():
      submissions = reddit_api.subreddit("animemes").hot()
      post = random.randint(1,30)
      ran_submission = (x for x in submissions if not x.stickied)
      for x in range (post): #Creación del embed
        url_animemes = next(ran_submission).url
        em_animemes = discord.Embed(color = 0xed2dc0)
        em_animemes.set_image(url = url_animemes)
        em_animemes.set_footer(text= "r/animemes")
    await ctx.send(embed = em_animemes)

#Construcción para comando nya>antimeme
  @commands.command(name="antimeme")
  async def antimeme(self, ctx: commands.Context):
    """
    Kappa
    """
    async with ctx.typing():
      submissions = reddit_api.subreddit("antimemes").hot()
      post = random.randint(1,30)
      ran_submission = (x for x in submissions if not x.stickied)
    for x in range (post): #Creación del embed
        url_antimemes = next(ran_submission).url
        em_antimemes = discord.Embed(color = 0xbbc61b)
        em_antimemes.set_image(url = url_antimemes)
        em_antimemes.set_footer(text= "r/antimemes")
    await ctx.send(embed = em_antimemes)

#Construcción para comando nya>hmmm
  @commands.command(name="hmmm")
  async def hmmm(self, ctx: commands.Context):
    """
    Hmmm...
    """
    async with ctx.typing():
      submissions = reddit_api.subreddit("hmmm").hot()
      post = random.randint(1,30)
      ran_submission = (x for x in submissions if not x.stickied)
    for x in range (post): #Creación del embed
        url_hmmm = next(ran_submission).url
        em_hmmm = discord.Embed(color = 0xe26d46)
        em_hmmm.set_image(url = url_hmmm)
        em_hmmm.set_footer(text= "r/hmmm")
    await ctx.send(embed = em_hmmm)

#Construcción para comando nya>dank
  @commands.command(name="dank")
  async def dank(self, ctx: commands.Context):
    """
    Memes densos de r/dankmemes
    """
    async with ctx.typing():
      submissions = reddit_api.subreddit("dankmemes").hot()
      post = random.randint(1,30)
      ran_submission = (x for x in submissions if not x.stickied)
    for x in range (post): #Creación del embed
        url_dank = next(ran_submission).url
        em_dank = discord.Embed(color = 0x8c5e1e)
        em_dank.set_image(url = url_dank)
        em_dank.set_footer(text= "r/dankmemes")
    await ctx.send(embed = em_dank)

#Construcción para comando nya>chantext
  @commands.command(name="chantext")
  async def chantext(self, ctx: commands.Context):
    """
    Extractos de 4chan en r/greentext
    """
    async with ctx.typing():
      submissions = reddit_api.subreddit("greentext").hot()
      post = random.randint(1,30)
      ran_submission = (x for x in submissions if not x.stickied)
    for x in range (post): #Creación del embed
        url_chantext = next(ran_submission).url
        em_chantext = discord.Embed(color = 0x3bf94e)
        em_chantext.set_image(url = url_chantext)
        em_chantext.set_footer(text= "r/greentext")
    await ctx.send(embed = em_chantext)

#Construcción para comando nya>shower
  @commands.command(name="shower")
  async def shower(self, ctx: commands.Context):
    """
    Frases célebres de r/ShowerThoughts
    """
    async with ctx.typing():
      submissions = reddit_api.subreddit("showerthoughts").hot()
      post = random.randint(1,30)
      ran_submission = (x for x in submissions if not x.stickied)
    for x in range (post): #Creación del embed
        url_shower = next(ran_submission).url
        title_post = next(ran_submission).title
        em_shower = discord.Embed(title = title_post, url = url_shower, color = 0x5683ea)
        em_shower.set_footer(text= "r/ShowerThoughts")
    await ctx.send(embed = em_shower)

#Construcción para comando nya>hispameme
  @commands.command(name="hispameme")
  async def hispameme(self, ctx: commands.Context):
    """
    Memes hispanos
    """
    async with ctx.typing():
      submissions = reddit_api.subreddit("SpanishMeme").hot()
      post = random.randint(1,30)
      ran_submission = (x for x in submissions if not x.stickied)
    for x in range (post): #Creación del embed
        url_hispa = next(ran_submission).url
        em_hispa = discord.Embed(color = 0xf4f27a)
        em_hispa.set_image(url = url_hispa)
        em_hispa.set_footer(text= "r/SpanishMeme")
    await ctx.send(embed = em_hispa)

def setup(bot: commands.Bot):
    bot.add_cog(reddit(bot))