import discord
import os
import requests
import json
import random
#keep_alive: formato para mantener al bot activo 24/7 mediante un ping generado cada 5 min
from keep_alive import keep_alive

client = discord.Client()

#lista de palabras en un mensaje común que hacen trigger al bot 
sad_words = ["triste", "depresivo", "mal", "depresión"]

#lista de respuestas a los triggers de sad_words
starter_encouragments = [
  "¡No te preocupes! Estamos aquí para apoyarte.",
  "¿Te sientes desanimado? Prueba a descansar un poco haciendo algo que te guste.",
  "¿Te sientes mal? Toma, un chocolate para ti 🍫",
]

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

@client.event
#on_message: Cuando recibe un mensaje, actúa si el mensaje es de otro miembro y no del propio bot.
async def on_message(message):
  if message.author == client.user:
    return
  # variable msg para acortar 
  msg = message.content
#.startwith: El trigger que lee el bot para reaccionar.
  if msg.startswith('>quote'):
    quote = get_quote()
    await message.channel.send(quote)
  if any (word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragments))
keep_alive()
client.run(os.getenv('Token'))