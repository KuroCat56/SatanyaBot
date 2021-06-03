import discord
from discord.ext import commands
import asyncio

class utils(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command()
  async def remind(self, ctx, time, *, task):
    """
    (BETA)Intentaré recordarte cualquier cosa que necesites.
    """
    def convert(time):
      pos = ['s', 'm', 'h', 'd']

      time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

      unit = time[-1]

      if unit not in pos:
        return -1
      try:
        val = int(time[:-1])
      except:
        return -2
      
      return val * time_dict[unit]
    converted_time = convert(time)

    if converted_time == -1:
      await ctx.send("Comando inválido")
      return
    if converted_time == -2:
      await ctx.send("Debes de especificar usando enteros")
      return

    await ctx.send(f"⏱️ {ctx.author.mention}, tu recordatorio para **{task}** fue activado y serás recordado en **{time}**")

    await asyncio.sleep(converted_time)
    await ctx.send(f"⏰ {ctx.author.mention}, tu recordatorio por **{task}** ha terminado.")

  @commands.command()
  async def commands(self, ctx):
    """
    ¿Quieres saber cuántos comandos tengo en mi código?
    """
    value=len([x.name for x in self.bot.commands]) #Variable extraída de AlexFlipnote/discord_bot.py/blob/master/cogs/info.py
    await ctx.send(f"¿Mis comandos? Actualmente tengo **{value}** comandos en mi código fuente. Utiliza `nya>help` para mandarte la lista de comandos que puedes utilizar. (´ ω `♡)")

  # @commands.command()
  # async def getemoji(self, ctx, emoji: discord.PartialEmoji):
  #   """
  #   Deja te paso ese emoji para que lo veas mejor.
  #   """
  #   await ctx.send(emoji.url)

  # @commands.command()
  # async def poll(self, ctx, *args):
  #   """
  #   Crea una mini encuesta para lo que gustes
  #   """
  #   poll_title = " ".join(args)
  #   embed = discord.Embed(
  #       title="📊 ENCUESTA 📊",
  #       description=f"{poll_title}",
  #       color=0xfbf9fa,
  #   )
  #   embed.set_footer(text=f"Creado por: {ctx.message.author} - ¡Reacciona para votar!")
  #   embed_message = await ctx.send(embed=embed)
  #   await embed_message.add_reaction("👍")
  #   await embed_message.add_reaction("👎")
  #   await embed_message.add_reaction("🤷")

def setup(bot: commands.Bot):
    bot.add_cog(utils(bot))