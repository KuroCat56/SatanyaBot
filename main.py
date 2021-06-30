import discord
from discord.ext import commands
from datetime import datetime
import os
import random
import asyncio
import config
from dotenv import load_dotenv
from psutil import Process
from os import getpid
import sys, traceback

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['nya>', 'nya ', '>']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '>>'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)

bot = commands.Bot(command_prefix=get_prefix)
bot.launch_time = datetime.utcnow()

#Busca todos los cogs y los carga al iniciar
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")

mention = ["satanya", "satanyabot"]
@bot.event
async def on_message(msg):
  if msg.author.bot:
    return
  if any(word in msg.content.lower() for word in mention):
   nya="<:SatanyaBot:858480664143331338>"
   await msg.add_reaction(nya)
  await bot.process_commands(msg)

#on_ready: Cuando el bot esté activo y funcional mandará un mensaje confirmando que está corriendo.
@bot.event
async def on_ready():
    print('Nos hemos conectado como {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name=f'nya>help | v{config.VERSION} 🔲'))

class MyNewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            await destination.send(embed=emby)

bot.help_command = MyNewHelp()
load_dotenv()
bot.run(os.getenv('Token'))
