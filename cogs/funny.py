from typing import final
from TextToOwO.owo import text_to_owo
from discord.ext import commands
import discord
import random

def random_love():
    love = random.randint(0, 100)
    return(love)

class funny(commands.Cog):
  """Comando divertidos muy variados"""
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_message(self, msg):
    self.bot.mention = ["satanya", "satanyabot"]
    mention = self.bot.mention
    if msg.author.bot:
      return
    if any(word in msg.content.lower() for word in mention):
      nya="<:SatanyaBot:858480664143331338>"
    await msg.add_reaction(nya)
    await self.bot.process_commands(msg)

  @commands.command()
  async def owo(self, ctx):
    """
    Escribe lo que quieras al usar este comando para que lo owofique.
    """
    comand = ["nya>owo", ">>owo", "nya", "owo", "@SatanyaBot"]
    owo = ctx.message.content
    new_owo = owo.split()
    final_owo = [word for word in new_owo if word not in comand]
    final_owo = " ".join(final_owo)
    send_final_owo = (text_to_owo(final_owo))
    await ctx.send(send_final_owo)
    await ctx.message.delete() #El bot elimina el mensaje del comando enviado por el usuario

  @commands.command()
  async def say(self, ctx):
    """
    ¿Quieres que diga algo por ti?
    """
    comand = ["nya>say", ">>say", "nya", "say", "@SatanyaBot"]
    say = ctx.message.content
    new_say = say.split()
    final_say = [word for word in new_say if word not in comand]
    final_say = " ".join(final_say)
    await ctx.send(final_say)
    await ctx.message.delete() #El bot elimina el mensaje del comando enviado por el usuario

  #Extraído de https://github.com/LeoCx1000/discord-bots/blob/master/DuckBot/cogs/text.py
  @commands.command()
  async def jumbo(self, ctx, emoji: discord.PartialEmoji):
    """
    Deja te paso ese emoji para que lo veas mejor.
    """
    if emoji.animated: emojiformat = f"*`<`*`a:{emoji.name}:{emoji.id}>`"
    else: emojiformat = f"*`<`*`:{emoji.name}:{emoji.id}>`"
    embed = discord.Embed(description=f"{emojiformat}",color=ctx.me.color)
    embed.set_image(url = emoji.url)
    await ctx.send(embed=embed)

  @commands.command()
  async def love(self, ctx, member: discord.Member=None):
    """
    Calcula tus posibilidades con otro usuario
    """
    calc_love = random_love()
    if member is None:
      message = "¡Primero necesitas etiquetar a alguien!"
      await ctx.reply(message, mention_author=False)
    elif member is ctx.author.name:
      message = "∞ [█████████████████████]\n**Tienes el suficiente ego como para aceptarte y amarte como eres.**"
      await ctx.reply(message, mention_author=False)
    else:
      if calc_love == 0:
        love_messsage = f"{calc_love}% [ . . . . . . . . . . ]\n🚫 No existe compatibilidad entre **{ctx.author.name}** y **{member.name}**"
      elif 1 <= calc_love <= 10:
        love_messsage = f"{calc_love}% [██ . . . . . . . . . ]\n🙅‍♀️ La compatibilidad entre **{ctx.author.name}** y **{member.name}** es demasiado baja"
      elif 11 <= calc_love <= 20:
        love_messsage = f"{calc_love}% [████ . . . . . . . . ]\n🤔 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es demasiado baja"
      elif 21 <= calc_love <= 30:
        love_messsage = f"{calc_love}% [██████ . . . . . . . ]\n🤟 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es baja"
      elif 31 <= calc_love <= 40:
        love_messsage = f"{calc_love}% [████████ . . . . . . ]\n💌 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es baja"
      elif 41 <= calc_love <= 50:
        love_messsage = f"{calc_love}% [██████████ . . . . . ]\n💑 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es normal"
      elif 51 <= calc_love <= 60:
        love_messsage = f"{calc_love}% [████████████ . . . . ]\n❤️ La compatibilidad entre **{ctx.author.name}** y **{member.name}** es normal"
      elif 61 <= calc_love <= 70:
        love_messsage = f"{calc_love}% [██████████████ . . . ]\n💕 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es decemte"
      elif 71 <= calc_love <= 80:
        love_messsage = f"{calc_love}% [████████████████ . . ]\n💝 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es decemte"
      elif 81 <= calc_love <= 90:
        love_messsage = f"{calc_love}% [████████████████ . . ]\n💘 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es muy buena"
      elif 91 <= calc_love <= 99:
        love_messsage = f"{calc_love}% [██████████████████ . ]\n💞 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es muy buena"
      elif calc_love == 100:
        love_messsage = f"{calc_love}% [█████████████████████]\n💖 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es perfecta"
    embed = discord.Embed(description = f"{love_messsage}")
    await ctx.reply(embed = embed, mention_author=False)

def setup(bot: commands.Bot):
    bot.add_cog(funny(bot))