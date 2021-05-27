from TextToOwO.owo import text_to_owo
from discord.ext import commands

class funny(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.command()
  async def owo(self, ctx):
    """
    Escribe lo que quieras al usar este comando para que lo owofique.
    """
    owo = (text_to_owo(ctx.message.content))
    owo = owo.lstrip("nya>owo") #Se elimina 'nya>owo' del string para que no se imprima en el ctx.send
    await ctx.send(owo)
    await ctx.message.delete() #El bot elimina el mensaje del comando enviado por el usuario

  @commands.command()
  async def say(self, ctx):
    """
    ¿Quieres que diga algo por ti?
    """
    say = ctx.message.content
    say = say.lstrip("nya>say") #Se elimina 'nya>say' del string para que no se imprima en el ctx.send
    await ctx.send(say)
    await ctx.message.delete() #El bot elimina el mensaje del comando enviado por el usuario

def setup(bot: commands.Bot):
    bot.add_cog(funny(bot))