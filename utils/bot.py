import os

import discord
from discord.ext.commands import (
    AutoShardedBot,
    MinimalHelpCommand,
    when_mentioned_or,
)


def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['nya>', 'nya', '>>', f'{os.environ["PREFIX"]}']

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return when_mentioned_or(*prefixes)(bot, message)


class Bot(AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(command_prefix=get_prefix, *args, **kwargs)

    async def setup_hook(self):
        for file in os.listdir('cogs'):
            if file.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{file[:-3]}')
                except Exception as e:
                    print(f"Cannot load {file}: {e}")

    async def on_message(self, msg):
        if not self.is_ready() or msg.author.bot or not msg.guild:
            return

        await self.process_commands(msg)


class HelpCommand(MinimalHelpCommand):
    color = 0xFBF9FA
    NEWS = 'Ya me puedes encontrar en top.gg (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧\n'

    def footer(self):
        return f'{self.context.clean_prefix}{self.invoked_with} [comando] para más información.'

    def get_command_signature(self, command):
        return f'```fix\n{self.context.clean_prefix}{command.qualified_name} {command.signature}\n```'

    async def send_cog_help(self, cog):
        embed = discord.Embed(
            title=f'__**Comandos {cog.qualified_name}**__', color=self.color
        )
        if cog.description:
            embed.description = cog.description

        filtered = await self.filter_commands(cog.get_commands(), sort=True)
        for command in filtered:
            embed.add_field(
                name=command.qualified_name,
                value=command.short_doc or 'Sin descripción',
            )

        embed.set_footer(text=self.footer())
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(title=command.qualified_name, color=self.color)
        if command.help:
            embed.description = command.help

        embed.add_field(name='Uso', value=self.get_command_signature(command))
        await self.get_destination().send(embed=embed)

    async def send_bot_help(self, mapping):
        block = '`' * 3
        embed = discord.Embed(color=self.color)
        embed.set_author(
            name=f'🌸 Menú de ayuda 🌸| v{os.environ["VERSION"]}',
            icon_url='https://media.discordapp.net/attachments/829223734559637545/859941157944557588/headAsset_214x-8.png',
        )
        description = f'{block}fix\n{self.NEWS}\n{block}\n> *Si tienes algún problema consulta en https://discord.gg/bqcdKxuW3X*\n'
        embed.set_image(
            url='https://cdn.discordapp.com/attachments/829223734559637545/866011691123736606/cherry.png'
        )
        if description:
            embed.description = description

        for cog, commands in mapping.items():
            if not cog:
                continue
            filtered = await self.filter_commands(commands, sort=True)
            if filtered:
                value = '\t'.join(f'`{i.name}`' for i in commands)
                embed.add_field(
                    name=cog.qualified_name, value=value, inline=False
                )
        embed.set_footer(text=self.footer())
        await self.get_destination().send(embed=embed)
