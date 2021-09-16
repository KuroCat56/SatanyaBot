from typing import final
from TextToOwO.owo import text_to_owo
from discord.ext import commands
import discord
import random

def random_love():
    love = random.randint(0, 100)
    return(love)

eightballresponses = [
    "Ciertamente.",
    "Es decididamente así.",
    "Sin duda.",
    "Sí - definitivamente.",
    "Puedes confiar en ello.",
    "Como yo lo veo, sí.",
    "Es lo más probable.",
    "Si.",
    "Las señales dicen que si.",
    "Respuesta confusa, intenta otra vez.",
    "Pregunta de nuevo más tarde.",
    "Mejor no decirte ahora.",
    "No se puede predecir ahora.",
    "Concéntrate y pregunta otra vez.",
    "No cuentes con eso",
    "Mi respuesta es no.",
    "Mis fuentes dicen que no.",
    "Muy dudoso."
]

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
    elif member is ctx.author:
      message = "∞ [█████████████████████]\n**Tienes el suficiente ego como para aceptarte y amarte como eres.**"
      await ctx.reply(message, mention_author=False)
    else:
      if calc_love == 0:
        love_messsage = f"{calc_love}% [ . . . . . . . . . . ]\n🚫 No existe compatibilidad entre **{ctx.author.name}** y **{member.name}**"
      elif 1 <= calc_love <= 10:
        love_messsage = f"{calc_love}% [█ . . . . . . . . . ]\n🙅‍♀️ La compatibilidad entre **{ctx.author.name}** y **{member.name}** es demasiado baja"
      elif 11 <= calc_love <= 20:
        love_messsage = f"{calc_love}% [█ . . . . . . . . . ]\n🤔 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es demasiado baja"
      elif 21 <= calc_love <= 30:
        love_messsage = f"{calc_love}% [██ . . . . . . . ]\n😶 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es baja"
      elif 31 <= calc_love <= 40:
        love_messsage = f"{calc_love}% [███ . . . . . . ]\n💌 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es baja"
      elif 41 <= calc_love <= 50:
        love_messsage = f"{calc_love}% [████ . . . . . ]\n💑 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es normal"
      elif 51 <= calc_love <= 60:
        love_messsage = f"{calc_love}% [█████ . . . . ]\n❤️ La compatibilidad entre **{ctx.author.name}** y **{member.name}** es normal"
      elif 61 <= calc_love <= 70:
        love_messsage = f"{calc_love}% [██████ . . . ]\n💕 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es decemte"
      elif 71 <= calc_love <= 80:
        love_messsage = f"{calc_love}% [███████ . . ]\n💝 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es decemte"
      elif 81 <= calc_love <= 90:
        love_messsage = f"{calc_love}% [████████ . ]\n💘 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es muy buena"
      elif 91 <= calc_love <= 99:
        love_messsage = f"{calc_love}% [█████████]\n💞 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es muy buena"
      elif calc_love == 100:
        love_messsage = f"{calc_love}% [██████████]\n💖 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es perfecta"
    embed = discord.Embed(description = f"{love_messsage}", color = 0xff9999)
    await ctx.reply(embed = embed, mention_author=False)

  #Extraído de https://github.com/iiSakuu/Marshmallow
  @commands.command(aliases=['shipname'])
  async def ship(self, ctx, member : discord.Member, member2 : discord.Member = None):
        """
        Descubre el cómo sería el shipname entre dos usuarios 💘
        """

        if member2 is None:
            member2 = ctx.author

        if len(member.display_name) < 4:
            N = len(member.display_name) / 2

            firstmember = member.display_name
            firstship = firstmember[0:int(N)]

            secondmember = member2.display_name
            secondship = secondmember[0:4]

        elif len(member2.display_name) < 4 :
            N = len(member2.display_name) / 2

            firstmember = member.display_name
            firstship = firstmember[0:4]

            secondmember = member2.display_name
            secondship = secondmember[0:int(N)]

        else:

            firstmember = member.display_name
            firstship = firstmember[0:4]

            secondmember = member2.display_name
            secondship = secondmember[0:4]

        shipname = firstship + secondship

        embed = discord.Embed(
            description=f'{member.display_name} + {member2.display_name} = **{shipname}** 💘',
            colour=0xffb5f7
            )

        await ctx.send(embed=embed)

  @commands.command(aliases=['8ball','ball8'])
  async def _8ball(self, ctx, *, question):
    """
    Hazme una pregunta y yo te daré una respuesta.
    """
    eightball = discord.Embed(
        title='Tu pregunta:',
        description=f'{question}',
        color=discord.Colour.random()
        )
    eightball.add_field(
        name='La respuesta:',
        value=f'||{(random.choice(eightballresponses))}||'
      )

    await ctx.reply('🎱 Sacudiendo...', embed=eightball, mention_author=False)

  @commands.command(aliases=['choice'])
  async def choose(ctx, *, msg: str):
    """
    Dame opciones y elegiré una por ti.
    """
    new_msg = msg.split()
    await ctx.send(random.choice(new_msg))

def setup(bot: commands.Bot):
    bot.add_cog(funny(bot))