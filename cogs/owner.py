from discord.ext import commands
import datetime
from os import getpid
from psutil import Process

def lines_of_code():
    """
    I did not write this code.
    This code was taken off of a tag in discord.gg/dpy owned by Dutchy#6127
    I don't know if this is licensed
    but alas
    :return:
    """
    import pathlib
    p = pathlib.Path('./')
    cm = cr = fn = cl = ls = fc = 0
    for f in p.rglob('*.py'):
        if str(f).startswith("venv"):
            continue
        fc += 1
        with f.open() as of:
            for l in of.readlines():
                l = l.strip()
                if l.startswith('class'):
                    cl += 1
                if l.startswith('def'):
                    fn += 1
                if l.startswith('async def'):
                    cr += 1
                if '#' in l:
                    cm += 1
                ls += 1
    return {
        "comments": cm,
        "coroutine": cr,
        "functions": fn,
        "classes": cl,
        "lines": ls,
        "files": fc
    }

lines = lines_of_code()

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
    async def alive(self, ctx):
        delta_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        alive = (f"{days}d, {hours}h, {minutes}m, {seconds}s")
        await ctx.send(f'Llevo encendida desde hace: **{alive}**')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def memory(self, ctx):
      await ctx.send(f'Estoy usando **{round(Process(getpid()).memory_info().rss/1024/1024, 2)} MB** en mi servidor.')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def lines(self, ctx):
        await ctx.send(f"Estoy hecha con {lines.get('lines'):,} líneas de código.")

    @commands.command(hidden=True)
    @commands.is_owner()
    async def commandstats(self, ctx, limit=20):
        """Shows command stats.
        Use a negative number for bottom instead of top.
        This is only for the current session.
        """
        counter = self.bot.command_stats
        width = len(max(counter, key=len))
        total = sum(counter.values())

        if limit > 0:
            common = counter.most_common(limit)
        else:
            common = counter.most_common()[limit:]

        output = '\n'.join(f'{k:<{width}}: {c}' for k, c in common)

        await ctx.send(f'```\n{output}\n```')

def setup(bot):
    bot.add_cog(OwnerCog(bot))
