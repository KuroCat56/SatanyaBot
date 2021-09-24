import discord
from discord.ext import commands
import asyncio
import inspect
import random
import calendar
from googlesearch import search

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
    await embed_message.add_reaction("👍")
    await embed_message.add_reaction("👎")
    await embed_message.add_reaction("🤷")

  @commands.command() #Extraído de https://github.com/cree-py/RemixBot/blob/master/cogs/utility.py
  async def source(self, ctx, command):
      '''Get the source code for any command.'''
      block = "`"*3
      source = inspect.getsource(self.bot.get_command(command).callback)
      if not source:
        return await ctx.send(f'{command} is not a valid command.')
      try:
        await ctx.send(f'{block}py\n{source}\n{block}')
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
    """
    Tablero oficial de Trello para checar los avances.
    """
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

  # @commands.command(name="commands")
  # @commands.guild_only()
  # async def _commands(self, ctx):
    """
    ¿Quieres saber cuántos comandos tengo en mi código?
    """
    value=len([x.name for x in self.bot.commands]) #Variable extraída de AlexFlipnote/discord_bot.py/blob/master/cogs/info.py
    usable = len([await x.can_run(ctx) for x in self.bot.commands])
    await ctx.send(f"¿Mis comandos? Actualmente tengo **{value}** comandos en mi código fuente. Puedes utilizar **{usable}** (´ ω `♡)")

  @commands.command()
  @commands.guild_only()
  @commands.check_any(commands.is_owner(), is_guild_owner())
  async def giveaway(self, ctx):
    """
    ¿Quieres hacer un giveaway? Responde estas simples preguntas.
    """
    def convert(time):
      pos = ['s', 'm', 'h', 'd']
      time_dict = {'s': 1, 'm':60, 'h':3600, 'd':3600*24}
      unit = time[-1]
      
      if unit not in pos:
        return -1
      try:
        val = int(time[:-1])
      except:
        return -2
      return val * time_dict[unit]

    await ctx.send("Por favor responde a estas preguntas para empezar el giveaway.\n**Sólo tienes 15 segundos para responder cada pregunta.**")
    
    questions = ["1. **¿En qué canal se hará el giveaway?**",
                "2. **¿Cuál será la duración del giveaway?** (Ejemplo: 30s, 5h, 3d)",
                "3. **¿Qué es el premio que se sorteará?**"]

    answers = []

    def check(m):
      return m.author == ctx.author and m.channel == ctx.channel
    
    for i in questions:
      await ctx.send(i)

      try:
        msg = await self.bot.wait_for('message', timeout = 15.0, check = check)
      except asyncio.TimeoutError:
        await ctx.send('⌛ Tardaste más de 15 segundos en responder la pregunta. Vuelve a intentarlo pero sé más rápido.')
        return
      else:
        answers.append(msg.content)
      
    try:
      c_id = int(answers[0][2:-1])
    except:
      await ctx.send(f'<:nope:846611758445625364> Hubo un problema con el canal mencionado. Intenta de nuevo mencionando el canal así: {ctx.channel.mention}')
      return
    
    channel = self.bot.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
      await ctx.send(f'<:nope:846611758445625364> Hubo un problema con el tiempo ingresado. Intenta de nuevo usando formato correcto. (*s, m, h* o *d*)')
      return
    elif time == -2:
      await ctx.send('<:nope:846611758445625364> El tiempo ingresado no es un entero. Intenta de nuevo usando un número entero.')
      return

    prize = answers[2]
    await ctx.send(f'El giveaway se realizará en {channel.mention} y durará {answers[1]}')

    embed = discord.Embed(title='**¡GIVEAWAY!**', description = (f'{prize}'), color = ctx.author.color)
    embed.add_field(name = 'Organizado por:', value = ctx.author.mention)
    embed.set_thumbnail(url='https://emoji.gg/assets/emoji/7825_blurple_tada.png')
    embed.set_footer(text = f'Termina en {answers[1]} a partir de ahora.')

    my_msg = await channel.send(embed = embed)
    await my_msg.add_reaction('🎉')
    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(my_msg.id)
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(self.bot.user))
    winner = random.choice(users)

    await channel.send(f'🎉 ¡Felicidades! El usuario {winner.mention} ganó **{prize}** 🎉')

  @commands.command()
  async def calendar(self, ctx, year : int, month : int):
    """
    Vistazo rápido a un mes del año.
    """
    block = "`"*3
    embed = discord.Embed(
      title = f"Mes: {month} - Año: {year}",
      description = f"{block}\n{calendar.month(year, month)}\n{block}",
      color=0xfbf9fa
    )
    await ctx.send(embed=embed)

  @commands.command(aliases = ["ggl"])
  async def google(self, ctx, *, google):
    """
    Búsqueda rápida en Google.
    """
    try:
      results = search(f"{google}", num_results=3, lang="es")
      embed = discord.Embed(
        title = f"Estas son los primeros resultados que he encontrado en Google:",
        description = f"{results[0]}\n=============={results[1]}\n=============={results[2]}",
        color = ctx.author.color
      )
      await ctx.send(embed=embed)
    except:
      await ctx.send("Parece que hubo un error.")

def setup(bot: commands.Bot):
    bot.add_cog(utils(bot))