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
    quote = json_data[0]['q'] 
    author = json_data[0]['a']
    return quote, author

def get_emojify():
    response = requests.get(f"https://normal-api.ml/emojify?text={message}")
    json_data = json.loads(response.text)
    emojify = json_data['emojify']
    return (emojify)

class apis(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 3, commands.BucketType.user)}):
  """Comandos que requieren de alguna API"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot

#Comando que envía quotes
  @commands.command(name="quo")
  async def quo(self, ctx: commands.Context):
    """
    Cuidado con las crisis existenciales.
    """
    async with ctx.typing():
      quote_em, author_em = get_quote()
      embed = discord.Embed(
        title=f"{quote_em}",
        description=f"-{author_em}",
        color=0xfbf9fa
      )
    await ctx.send(embed=embed)

#Comando que envía kaomojis
  @commands.command(name="kao")
  async def kao(self, ctx: commands.Context):
    """
     ( ˆᴗˆ  )
    """
    kao = get_kao()
    await ctx.send(kao)

  @commands.command(name="emojify")
  async def emojify(self, ctx):
    """
    🇪 🇲 🇴 🇯 🇮 🇸
    """
    message = ctx.message.content
    message = message.lstrip("emojify>>nya>@SatanyaBot")
    emojify = get_emojify(message)
    await ctx.send(emojify)
    await ctx.message.delete()

def setup(bot: commands.Bot):
    bot.add_cog(apis(bot))
