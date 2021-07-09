import discord
from discord.ext import commands
import asyncio
import inspect

class utils(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 3, commands.BucketType.user)}):
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

  @commands.command(name="commands")
  async def _commands(self, ctx):
    """
    ¿Quieres saber cuántos comandos tengo en mi código?
    """
    value=len([x.name for x in self.bot.commands]) #Variable extraída de AlexFlipnote/discord_bot.py/blob/master/cogs/info.py
    await ctx.send(f"¿Mis comandos? Actualmente tengo **{value}** comandos en mi código fuente. Utiliza `nya>help` para mandarte la lista de comandos que puedes utilizar. (´ ω `♡)")

  @commands.command(name="prefix")
  async def prefix(self, ctx):
    """
    Tengo varios prefijos, prueba a usar el que más te guste.
    """
    await ctx.send("Actualmente mis prefijos son `nya>`, `nya `, `>>` y `@SatanyaBot` ♪└( ＾ω＾ )」")

  @commands.command()
  async def jumbo(self, ctx, emoji: discord.PartialEmoji):
    """
    Deja te paso ese emoji para que lo veas mejor.
    """
    emoji = emoji.url
    await ctx.send(emoji)

  @commands.command()
  async def poll(self, ctx, *args):
    """
    Crea una mini encuesta para lo que gustes
    """
    poll_title = " ".join(args)
    embed = discord.Embed(
        title=f"📊 {poll_title}",
        color=0xfbf9fa,
    )
    embed.set_footer(text=f"Encuesta por: {ctx.message.author} - ¡Reacciona para votar!")
    embed_message = await ctx.send(embed=embed)
    await ctx.message.delete()
    await embed_message.add_reaction("👍")
    await embed_message.add_reaction("👎")
    await embed_message.add_reaction("🤷")

  @commands.command()
  async def source(self, ctx, command):
      '''Get the source code for any command.'''
      source = inspect.getsource(self.bot.get_command(command).callback)
      if not source:
        return await ctx.send(f'{command} is not a valid command.')
      try:
        await ctx.send(f'```py\n{source}\n```')
      except:
        paginated_text = utils.paginate(source)
        for page in paginated_text:
          if page == paginated_text[-1]:
            await ctx.send(f'```py\n{page}\n```')
            break
          await ctx.send(f'```py\n{page}\n```')

def setup(bot: commands.Bot):
    bot.add_cog(utils(bot))