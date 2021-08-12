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
PAT = "https://purrbot.site/api/img/sfw/pat/gif"
CUDDLE = "https://purrbot.site/api/img/sfw/cuddle/gif"
SLAP = "https://purrbot.site/api/img/sfw/slap/gif"
SMILE = "https://purrbot.site/api/img/sfw/smile/gif"
TICKLE = "https://purrbot.site/api/img/sfw/tickle/gif"
POKE = "https://purrbot.site/api/img/sfw/poke/gif"
BLUSH = "https://purrbot.site/api/img/sfw/blush/gif"
CRY = "https://purrbot.site/api/img/sfw/cry/gif"
KISS = "https://purrbot.site/api/img/sfw/kiss/gif"
TAIL = "https://purrbot.site/api/img/sfw/tail/gif"
FEED = "https://purrbot.site/api/img/sfw/feed/gif"

#Lista de endpoint provistas por WaifuPics
WAIFU = "https://avatars.githubusercontent.com/u/71401053" #repo avatar
WAIFU_FOOTER = "Powered by Waifu.pics API"

SMUG = "https://api.waifu.pics/sfw/smug"
WAVE = "https://api.waifu.pics/sfw/wave"
YEET = "https://api.waifu.pics/sfw/yeet"

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

def get_dance():
    response = requests.get(f"{DANCE}")
    json_data = json.loads(response.text)
    dance = json_data['link']
    error_dance = json_data['error']
    return dance, error_dance

def get_pat():
    response = requests.get(f"{PAT}")
    json_data = json.loads(response.text)
    pat = json_data['link']
    error_pat = json_data['error']
    return pat, error_pat

def get_cuddle():
    response = requests.get(f"{CUDDLE}")
    json_data = json.loads(response.text)
    cuddle = json_data['link']
    error_cuddle = json_data['error']
    return cuddle, error_cuddle

def get_slap():
    response = requests.get(f"{SLAP}")
    json_data = json.loads(response.text)
    slap = json_data['link']
    error_slap = json_data['error']
    return slap, error_slap

def get_smile():
    response = requests.get(f"{SMILE}")
    json_data = json.loads(response.text)
    smile = json_data['link']
    error_smile = json_data['error']
    return smile, error_smile

def get_tickle():
    response = requests.get(f"{TICKLE}")
    json_data = json.loads(response.text)
    tickle = json_data['link']
    error_tickle = json_data['error']
    return tickle, error_tickle

def get_poke():
    response = requests.get(f"{POKE}")
    json_data = json.loads(response.text)
    poke = json_data['link']
    error_poke = json_data['error']
    return poke, error_poke

def get_blush():
    response = requests.get(f"{BLUSH}")
    json_data = json.loads(response.text)
    blush = json_data['link']
    error_blush = json_data['error']
    return blush, error_blush

def get_cry():
    response = requests.get(f"{CRY}")
    json_data = json.loads(response.text)
    cry = json_data['link']
    error_cry = json_data['error']
    return cry, error_cry

def get_kiss():
    response = requests.get(f"{KISS}")
    json_data = json.loads(response.text)
    kiss = json_data['link']
    error_kiss = json_data['error']
    return kiss, error_kiss

def get_tail():
    response = requests.get(f"{TAIL}")
    json_data = json.loads(response.text)
    tail = json_data['link']
    error_tail = json_data['error']
    return tail, error_tail

def get_feed():
    response = requests.get(f"{FEED}")
    json_data = json.loads(response.text)
    feed = json_data['link']
    error_feed = json_data['error']
    return feed, error_feed

def get_smug():
    response = requests.get(f"{SMUG}")
    json_data = json.loads(response.text)
    smug = json_data['url']
    return smug

def get_wave():
    response = requests.get(f"{WAVE}")
    json_data = json.loads(response.text)
    wave = json_data['url']
    return wave

