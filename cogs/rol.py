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

def setup(bot: commands.Bot):
    bot.add_cog(rol(bot))