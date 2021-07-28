import discord
from discord.ext import commands
from datetime import datetime
import os
import config
from dotenv import load_dotenv
from difflib import get_close_matches
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

bot = commands.Bot(command_prefix=get_prefix, intents=intents)
bot.launch_time = datetime.utcnow()

#Busca todos los cogs y los carga al iniciar
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    try:
      bot.load_extension(f"cogs.{filename[:-3]}")
    except Exception as error:
      print(f"Could not load {filename}: {error}")
print("COGS HAVE BEEN LOADED")

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

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        cmd = ctx.invoked_with
        cmds = [cmd.name for cmd in bot.commands if not cmd.hidden] # use this to stop showing hidden commands as suggestions
        matches = get_close_matches(cmd, cmds)
        if len(matches) > 0:
            await ctx.send(f'<:okaynt:846612437637660702> No encontré el comando **"{cmd}"**, ¿Quisiste decir **"{matches[0]}"**?', delete_after=10)
        else:
          await ctx.send(f'<:nope:846611758445625364> No encontré el comando **"{cmd}"**. Usa el comando de ayuda para saber que comandos están disponibles.', delete_after=10)

bot.snipes = {}

@bot.event
async def on_message_delete(message):
  bot.snipes[message.channel.id] = message
@bot.command()  
async def snipe(ctx, *, channel: discord.TextChannel = None):
  channel = channel or ctx.channel
  try:
    msg = bot.snipes[channel.id]
  except KeyError:
    return await ctx.send('Nothing to snipe!')
  # one liner, dont complain
  await ctx.send(embed=discord.Embed(description=msg.content, color=msg.author.color).set_author(name=str(msg.author), icon_url=str(msg.author.avatar_url)))

class MyNewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            await destination.send(embed=emby)

bot.help_command = MyNewHelp()
load_dotenv()
bot.run(os.getenv('Token'))
