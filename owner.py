from discord.ext import commands
import datetime
from os import getpid
from psutil import Process
import discord
import os


# Extraído de https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
class OwnerCog(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot
        bot.snipes = {}

    # Hidden means it won't show up on the default help.
    @commands.command(name="load")
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            await self.bot.load_extension(cog)
        except Exception as e:
            await ctx.reply(
                f"<:nope:846611758445625364> **`ERROR:`** {type(e).__name__} - {e}",
                mention_author=False,
            )
        else:
            await ctx.reply(
                f"<:okay:846612389046386689> **`OKAY:`** He cargado *{cog}* correctamente.",
                mention_author=False,
            )

    @commands.command(name="unload")
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            await self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.reply(
                f"<:nope:846611758445625364> **`ERROR:`** {type(e).__name__} - {e}",
                mention_author=False,
            )
        else:
            await ctx.reply(
                f"<:okay:846612389046386689> **`OKAY:`** He descargado __{cog}__ correctamente.",
                mention_author=False,
            )

    @commands.command(name="reload")
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            await self.bot.unload_extension(cog)
            await self.bot.load_extension(cog)
        except Exception as e:
            await ctx.reply(
                f"<:nope:846611758445625364> **`ERROR:`** {type(e).__name__} - {e}",
                mention_author=False,
            )
        else:
            await ctx.reply(
                f"<:okay:846612389046386689> **`OKAY:`** He recargado __{cog}__ correctamente.",
                mention_author=False,
            )

    @commands.command(name="rall")
    @commands.is_owner()
    async def rall(self, ctx):
        """Recarga todos los cogs"""
        cogs = []
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                try:
                    await self.bot.unload_extension(f"cogs.{filename[:-3]}")
                    await self.bot.load_extension(f"cogs.{filename[:-3]}")

                    cogs.append(f"{filename}")
                except Exception as error:
                    await ctx.reply(
                        f"<:nope:846611758445625364> Nope: {filename}: {error}",
                        mention_author=False,
                    )
        await ctx.reply(
            f"<:okay:846612389046386689> Recargué los siguientes cogs:\n {cogs}",
            mention_author=False,
        )

    @commands.command()
    @commands.is_owner()
    async def memory(self, ctx):
        await ctx.send(
            f"Estoy usando **{round(Process(getpid()).memory_info().rss/1024/1024, 2)} MB** en mi servidor."
        )

    # https://vcokltfre.dev/tutorial/09-snipe/
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.bot.snipes[message.channel.id] = message

    @commands.command(name="snipe")
    @commands.is_owner()
    async def snipe(self, ctx, *, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        try:
            msg = self.bot.snipes[channel.id]
        except KeyError:
            return await ctx.send("Nothing to snipe!")
        # one liner, dont complain
        await ctx.send(
            embed=discord.Embed(
                description=msg.content, color=msg.author.color
            ).set_author(name=str(msg.author), icon_url=str(msg.author.avatar_url))
        )

    @commands.command()
    @commands.is_owner()
    async def serverlist(self, ctx):
        guilds = [guild.name for guild in self.bot.guilds]
        member_count = [guild.member_count for guild in self.bot.guilds]
        serverlist = dict(zip(guilds, member_count))
        output = "\n".join(f"{k} ({v})" for k, v in serverlist.items())
        servers = discord.Embed(
            title=f"Servers ({len(guilds)})",
            description=output,
            colour=0xFBF9FA,
        )
        await ctx.send(embed=servers)

    @commands.command(aliases=["disconnect", "close", "stopbot"])
    @commands.is_owner()
    async def logout(self, ctx):
        await ctx.send("Okay, hora de reiniciar 💤💤💤")
        await self.bot.logout()


async def setup(bot):
    await bot.add_cog(OwnerCog(bot))
