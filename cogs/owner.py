import os
from os import getpid

import discord
from discord.ext import commands
from psutil import Process


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.snipes = {}

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx: commands.Context, name: str):
        """Carga un cog"""
        try:
            await self.bot.load_extension(f'cogs.{name}')
        except Exception as e:
            await ctx.reply(
                f'<:nope:846611758445625364> **`ERROR:`** {type(e).__name__} - {e}',
            )
        else:
            await ctx.reply(
                f'<:okay:846612389046386689> **`OKAY:`** He cargado __{name}__ correctamente.',
            )

    @commands.command(name='unload')
    @commands.is_owner()
    async def unload(self, ctx: commands.Context, name: str):
        """Descarga un cog"""
        try:
            await self.bot.unload_extension(f'cogs.{name}')
        except Exception as e:
            await ctx.reply(
                f'<:nope:846611758445625364> **`ERROR:`** {type(e).__name__} - {e}',
            )
        else:
            await ctx.reply(
                f'<:okay:846612389046386689> **`OKAY:`** He descargado __{name}__ correctamente.',
            )

    @commands.command(name='reload')
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, name: str):
        """Recarga un cog"""
        try:
            await self.bot.unload_extension(f'cogs.{name}')
            await self.bot.load_extension(f'cogs.{name}')
        except Exception as e:
            await ctx.reply(
                f'<:nope:846611758445625364> **`ERROR:`** {type(e).__name__} - {e}',
            )
        else:
            await ctx.reply(
                f'<:okay:846612389046386689> **`OKAY:`** He recargado __{name}__ correctamente.',
            )

    @commands.command(name='rall')
    @commands.is_owner()
    async def rall(self, ctx: commands.Context):
        """Recarga todos los cogs"""
        cogs = []
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    await self.bot.unload_extension(f'cogs.{filename[:-3]}')
                    await self.bot.load_extension(f'cogs.{filename[:-3]}')

                    cogs.append(f'{filename}')
                except Exception as error:
                    await ctx.reply(
                        f'<:nope:846611758445625364> Nope: {filename}: {error}',
                        mention_author=False,
                    )
        await ctx.reply(
            f'<:okay:846612389046386689> Recargué los siguientes cogs:\n {cogs}'
        )

    @commands.command()
    @commands.is_owner()
    async def memory(self, ctx: commands.Context):
        await ctx.send(
            f'Estoy usando **{round(Process(getpid()).memory_info().rss/1024/1024, 2)} MB** en mi servidor.'
        )

    # https://vcokltfre.dev/tutorial/09-snipe/
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.bot.snipes[message.channel.id] = message

    @commands.command(name='snipe')
    @commands.is_owner()
    async def snipe(self, ctx: commands.Context, *, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        try:
            msg = self.bot.snipes[channel.id]
        except KeyError:
            return await ctx.send('Nothing to snipe!')
        # one liner, dont complain
        await ctx.send(
            embed=discord.Embed(
                description=msg.content, color=msg.author.color
            ).set_author(
                name=str(msg.author), icon_url=str(msg.author.avatar.url)
            )
        )

    @commands.command()
    @commands.is_owner()
    async def serverlist(self, ctx: commands.Context):
        guilds = [guild.name for guild in self.bot.guilds]
        member_count = [guild.member_count for guild in self.bot.guilds]
        serverlist = dict(zip(guilds, member_count))
        output = '\n'.join(f'{k} ({v})' for k, v in serverlist.items())
        servers = discord.Embed(
            title=f'Servers ({len(guilds)})',
            description=output,
            colour=0xFBF9FA,
        )
        await ctx.send(embed=servers)

    @commands.command(name="logout", aliases=['close', 'stopbot'])
    @commands.is_owner()
    async def logout(self, ctx):
        await ctx.send('Okay, hora de reiniciar 💤💤💤')
        await self.bot.close()

    @commands.command(name="sync")
    @commands.is_owner()
    async def _sync(self, ctx: commands.Context):
        await self.bot.tree.sync()
        embed = discord.Embed(
            title="Sincronizado!",
            description="El arbol de commandos se ha sincronizado exitosamente",
            colour=0xFBF9FA,
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Owner(bot))
