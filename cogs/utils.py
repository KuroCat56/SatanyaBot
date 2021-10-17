import discord
from discord.ext import commands
import asyncio
import inspect
import random
import calendar
from googlesearch import search
from googletrans import Translator

class utils(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 15, commands.BucketType.user)}):
  """
  Comando útiles (y no tan útiles)
  
  Cooldown: 15s per command
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

    Segundos (s), Minutos (m), Horas (h), Días (d)
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
        """
        Muestra los permisos del bot en un canal específico o en el actual.
        Esta es una buena manera para checar si el bot tiene los permisos necesarios para ejecutar ciertos comandos.
        """
        channel = channel or ctx.channel
        member = ctx.guild.me
        await self.say_permissions(ctx, member, channel)

  @commands.command(aliases=['perms'])
  @commands.guild_only()
  async def permissions(self, ctx, member: discord.Member = None, channel: discord.TextChannel = None):
        """
        Muestra los permisos de un usuario en un canal específico o en el actual.
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

  @commands.command()
  @commands.guild_only()
  @commands.check_any(commands.is_owner(), is_guild_owner())
  async def giveaway(self, ctx):
    """
    ¿Quieres hacer un giveaway? Responde estas simples preguntas.

    Solo el propietario del servidor puede realizar los giveaway.
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
    Muestra los primeros tres resultados de una búsqueda en Google.
    """
    try:
      results = search(f"{google}", num_results=3, lang="es")
      embed = discord.Embed(
        title = f"Esto es lo que he encontrado en Google sobre:\n__{google}__",
        description = f"1️⃣ {results[0]}\n\n2️⃣ {results[1]}\n\n3️⃣ {results[2]}",
        color = ctx.author.color
      )
      await ctx.send(embed=embed)
    except:
      await ctx.send("Parece que hubo un error.")

  @commands.command(aliases = ["traducir", "traductor"])
  async def translate(self, ctx, lang : str, *, texto):
    """
    Traducción rápida usando el traductor de Google.
    """
    block = "`"*3
    translator = Translator()
    try:
      translated = translator.translate(f"{texto}", dest=f"{lang}")
      detection = translator.detect(f"{texto}")
      embed = discord.Embed(
        description = f"Traducción de __{detection.lang}__ a __{lang}__:",
        color = ctx.author.color
      )
      embed.add_field(
        name= "Texto ingresado:",
        value=f"{block}\n{texto}\n{block}",
        inline=False
      )
      embed.add_field(
        name= "Texto traducido:",
        value=f"{block}\n{translated.text}\n{block}",
        inline=False
      )
      embed.set_footer(
        text=f"Estoy {detection.confidence*100}% segura de que el texto ingresado es: {detection.lang}"
        )
      await ctx.reply(embed=embed, mention_author=False)
    except:
      embed = discord.Embed(
        description = f"**Parece que hubo un error:**\n1️⃣ Es probable que debas de checar si el lenguaje que escibiste ({lang}) esté bien escrito.\nPuedes comprobarlo aquí: http://www.lingoes.net/en/translator/langcode.htm \n2️⃣ Es probable que el lenguaje que escribiste ({lang} no esté disponible.)",
        color = ctx.author.color
      )
      await ctx.send(embed=embed)


  @commands.command()
  @commands.check_any(commands.is_owner(), commands.has_permissions(manage_messages=True))
  async def clear(self, ctx, number: int):
    """
    Borra todos mis mensajes en el canal actual.
    """
    counter = 0
    async for message in ctx.channel.history(limit=100):
        if message.author.id == ctx.bot.user.id:
            await message.delete()
            counter += 1
        if counter >= number:
            break
    embed = discord.Embed(
      title = f"🧹 He borrado `{number}` de mis mensajes en este canal",
      description = f"",
      color = ctx.author.color
      )
    await ctx.send(embed=embed, delete_after=10)

  @commands.command(name="purge", aliases=["pu"])
  @commands.check_any(commands.is_owner(), commands.has_permissions(manage_messages=True))
  async def purge(self, ctx:commands.Context, *, amount:int):
    """
    Borra x cantidad de mensajes en el canal actual.
    """
    embed = discord.Embed(
        color=self.bot.color,
        timestamp=ctx.message.created_at
    )
    embed.set_footer(text=ctx.author, icon_url=ctx.author.display_avatar.url)
    if amount > 50:
        embed.title = "No puedo borrar +50 de mensajes."
        return await ctx.send(embed=embed, delete_after=5)
    embed.title = f"Borrados {amount} mensajes en este canal."
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(embed=embed, delete_after=5)

def setup(bot: commands.Bot):
    bot.add_cog(utils(bot))