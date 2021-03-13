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
bot = commands.Bot(command_prefix="nya>")

#on_ready: Cuando el bot esté activo y funcional mandará un mensaje confirmando que está corriendo.
@client.event
async def on_ready():
    print('Nos hemos conectado como {0.user}'.format(client))
    #Genera el estado de "Jugando" con la descripción name=''
    await client.change_presence(activity=discord.Game(name='nya>help | v0.1.2'))

#Zenquotes api para experimentar con las api
#q = quote ; a = author
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = "**" + json_data[0]['q'] + "**" + " -" + json_data[0]['a']
    return (quote)

def get_kao():
    response = requests.get("http://kaomoji.n-at.me/random.json")
    json_data = json.loads(response.text)
    kaomoji = json_data['record']['text']
    return (kaomoji)


#Sección de trigger para saludar y despedir
#lista de palabras triggers en un mensaje común que hacen trigger al bot
hola = ["hola", "buenas", "wenas", "hello"]
adios = ["adiós", "adios", "bye", "chao"]

@client.event
async def on_message(msg):
  if any(word in msg.lower() for word in hola):
   await msg.content.add_reaction("👋")
  if any(word in msg.lower() for word in adios):
    await msg.content.add_reaction("🖐️")
await client.process_commands(msg)

@commands.comand()
async def quo(ctx):
    quote = get_quote()
    await message.channel.send(quote)
    
    
#if msg.startswith('>kao'):
        kaomoji = get_kao()
        await message.channel.send(kaomoji)


#Sección de mantenimiento 24/7 encendido e iniciado del bot
keep_alive()
client.run(os.getenv('Token'))
