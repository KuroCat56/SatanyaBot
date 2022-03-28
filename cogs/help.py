import discord
from discord.ext import commands
import config


class HelpCommand(commands.HelpCommand):
    color = 0xFBF9FA
    NEWS = "Ya me puedes encontrar en top.gg (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧\n"

    def footer(self):
        return f"{self.context.clean_prefix}{self.invoked_with} [comando] para más información."

    def get_command_signature(self, command):
        return f"```fix\n{self.context.clean_prefix}{command.qualified_name} {command.signature}\n```"

    async def send_cog_help(self, cog):
        embed = discord.Embed(
            title=f"__**Comandos {cog.qualified_name}**__", color=self.color
        )
        if cog.description:
            embed.description = cog.description

        filtered = await self.filter_commands(cog.get_commands(), sort=True)
        for command in filtered:
            embed.add_field(
                name=command.qualified_name,
                value=command.short_doc or "Sin descripción",
            )

        embed.set_footer(text=self.footer())
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(title=command.qualified_name, color=self.color)
        if command.help:
            embed.description = command.help

        embed.add_field(name="Uso", value=self.get_command_signature(command))
        # embed.set_footer(text=self.footer())
        await self.get_destination().send(embed=embed)

    async def send_bot_help(self, mapping):
        block = "`" * 3
        embed = discord.Embed(color=self.color)
        embed.set_author(
            name=f"🌸 Menú de ayuda 🌸| v{config.VERSION}",
            icon_url="https://media.discordapp.net/attachments/829223734559637545/859941157944557588/headAsset_214x-8.png?width=465&height=473",
        )
        description = f"{block}fix\n{self.NEWS}\n{block}\n> *Si tienes algún problema consulta en https://discord.gg/bqcdKxuW3X*\n"
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/829223734559637545/866011691123736606/cherry.png"
        )
        if description:
            embed.description = description

        for cog, commands in mapping.items():
            if not cog:
                continue
            filtered = await self.filter_commands(commands, sort=True)
            if filtered:
                value = "\t".join(f"`{i.name}`" for i in commands)
                embed.add_field(name=cog.qualified_name, value=value, inline=False)
        embed.set_footer(text=self.footer())
        await self.get_destination().send(embed=embed)


async def setup(bot):
    bot.help_command = HelpCommand()
