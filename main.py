import discord
from discord.ext import commands
import os
import requests
import json
import random

#keep_alive: formato para mantener al bot activo 24/7 mediante un ping generado cada 5 min
from keep_alive import keep_alive

client = discord.Client()

#Prefijo de comando de discord.ext
client = commands.Bot(command_prefix="nya>")

#on_ready: Cuando el bot esté activo y funcional mandará un mensaje confirmando que está corriendo.
@client.event
async def on_ready():
    print('Nos hemos conectado como {0.user}'.format(client))
    #Genera el estado de "Jugando" con la descripción name=''
    await client.change_presence(activity=discord.Game(name='nya>help | v0.1.2'))

#Comando de test/ping
@client.command()
async def ping(ctx):
  await ctx.send(f'Pong {round(client.latency * 1000)}ms')

#API de Zenquotes
#q = quote ; a = author
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = "**" + json_data[0]['q'] + "**" + " -" + json_data[0]['a']
    return (quote)

@client.command()
async def quo(ctx):
  quote = get_quote()
  await ctx.send(quote)

#API de Kaomojis
def get_kao():
    response = requests.get("http://kaomoji.n-at.me/random.json")
    json_data = json.loads(response.text)
    kaomoji = json_data['record']['text']
    return (kaomoji)

@client.command()
async def kao(ctx):
  kao = get_kao()
  await ctx.send(kao)


#Sección de trigger para saludar y despedir
#lista de palabras triggers en un mensaje común que hacen trigger al bot
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
