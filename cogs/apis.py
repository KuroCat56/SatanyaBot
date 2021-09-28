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

def get_eevee():
    response = requests.get("https://purrbot.site/api/img/sfw/eevee/gif")
    json_data = json.loads(response.text)
    eevee = json_data['link']
    return (eevee)

def get_fox():
  response = requests.get("https://randomfox.ca/floof/")
  json_data = json.loads(response.text)
  fox = json_data['image']
  return (fox)

def get_dog():
  response = requests.get("https://random.dog/woof.json")
  json_data = json.loads(response.text)
  dog = json_data['url']
  return (dog)

def get_cat():
  response = requests.get("https://aws.random.cat/meow")
  json_data = json.loads(response.text)
  cat = json_data['file']
  return (cat)

def get_shiba():
  response = requests.get("https://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true")
  json_data = json.loads(response.text)
  shiba = json_data[0]
  return (shiba)

class apis(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 5, commands.BucketType.user)}):
  """
  Comandos que dependen de alguna API. Prueba todos para saber lo que hacen.
  
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
      embed.set_footer(text="Powered by zenquotes.io")
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

  @commands.command(name="eevee")
  async def eevee(self, ctx: commands.Context):
    """
    ¿Te gustan los Eevees?
    """
    eevee = get_eevee()
    em_eevee = discord.Embed(color = 0xAF6357)
    em_eevee.set_image(url = eevee)
    em_eevee.set_footer(text= "Powered by PurrBotAPI", icon_url="https://docs.purrbot.site/assets/img/logo.png")
    await ctx.reply(embed = em_eevee, mention_author=False)

  @commands.command(name="fox", aliases=["floof"])
  async def randomfox(self, ctx: commands.Context):
    """
    Imágenes aleatorias de zorros. 🦊
    """
    fox = get_fox()
    em_fox = discord.Embed(color = 0xF98626)
    em_fox.set_image(url = fox)
    em_fox.set_footer(text= "🦊 Powered by randomfox.ca")
    await ctx.reply(embed = em_fox, mention_author=False)

  @commands.command(name="dog", aliases=["woof"])
  async def randomdog(self, ctx: commands.Context):
    """
    Imágenes aleatorias de perros. 🐶
    """
    dog = get_dog()
    em_dog = discord.Embed(color = 0xC77768)
    em_dog.set_image(url = dog)
    em_dog.set_footer(text= "🐶 Powered by random.dog")
    await ctx.reply(embed = em_dog, mention_author=False)

  @commands.command(name="cat", aliases=["meow"])
  async def randomcat(self, ctx: commands.Context):
    """
    Imágenes aleatorias de gatos. 🐱
    """
    cat = get_cat()
    em_cat = discord.Embed(color = 0xFFD356)
    em_cat.set_image(url = cat)
    em_cat.set_footer(text= "🐱 Powered by aws.random.cat")
    await ctx.reply(embed = em_cat, mention_author=False)

  @commands.command(name="shiba", aliases=["inu"])
  async def randomshiba(self, ctx: commands.Context):
    """
    Imágenes aleatorias de shibas inu. 🐕
    """
    shiba = get_shiba()
    em_shiba = discord.Embed(color = 0xF6C436)
    em_shiba.set_image(url = shiba)
    em_shiba.set_footer(text= "🐕 Powered by shibe.online")
    await ctx.reply(embed = em_shiba, mention_author=False)

def setup(bot: commands.Bot):
    bot.add_cog(apis(bot))
