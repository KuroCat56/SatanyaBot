from typing import final
from TextToOwO.owo import text_to_owo
from discord.ext import commands
import discord

class funny(commands.Cog):
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
    final_owo = (text_to_owo(ctx.message.content))
    await ctx.send(final_owo)
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

  @commands.command()
  async def jumbo(self, ctx, emoji: discord.PartialEmoji):
    """
    Deja te paso ese emoji para que lo veas mejor.
    """
    emoji = emoji.url
    await ctx.send(emoji)
def setup(bot: commands.Bot):
    bot.add_cog(funny(bot))