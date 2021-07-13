from discord.ext import commands
import datetime
from os import getpid
from psutil import Process
import general

#Extraído de https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
class OwnerCog(commands.Cog):

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
    async def alive(self, ctx):
        await ctx.send(f'Llevo encendida desde hace: **{general.uptime}**')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def memory(self, ctx):
      await ctx.send(f'Estoy usando **{round(Process(getpid()).memory_info().rss/1024/1024, 2)} MB** en mi servidor.')

    @commands.command()
    @commands.is_owner()
    async def lines(self, ctx):
        await ctx.send(f"**{self.bot.user.name}** was made with **{general.lines}** lines of code!")

def setup(bot):
    bot.add_cog(OwnerCog(bot))
