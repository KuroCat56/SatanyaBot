from discord.ext import commands
import discord
import requests
import json
import praw
import private.reddit
import random

#API de Kaomojis
def get_kao():
    response = requests.get("http://kaomoji.n-at.me/random.json")
    json_data = json.loads(response.text)
    kaomoji = json_data['record']['text']
    return (kaomoji)

#API de Zenquotes
#q = quote ; a = author
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = "**" + json_data[0]['q'] + "**" + " -" + json_data[0]['a']
    return (quote)

#API de Reddit
reddit = praw.Reddit(client_id = private.reddit.client_id,
                    client_secret = private.reddit.secret,
                    username = private.reddit.username,
                    password = private.reddit.password,
                    user_agent = private.reddit.user_agent,
                    check_for_async=False)
#Construcción para comando nya>meme
submissions = reddit.subreddit("memes").hot()
post = random.randint(1,20)
ran_submission = (x for x in submissions if not x.stickied)
for x in range (post):
  #Creación del embed
    url_memes = next(ran_submission).url
    em_memes = discord.Embed(title = None, color = 0xeded2d)
    em_memes.set_image(url = url_memes)
#Construcción para comando nya>animeme
subreddit_animemes = reddit.subreddit("animemes")
all_subs_animemes = []
top = subreddit_animemes.top(limit = 50)
for submission in top:
  all_subs_animemes.append(submission)
  random_sub_animemes = random.choice(all_subs_animemes)
  #Creación del embed
  url_animemes = random_sub_animemes.url
  em_animemes = discord.Embed(title = None, color = 0xed2dc0)
  em_animemes.set_image(url = url_animemes)

class apis_commands(commands.Cog):
  """Comandos que requieren de alguna API"""

  def __init__(self, client: commands.Bot):
    self.client = client
#Comando que envía quotes
  @commands.command(name="quo")
  async def quo(self, ctx: commands.Context):
    quote = get_quote()
    await ctx.send(quote)
#Comando que envía kaomojis
  @commands.command(name="kao")
  async def kao(self, ctx: commands.Context):
    kao = get_kao()
    await ctx.send(kao)
#Comandos que envían memes
  @commands.command(name="meme")
  async def meme(self, ctx: commands.Context):
    await ctx.send(embed = em_memes)
  @commands.command(name="animeme")
  async def animeme(self, ctx: commands.Context):
    await ctx.send(embed = em_animemes)


def setup(client: commands.Bot):
    client.add_cog(apis_commands(client))