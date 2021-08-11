import discord
from discord.ext import commands
import requests
import json

#Lista de endpoints provistas por PurrBotAPI https://purrbot.site/api
HUG = "https://purrbot.site/api/img/sfw/hug/gif"

def get_hug():
    response = requests.get(f"{HUG}")
    json_data = json.loads(response.text)
    hug = json_data['link']
    error_hug = json_data['error']
    return hug, error_hug

class rol(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 5, commands.BucketType.user)}):
  
  """
  Reacciones de anime para rol y cosas divertidas
  
  Cooldown: 5s per command
  """
  
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command(name="hug")
  async def emojify(self, ctx, member: discord.Member=None):
    """
    ¡Abrazos virtuales!
    """
    hug, error = get_hug()
    if member is None:
      message = "¡No puede abrazarte a tí mismo! Aunque puedo darte un abrazo si quieres ヽ(・∀・)ﾉ"
      await ctx.reply(message, mention_author=False)
    else:
      if error is not "True":
        async with ctx.typing():
          embed = discord.Embed(
          title=f"¡{ctx.author} ha abrazado a {member}!", color=discord.Colour.random())
          embed.set_image(url = f"{hug}")
          await ctx.send(embed = embed)
      else:
        await ctx.reply("Parece que hay un problema con la API o con mi procesamiento. Usa `nya>help` para más información o acude a mi server de soporte usando `nya>server`")


def setup(bot: commands.Bot):
    bot.add_cog(rol(bot))