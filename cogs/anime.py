import discord
from discord.ext import commands

class anime(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 10, commands.BucketType.user)}):
    """
    Comandos relacionados a cosas de anime.
    
    Cooldown: 10s per command
    """
    def __init__(self, bot: commands.Bot):
      self.bot = bot


def setup(bot: commands.Bot):
    bot.add_cog(anime(bot))