def get_yeet():
    response = requests.get(f"{YEET}")
    json_data = json.loads(response.text)
    yeet = json_data['url']
    return yeet

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
      if error is not "true":
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
      if error is not "true":
        async with ctx.typing():
          embed = discord.Embed(
          description=f"😏 ¡**{ctx.author.name}** ha mordido a **{member.name}**!", color=discord.Colour.random())
          embed.set_image(url = f"{bite}")
          embed.set_footer(text=f"{PURR_FOOTER}", icon_url=f"{PURR}")
        await ctx.send(embed = embed)
      else:
        await ctx.reply(f"{ERROR}")

  @commands.command(name="dance", aliases=["party"])
  async def dance(self, ctx, member: discord.Member=None):
    """
    ¡Esto hay que celebrarlo!
    """
    dance, error = get_dance()
    if error is not "true":
      async with ctx.typing():
            if member is None:
              desc = f"🎉 ¡**{ctx.author.name}** se ha puesto a bailar!"
            else:
              desc = f"🎊 ¡**{ctx.author.name}** y **{member.name}** están bailando juntos!"
            embed = discord.Embed(
            description=f"{desc}", color=discord.Colour.random())
            embed.set_image(url = f"{dance}")
            embed.set_footer(text=f"{PURR_FOOTER}", icon_url=f"{PURR}")
            await ctx.send(embed = embed)
    else:
      await ctx.reply(f"{ERROR}")

  @commands.command(name="pat", aliases=["headpat"])
  async def pat(self, ctx, member: discord.Member=None):
    """
    ¿Alguien se merece unos pat-pat?
    """
    pat, error = get_pat()
    if member is None:
      message = "¡No puedes darte pat-pats a tí mismo!\nPero puede darme unos a mí (o´▽`o)"
      await ctx.reply(message, mention_author=False)
    else:
      if error is not "true":
        async with ctx.typing():
          embed = discord.Embed(
          description = f"❣️ **{ctx.author.name}** le ha dado unos pat-pats a **{member.name}**", color=discord.Colour.random())
          embed.set_image(url = f"{pat}")
          embed.set_footer(text=f"{PURR_FOOTER}", icon_url=f"{PURR}")
        await ctx.send(embed = embed)
      else:
        await ctx.reply(f"{ERROR}")

  @commands.command(name="cuddle")
  async def cuddle(self, ctx, member: discord.Member=None):
    """
    Abrazos pero con más cariño~
    """
    cuddle, error = get_cuddle()
    if member is None:
      message = "¡No puedes darte cariños a tí mismo!\nPero puede darme unos a mí (o´▽`o)"
      await ctx.reply(message, mention_author=False)
    else:
      if error is not "true":
        async with ctx.typing():
          embed = discord.Embed(
          description = f"💞 **{ctx.author.name}** abraza con mucho cariño a **{member.name}**", color=discord.Colour.random())
          embed.set_image(url = f"{cuddle}")
          embed.set_footer(text=f"{PURR_FOOTER}", icon_url=f"{PURR}")
          await ctx.send(embed = embed)
      else:
        await ctx.reply(f"{ERROR}")

  @commands.command(name="slap")
  async def slap(self, ctx, member: discord.Member=None):
    """
    Porque a veces alguien necesita una cachetada (con cariño)
    """
    slap, error = get_slap()
    if member is None:
      message = "¡No puedes pegarte a tí mismo!\nA no ser que te guste..."
      await ctx.reply(message, mention_author=False)
    else:
      if error is not "true":
        async with ctx.typing():
          embed = discord.Embed(
          description = f"💢 **{ctx.author.name}** ha cacheteado a **{member.name}**", color=discord.Colour.random())
          embed.set_image(url = f"{slap}")
          embed.set_footer(text=f"{PURR_FOOTER}", icon_url=f"{PURR}")
        await ctx.send(embed = embed)
      else:
        await ctx.reply(f"{ERROR}")

  @commands.command(name="smile")
  async def smile(self, ctx):
    """
    Una sonrisa vale más que mil palabras
    """
    smile, error = get_smile()
    if error is not "true":
      async with ctx.typing():
        embed = discord.Embed(
        description = f"✨ **{ctx.author.name}** se ha puesto muy feliz", color=discord.Colour.random())
        embed.set_image(url = f"{smile}")
        embed.set_footer(text=f"{PURR_FOOTER}", icon_url=f"{PURR}")
      await ctx.send(embed = embed)
    else:
      await ctx.reply(f"{ERROR}")

  @commands.command(name="tickle")
  async def tickle(self, ctx, member: discord.Member=None):
    """
    Para molestar a los que tienen cosquillas
    """
    tickle, error = get_tickle()
    if member is None:
      message = "¡No puedes darte cosquillas a tí mismo!\nAunque puedo darte algunos si quieres (─‿‿─)"
      await ctx.reply(message, mention_author=False)
    else:
      if error is not "true":
        async with ctx.typing():
          embed = discord.Embed(
          description = f"🤣 ¡**{ctx.author.name}** le hace cosquillas a **{member.name}!**", color=discord.Colour.random())
          embed.set_image(url = f"{tickle}")
          embed.set_footer(text=f"{PURR_FOOTER}", icon_url=f"{PURR}")
        await ctx.send(embed = embed)
      else:
        await ctx.reply(f"{ERROR}")

  @commands.command(name="poke")
  async def poke(self, ctx, member: discord.Member=None):
    """
    ¿Quieres llamar la atención de alguien?
    """
    poke, error = get_poke()
    if member is None:
      message = "¡No puedes molestarte a tí mismo!"
      await ctx.reply(message, mention_author=False)
    else:
      if error is not "true":
        async with ctx.typing():
          embed = discord.Embed(
          description = f"👉 **{ctx.author.name}** está molestando a **{member.name}**", color=discord.Colour.random())
          embed.set_image(url = f"{poke}")
          embed.set_footer(text=f"{PURR_FOOTER}", icon_url=f"{PURR}")
        await ctx.send(embed = embed)
      else:
        await ctx.reply(f"{ERROR}")

  @commands.command(name="blush")
  async def blush(self, ctx):
    """
    Rojo como tomate
    """
    blush, error = get_blush()
    if error is not "true":
      async with ctx.typing():
        embed = discord.Embed(
        description = f"😳 **{ctx.author.name}** se ha puesto rojo como tomate", color=discord.Colour.random())
        embed.set_image(url = f"{blush}")
        embed.set_footer(text=f"{PURR_FOOTER}", icon_url=f"{PURR}")
      await ctx.send(embed = embed)
    else:
      await ctx.reply(f"{ERROR}")

  @commands.command(name="cry", aliases=["sad"])
  async def cry(self, ctx):
    """
    :(
    """
    cry, error = get_cry()
    if error is not "true":
      async with ctx.typing():
        embed = discord.Embed(
        description = f"😭 **{ctx.author.name}** está llorando. Que alguien le consuele :(", color=discord.Colour.random())
        embed.set_image(url = f"{cry}")
        embed.set_footer(text=f"{PURR_FOOTER}", icon_url=f"{PURR}")
      await ctx.send(embed = embed)
    else:
      await ctx.reply(f"{ERROR}")

  @commands.command(name="kiss")
  async def kiss(self, ctx, member: discord.Member=None):
    """
    ¿Son pareja? A ver, bésense
    """
    kiss, error = get_kiss()
    if member is None:
      message = "¡No puedes besarte a tí mismo!\nA no ser que uses algún espejo o algo parecido (￣▽￣*)ゞ"
      await ctx.reply(message, mention_author=False)
    else:
      if error is not "true":
        async with ctx.typing():
          embed = discord.Embed(
          description = f"💖 **{ctx.author.name}** he besado a **{member.name}**~", color=discord.Colour.random())
          embed.set_image(url = f"{kiss}")
          embed.set_footer(text=f"{PURR_FOOTER}", icon_url=f"{PURR}")
        await ctx.send(embed = embed)
      else:
        await ctx.reply(f"{ERROR}")

  @commands.command(name="tail", aliases=["wag"])
  async def tail(self, ctx):
    """
    ¿La emoción te supera?
    """
    tail, error = get_tail()
    if error is not "true":
      async with ctx.typing():
        embed = discord.Embed(
        description = f"🦊 **¡{ctx.author.name}** está moviendo su colita!", color=discord.Colour.random())
        embed.set_image(url = f"{tail}")
        embed.set_footer(text=f"{PURR_FOOTER}", icon_url=f"{PURR}")
      await ctx.send(embed = embed)
    else:
      await ctx.reply(f"{ERROR}")

  @commands.command(name="feed")
  async def feed(self, ctx, member: discord.Member=None):
    """
    ¿Quién tiene hambre?
    """
    feed, error = get_feed()
    if error is not "true":
      async with ctx.typing():
            if member is None:
              desc = f"🍴 **{ctx.author.name}** está comiendo algo rico"
            else:
              desc = f"🥄 ¡**{ctx.author.name}** le está dando de comer a **{member.name}**!"
            embed = discord.Embed(
            description=f"{desc}", color=discord.Colour.random())
            embed.set_image(url = f"{feed}")
            embed.set_footer(text=f"{PURR_FOOTER}", icon_url=f"{PURR}")
            await ctx.send(embed = embed)
    else:
      await ctx.reply(f"{ERROR}")

  @commands.command(name="smug")
  async def smug(self, ctx):
    """
    >;)
    """
    smug = get_smug()
    async with ctx.typing():
      embed = discord.Embed(
      description = f"💯 **{ctx.author.name}** tiene mucha malicia", color=discord.Colour.random())
      embed.set_image(url = f"{smug}")
      embed.set_footer(text=f"{WAIFU_FOOTER}", icon_url=f"{WAIFU}")
    await ctx.send(embed = embed)

  @commands.command(name="hi", aliases=["hola"])
  async def wave(self, ctx):
    """
    ¡Hola a todos!
    """
    hi = get_wave()
    async with ctx.typing():
      embed = discord.Embed(
      description = f"👋 **{ctx.author.name}** está saludando", color=discord.Colour.random())
      embed.set_image(url = f"{hi}")
      embed.set_footer(text=f"{WAIFU_FOOTER}", icon_url=f"{WAIFU}")
    await ctx.send(embed = embed)

  @commands.command(name="yeet")
  async def yeet(self, ctx, member: discord.Member=None):
    """
    YEET
    """
    yeet = get_yeet()
    if member is None:
      message = "¡No puedes hacerte yeet a tí mismo!"
      await ctx.reply(message, mention_author=False)
    else:
      async with ctx.typing():
        embed = discord.Embed(
        description = f"🚀 ¡**{ctx.author.name}** mandó a volar a {member.name}!", color=discord.Colour.random())
        embed.set_image(url = f"{yeet}")
        embed.set_footer(text=f"{WAIFU_FOOTER}", icon_url=f"{WAIFU}")
      await ctx.send(embed = embed)

def setup(bot: commands.Bot):
    bot.add_cog(rol(bot))