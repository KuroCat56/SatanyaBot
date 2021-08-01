import discord
from discord.ext import commands

class HelpCommand(commands.helpCommand):
    color = 0xfbf9fa

    def footer(self):
      return f"{self.clean_prefix}{self.invoked_with} [comando] para más información."

    def get_command_signature(self, command):
      return f"```{self.clean_prefix}{command.qualified_name} {command.signature}```"
    
    async def send_cog_help(self, cog):
      embed = discord.Embed(title=f"**{cog.qualified_name}** Comandos", color = self.color)
      if cog.description:
        embed.description = cog.description
      
      filtered = await self.filter_commands(cog.get_commands(), sort=True)
      for command in filtered:
        embed.add_field(name=command.qualified_name, value=command.short_doc or "No description")
      
      embed.set_footer(text=self.footer())
      await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
      embed = discord.Embed(title=command.qualified_name, color = self.color)
      if command.help:
        embed.description = command.help
      
      embed.add_field(name="Signature", value=self.get_command_signature(command))
      embed.set_footer(text=self.footer())
      await self.get_destination().send(embed=embed)

    async def send_bot_help(self, mapping):
      embed = discord.Embed(title="Bot commands", color=self.color)
      description = self.context.bot.description
      if description:
        embed.description = description
      
      for cog, commands in mapping.items():
        if not cog:
          continue
        filtered = await self.filter_commands(commands, sort = True)
        if filtered:
          value = "\t".join(f"`{i.name}`" for i in commands)
          embed.add_field(name = cog.qualified_name, value = value)
      embed.set_footer(text=self.footer())
      await self.get_destination().send(embed=embed)

def setup(bot):
  bot.help_command = HelpCommand() 