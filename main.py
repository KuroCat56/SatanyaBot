# -*- coding: utf-8 -*-
import os
from datetime import datetime

import discord
from dotenv import load_dotenv

from utils import bot
from utils.bot import Bot, HelpCommand

load_dotenv()

bot = Bot(
    case_insensitive=True,
    command_attrs=dict(hidden=True),
    allowed_mentions=discord.AllowedMentions(
        roles=False, users=True, everyone=False, replied_user=True
    ),
    intents=discord.Intents(
        guilds=True,
        members=True,
        messages=True,
        message_content=True,
    ),
    activity=discord.Game(
        name=f'{os.environ["PREFIX"]}help | v{os.environ["VERSION"]} 🔲'
    ),
    help_command=HelpCommand(),
)
bot.launch_time = datetime.utcnow()


@bot.event
async def on_ready():
    print(f'Nos hemos conectado como {bot.user}')


load_dotenv()
bot.run(os.getenv('TOKEN'))
