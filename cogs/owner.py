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
    async def clear(self, ctx, number: int):
        counter = 0
        async for message in ctx.channel.history(limit=100):
            if message.author.id == ctx.bot.user.id:
                await message.delete()
                counter += 1
            if counter >= number:
                break
        await ctx.send(f"🧹 He borrado `{number}` de mis mensajes en este canal.")

    @commands.command(hidden=True)
    @commands.is_owner()
    async def memory(self, ctx):
      await ctx.send(f'Estoy usando **{round(Process(getpid()).memory_info().rss/1024/1024, 2)} MB** en mi servidor.')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def lines(self, ctx):
        await ctx.send(f"Estoy hecha con {lines.get('lines'):,} líneas de código.")

def setup(bot):
    bot.add_cog(OwnerCog(bot))
