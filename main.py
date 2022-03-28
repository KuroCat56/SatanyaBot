# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from datetime import datetime
import os
from cogs.help import HelpCommand
import config
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True

# Extraído de https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ["nya>", "nya ", ">>"]

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return ">>"

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)
bot = commands.AutoShardedBot(
    case_insensitive=True,
    command_prefix=get_prefix,
    command_attrs=dict(hidden=True),
    allowed_mentions=discord.AllowedMentions(
        roles=False, users=True, everyone=False, replied_user=True
    ),
    intents=discord.Intents(
        guilds=True, members=True, messages=True, message_content=True
    ),
    activity=discord.Game(name=f"{config.PREFIX}help | v{config.VERSION} 🔲"),
    help_command=HelpCommand(),
)
bot.launch_time = datetime.utcnow()


async def load():
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            name = file[:-3]
            await bot.load_extension(f"cogs.{name}")


# on_ready: Cuando el bot esté activo y funcional mandará un mensaje confirmando que está corriendo.
@bot.event
async def on_ready():
    await load()
    print(f"Nos hemos conectado como {bot.user}")


load_dotenv()
bot.run(os.getenv("TOKEN"))
