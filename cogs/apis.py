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

class apis(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 5, commands.BucketType.user)}):
  """
  Comandos que requieren de alguna API
  
  Cooldown: 5s per command
  """

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

    response = requests.get(f"https://normal-api.ml/emojify?text={message}")
    json_data = json.loads(response.text)
    emojify = json_data['emojify']

    await ctx.send(emojify)
    await ctx.message.delete()

  @commands.command(name="reverse")
  async def reverse(self, ctx):
    """
    asrever ne otxeT
    """
    message = ctx.message.content
    message = message.lstrip(">>nya>@SatanyaBotSatanya")
    message = message.lstrip("reverse")

    response = requests.get(f"https://normal-api.ml/reverse?text={message}")
    json_data = json.loads(response.text)
    reversed = json_data['reversed']

    await ctx.reply(reversed, mention_author=False)

def setup(bot: commands.Bot):
    bot.add_cog(apis(bot))
