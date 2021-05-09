import os
from discord.ext import commands
import requests
import json
import discord

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
    quote_quo = json_data[0]['q'] 
    #quote_a = json_data[0]['a']
    return ()

class apis(commands.Cog):
  """Comandos que requieren de alguna API"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot

#Comando que envía quotes
  @commands.command(name="quo")
  async def quo(self, ctx: commands.Context):
    #quote = get_quote()
    embed = discord.Embed(
      title=get_quote()
    )
    await ctx.send(embed=embed)

#Comando que envía kaomojis
  @commands.command(name="kao")
  async def kao(self, ctx: commands.Context):
    kao = get_kao()
    await ctx.send(kao)

def setup(bot: commands.Bot):
    bot.add_cog(apis(bot))
