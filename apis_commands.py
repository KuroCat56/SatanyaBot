from discord.ext import commands
import requests
import json

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

class apis_commands(commands.Cog):
  """Comandos que requieren de alguna API"""

  def __init__(self, client: commands.Bot):
    self.client = client

  @commands.command(name="quo")
  async def quo(self, ctx: commands.Context):
    quote = get_quote()
    await ctx.send(quote)

  @commands.command(name="kao")
  async def kao(self, ctx: commands.Context):
    kao = get_kao()
    await ctx.send(kao)


def setup(client: commands.Bot):
    client.add_cog(apis_commands(client))