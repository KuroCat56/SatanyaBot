from discord.ext import commands
import datetime
from os import getpid
from psutil import Process

delta_uptime = datetime.utcnow() - self.bot.launch_time
hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
minutes, seconds = divmod(remainder, 60)
days, hours = divmod(hours, 24)
uptime = (f"{days}d, {hours}h, {minutes}m, {seconds}s")

#Extraído de https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
class OwnerCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.reply(f'<:nope:846611758445625364> **`ERROR:`** {type(e).__name__} - {e}', mention_author=False)
        else:
            await ctx.reply(f'<:okay:846612389046386689> **`OKAY:`** He cargado *{cog}* correctamente.', mention_author=False)

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.reply(f'<:nope:846611758445625364> **`ERROR:`** {type(e).__name__} - {e}', mention_author=False)
        else:
            await ctx.reply(f'<:okay:846612389046386689> **`OKAY:`** He descargado __{cog}__ correctamente.', mention_author=False)

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.reply(f'<:nope:846611758445625364> **`ERROR:`** {type(e).__name__} - {e}', mention_author=False)
        else:
            await ctx.reply(f'<:okay:846612389046386689> **`OKAY:`** He recargado __{cog}__ correctamente.', mention_author=False)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def uptime(self, ctx):
        delta_uptime = datetime.utcnow() - self.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        uptime = (f"{days}d, {hours}h, {minutes}m, {seconds}s")
        await ctx.send(f'Llevo encendida desde hace: **{uptime}**')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def memory(self, ctx):
      await ctx.send(f'Estoy usando **{round(Process(getpid()).memory_info().rss/1024/1024, 2)} MB** en mi servidor.')

def setup(bot):
    bot.add_cog(OwnerCog(bot))
