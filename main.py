import discord
import os
import requests
import json
import random
#keep_alive: formato para mantener al bot activo 24/7 mediante un ping generado cada 5 min
from keep_alive import keep_alive

client = discord.Client()

#lista de palabras triggers en un mensaje común que hacen trigger al bot 
hola = ["hola", "buenas", "wenas", "hi", "hello"]
readHola = open("hello_list.txt")

#Zenquotes api para experimentar con las api
#q = quote ; a = author
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = "**" + json_data[0]['q'] + "**" + " -" + "*" + json_data[0]['a'] + "*"
  return(quote)

#on_ready: Cuando el bot esté activo y funcional mandará un mensaje confirmando que está corriendo.
@client.event
async def on_ready():
  print('Nos hemos conectado como {0.user}'.format(client))
  #Genera el estado de "Jugando" con la descripción name=''
  await client.change_presence(activity=discord.Game(name='>nya'))


@client.event
#on_message: Cuando recibe un mensaje, actúa si el mensaje es de otro miembro y no del propio bot.
async def on_message(message):
  if message.author == client.user:
    return
  # variable msg para acortar 
  msg = message.content
#.startwith: El trigger que lee el bot para reaccionar según el comando especificado
  if msg.startswith('>quote'):
    quote = get_quote()
    await message.channel.send(quote)
#Sección de trigger para saludar
  if any (word in msg.lower() for word in hola):
    await message.channel.send(readHola.readline())
keep_alive()
client.run(os.getenv('Token'))