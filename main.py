import discord
from discord.ext import commands
from datetime import datetime
import os
import config
from dotenv import load_dotenv
intents = discord.Intents.default()
intents.members = True

#Extraído de https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['nya>', 'nya ', '>>']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '>>'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)

bot = commands.Bot(command_prefix=get_prefix, intents=intents, allowed_mentions=discord.AllowedMentions=(roles=False, users=True, everyone=False, replied_user=True))
bot.launch_time = datetime.utcnow()

#Busca todos los cogs y los carga al iniciar
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    try:
      bot.load_extension(f"cogs.{filename[:-3]}")
    except Exception as error:
      print(f"Could not load {filename}: {error}")
print("COGS HAVE BEEN LOADED")

#on_ready: Cuando el bot esté activo y funcional mandará un mensaje confirmando que está corriendo.
@bot.event
async def on_ready():
    print('Nos hemos conectado como {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name=f'nya>help | v{config.VERSION} 🔲'))

load_dotenv()
bot.run(os.getenv('Token'))
