import discord
from discord.ext import commands
import os
import random
import asyncio
import config

#keep_alive: formato para mantener al bot activo 24/7 mediante un ping generado cada 5 min
from keep_alive import keep_alive

client = discord.Client()

#Prefijo de comando de discord.ext
client = commands.Bot(command_prefix="nya>")

client.load_extension("apis_commands")
client.load_extension("general_commands")

#on_ready: Cuando el bot esté activo y funcional mandará un mensaje confirmando que está corriendo.
@client.event
async def on_ready():
    print('Nos hemos conectado como {0.user}'.format(client))

#Creación de un estado que cambia cada 10 segundos
@client.event
async def random_pr():
    await client.wait_until_ready()
    statuses = [f'nya>help | v{config.VERSION}', f'a moderar en {len(client.guilds)} servidores', 'Discord.py']
    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(activity = discord.Game(name=status))
        await asyncio.sleep(10)
client.loop.create_task(random_pr())

hola = ["hola", "buenas", "wenas", "hello"]
adios = ["adiós", "adios", "bye", "chao"]
@client.event
async def on_message(msg):
  if any(word in msg.content.lower() for word in hola):
   await msg.add_reaction("👋")
  if any(word in msg.content.lower() for word in adios):
    await msg.add_reaction("🖐️")
  await client.process_commands(msg)

#Sección de mantenimiento 24/7 encendido e iniciado del bot
keep_alive()
client.run(os.getenv('Token'))
