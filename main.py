import discord
from discord.ext import commands
from datetime import datetime
import os
import random
import asyncio
import config
from dotenv import load_dotenv

#test
#Prefijo de comando de discord.ext
bot = commands.Bot(command_prefix="nya>")
bot.launch_time = datetime.utcnow()

@bot.command()
@commands.is_owner()
async def load(cog, extension):
  bot.load_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def unload(cog, extension):
  bot.unload_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def reload(cog, extension):
  bot.reload_extension(f"cogs.{extension}")

@bot.command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"{days}d, {hours}h, {minutes}m, {seconds}s")


#on_ready: Cuando el bot esté activo y funcional mandará un mensaje confirmando que está corriendo.
@bot.event
async def on_ready():
    print('Nos hemos conectado como {0.user}'.format(bot))

#Busca todos los cogs y los carga al iniciar
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")

#Creación de un estado que cambia cada 10 segundos
@bot.event
async def random_pr():
    await bot.wait_until_ready()
    statuses = [f'nya>help | v{config.VERSION}', f'rolear en {len(bot.guilds)} servidores']
    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(activity = discord.Game(name=status))
        await asyncio.sleep(10)
bot.loop.create_task(random_pr())

mention = ["satanya", "satanyabot"]
@bot.event
async def on_message(msg):
  if msg.author.bot:
    return
  if any(word in msg.content.lower() for word in mention):
   nya="<:SatanyaBot:832392370472484875>"
   await msg.add_reaction(nya)
  await bot.process_commands(msg)

#Sección de mantenimiento 24/7 encendido e iniciado del bot
load_dotenv()
bot.run(os.getenv('Token'))
