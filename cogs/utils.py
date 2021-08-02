import discord
from discord.ext import commands
import asyncio
import inspect

class utils(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 5, commands.BucketType.user)}):
  """
  Comando útiles (y no tan útiles)
  
  Cooldown: 5s per command
  """
  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  #Estraído de https://github.com/Rapptz/RoboDanny/blob/0992171592f1b92ad74fe2eb5cf2efe1e9a51be8/cogs/meta.py#L557
  async def say_permissions(self, ctx, member, channel):
        permissions = channel.permissions_for(member)
        e = discord.Embed(colour=member.colour)
        avatar = member.avatar_url_as(static_format='png')
        e.set_author(name=str(member), url=avatar)
        allowed, denied = [], []
        for name, value in permissions:
            name = name.replace('_', ' ').replace('guild', 'server').title()
            if value:
                allowed.append(name)
            else:
                denied.append(name)

        e.add_field(name='Permitido', value='\n'.join(allowed))
        e.add_field(name='Denegado', value='\n'.join(denied))
        await ctx.send(embed=e)

  def is_guild_owner():
    def predicate(ctx):
      return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id
    return commands.check(predicate)

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
    usable=len(([x.name for x in self.bot.commands.can_run]))
    await ctx.send(f"¿Mis comandos? Actualmente tengo **{value}** comandos en mi código fuente. Puedes utilizar **{usable}** (´ ω `♡)")

  @commands.command(name="prefix")
  async def prefix(self, ctx):
    """
    Tengo varios prefijos, prueba a usar el que más te guste.
    """
    await ctx.send("Actualmente mis prefijos son `nya>`, `nya `, `>>` y `@SatanyaBot` ♪└( ＾ω＾ )」")

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

  @commands.command() #Extraído de https://github.com/cree-py/RemixBot/blob/master/cogs/utility.py
  async def source(self, ctx, command):
      '''Get the source code for any command.'''
      source = inspect.getsource(self.bot.get_command(command).callback)
      if not source:
        return await ctx.send(f'{command} is not a valid command.')
      try:
        await ctx.send(f'```py\n{source}\n```')
      except:
        await ctx.send("El bloque de código es demasiado largo como para enviarlo. Será mejor que uses `nya>git` para buscar el apartado por tu cuenta. <:doki_hmm:846549184807043133>")

  @commands.command(aliases=['botperms'])
  @commands.guild_only()
  @commands.check_any(commands.is_owner(), is_guild_owner())
  async def botpermissions(self, ctx, *, channel: discord.TextChannel = None):
        """Shows the bot's permissions in a specific channel.
        If no channel is given then it uses the current one.
        This is a good way of checking if the bot has the permissions needed
        to execute the commands it wants to execute.
        To execute this command you must have Manage Roles permission.
        You cannot use this in private messages.
        """
        channel = channel or ctx.channel
        member = ctx.guild.me
        await self.say_permissions(ctx, member, channel)

  @commands.command(aliases=['perms'])
  @commands.guild_only()
  async def permissions(self, ctx, member: discord.Member = None, channel: discord.TextChannel = None):
        """Shows a member's permissions in a specific channel.
        If no channel is given then it uses the current one.
        You cannot use this in private messages. If no member is given then
        the info returned will be yours.
        """
        channel = channel or ctx.channel
        if member is None:
            member = ctx.author

        await self.say_permissions(ctx, member, channel)

  @commands.command()
  async def trello(self, ctx):
    embed = discord.Embed(
    title="¿Qué hay pendiente en la lista?",
    description="🌸 SatanyaBot siempre está en desarrollo agregando nuevas características y arreglando otras.\n🍒 Si te da curiosidad saber en qué se está trabajando checa el link de abajo.",
    color=0xfbf9fa
    )
    embed.add_field(
    name="Tablero oficial de SatanyaBot",
    value="[Trello](https://trello.com/b/Z432JC83)",
    )
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/829223734559637545/859941157944557588/headAsset_214x-8.png?width=465&height=473")
    embed.set_image(url="https://images.unsplash.com/photo-1555231955-348aa2312e19")
    await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(utils(bot))