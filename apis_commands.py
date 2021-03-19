from discord.ext import commands
import requests
import json

class apis_commands(commands.Cog):
  """Comandos que requieren de alguna API"""

  def __init__(self, client: commands.Bot):
    self.bot = bot

    #API de Zenquotes
#q = quote ; a = author
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = "**" + json_data[0]['q'] + "**" + " -" + json_data[0]['a']
    return (quote)

@client.command()
async def quo(ctx):
  quote = get_quote()
  await ctx.send(quote)

def setup(bot: commands.Bot):
    bot.add_cog(apis_commands(bot))