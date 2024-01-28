import os
from datetime import datetime
import discord
from dotenv import load_dotenv
from utils.bot import Bot, HelpCommand
import asyncio

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = Bot(
    case_insensitive=True,
    command_attrs=dict(hidden=True),
    allowed_mentions=discord.AllowedMentions(
        roles=False, users=True, everyone=False, replied_user=True
    ),
    intents=intents,
    help_command=HelpCommand(),
)
bot.launch_time = datetime.utcnow()


async def dynamic_activity():
    presences = [
        discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers"
                         ),
        discord.Activity(type=discord.ActivityType.streaming, name=f"v{os.environ['VERSION']}",
                         url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
        discord.Activity(type=discord.ActivityType.listening, name=f"{os.environ['PREFIX']}help")
    ]
    current = 0
    while True:
        await bot.change_presence(activity=presences[current])
        current = (current + 1) % len(presences)
        await asyncio.sleep(10)


@bot.event
async def on_ready():
    print(f'Nos hemos conectado como {bot.user}')
    await bot.loop.create_task(dynamic_activity())


if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))
