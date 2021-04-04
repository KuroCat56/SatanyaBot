from TextToOwO.owo import text_to_owo
from discord.ext import commands

class funny(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client
  
  @commands.command()
  async def owo(self, ctx):
    owo = (text_to_owo(ctx.message.content))
    owo = owo.lstrip("nya>owo") #Se elimina 'nya>owo' del string para que no se imprima en el ctx.send
    await ctx.send(owo)
    await ctx.message.delete() #El bot elimina el mensaje del comando enviado por el usuario

def setup(client: commands.Bot):
    client.add_cog(funny(client))