import discord
from discord.ext import commands
import requests
import json

#Lista de endpoints provistas por PurrBotAPI https://purrbot.site/api
PURR = "https://docs.purrbot.site/assets/img/logo.png" #pfp purrbot
PURR_FOOTER = "Powered by PurrBotAPI"

HUG = "https://purrbot.site/api/img/sfw/hug/gif"
BITE = "https://purrbot.site/api/img/sfw/bite/gif"
DANCE = "https://purrbot.site/api/img/sfw/dance/gif"

#Si existe algún problema con al api
ERROR = "Parece que hay un problema con la API o con mi procesamiento. Usa `nya>help` para más información o acude a mi server de soporte usando `nya>invite`"

def get_hug():
    response = requests.get(f"{HUG}")
    json_data = json.loads(response.text)
    hug = json_data['link']
    error_hug = json_data['error']
    return hug, error_hug

def get_bite():
    response = requests.get(f"{BITE}")
    json_data = json.loads(response.text)
    bite = json_data['link']
    error_bite = json_data['error']
    return bite, error_bite

class rol(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 5, commands.BucketType.user)}):
  
  """
  Reacciones de anime para rol y cosas divertidas
  
  Cooldown: 5s per command
  """
  
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command(name="hug")
  async def hug(self, ctx, member: discord.Member=None):
    """
    ¡Abrazos virtuales!
    """
    hug, error = get_hug()
    if member is None:
      message = "¡No puedes abrazarte a tí mismo!\nAunque puedo darte un abrazo si quieres ヽ(・∀・)ﾉ"
      await ctx.reply(message, mention_author=False)
    else:
      if error is not "True":
        async with ctx.typing():
          embed = discord.Embed(
          description=f"🤗 ¡**{ctx.author.name}** ha abrazado a **{member.name}**!", color=discord.Colour.random())
          embed.set_image(url = f"{hug}")
          embed.set_footer(text=f"{PURR_FOOTER}", icon_url=f"{PURR}")
          await ctx.send(embed = embed)
      else:
        await ctx.reply(f"{ERROR}")

  @commands.command(name="bite", aliases=["ñam"])
  async def bite(self, ctx, member: discord.Member=None):
    """
    Ñam ñam ñam~
    """
    bite, error = get_bite()
    if member is None:
      message = "¡No puedes morderte a tí mismo!\nY yo no tengo ganasa de morder a nadie (´Д｀υ)"
      await ctx.reply(message, mention_author=False)
    else:
      if error is not "True":
        async with ctx.typing():
          embed = discord.Embed(
          description=f"😏 ¡**{ctx.author.name}** ha mordido a **{member.name}**!", color=discord.Colour.random())
          embed.set_image(url = f"{bite}")
          embed.set_footer(text=f"{PURR_FOOTER}", icon_url=f"{PURR}")
          await ctx.send(embed = embed)
      else:
        await ctx.reply(f"{ERROR}")

def setup(bot: commands.Bot):
    bot.add_cog(rol(bot))