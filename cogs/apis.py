import aiohttp
from discord.ext import commands
import discord
import secrets
import alexflipnote


class apis(
    commands.Cog,
    command_attrs={
        "cooldown": commands.CooldownMapping.from_cooldown(
            1, 5, commands.BucketType.user
        )
    },
):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.alex = alexflipnote.Client()
        self.session = aiohttp.ClientSession()

    # Comando que envía quotes
    @commands.command(name="quo")
    async def quo(self, ctx: commands.Context):
        """
        Cuidado con las crisis existenciales.
        """
        async with ctx.typing() and self.session.get(
            "https://zenquotes.io/api/random"
        ) as r:
            data = await r.json()
            quote_em = data[0]["q"]
            author_em = data[0]["a"]
            embed = discord.Embed(
                title=f"{quote_em}", description=f"-{author_em}", color=0xFBF9FA
            )
            embed.set_footer(text="Powered by zenquotes.io")
        await ctx.send(embed=embed)

    # Comando que envía kaomojis
    @commands.command(name="kao")
    async def kao(self, ctx: commands.Context):
        """
        ( ˆᴗˆ  )
        """
        async with ctx.typing() and self.session.get(
            "http://kaomoji.n-at.me/random.json"
        ) as r:
            data = await r.json()
            kao = data["record"]["text"]
        await ctx.reply(kao)

    #    @commands.command(name="emojify")
    #    async def emojify(self, ctx):
    #        """
    #        🇪 🇲 🇴 🇯 🇮 🇸
    #        """
    #        async with ctx.typing() and self.session.get(
    #            f"https://normal-api.ml/emojify?text={message}"
    #        ) as r:
    #            message = ctx.message.content
    #            if message.content > 2000:
    #                return
    #            message = message.lstrip(f"emojify>>nya>@{self.bot.name}")

    #            data = await r.json()
    #            emojify = data["emojify"]

    #        await ctx.reply(emojify, delete_after=10)

    @commands.command(name="eevee")
    async def eevee(self, ctx):
        """
        ¿Te gustan los Eevees?
        """
        async with ctx.typing() and self.session.get(
            "https://purrbot.site/api/img/sfw/eevee/gif"
        ) as r:
            data = await r.json()
            eevee = data["link"]
            embed = discord.Embed(color=0xAF6357)
            embed.set_image(url=f"{eevee}")
            embed.set_footer(
                text="Powered by PurrBotAPI",
                icon_url="https://docs.purrbot.site/assets/img/logo.png",
            )
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(name="fox", aliases=["floof"])
    async def randomfox(self, ctx: commands.Context):
        """
        Imágenes aleatorias de zorros. 🦊
        """
        async with ctx.typing() and self.session.get("https://randomfox.ca/floof") as r:
            data = await r.json()
            fox = data["image"]

        em_fox = discord.Embed(color=0xF98626)
        em_fox.set_image(url=fox)
        em_fox.set_footer(text="🦊 Powered by randomfox.ca")
        await ctx.reply(embed=em_fox, mention_author=False)

    @commands.command(name="dog", aliases=["woof"])
    async def randomdog(self, ctx: commands.Context):
        """
        Imágenes aleatorias de perros. 🐶
        """
        dog = self.alex.dogs()
        em_dog = discord.Embed(color=0xC77768)
        em_dog.set_image(url=dog)
        em_dog.set_footer(text="🐶 Powered by api.alexflipnote.dev")
        await ctx.reply(embed=em_dog, mention_author=False)

    @commands.command(name="cat", aliases=["meow"])
    async def randomcat(self, ctx: commands.Context):
        """
        Imágenes aleatorias de gatos. 🐱
        """
        cat = self.alex.cats()
        em_cat = discord.Embed(color=0xFFD356)
        em_cat.set_image(url=cat)
        em_cat.set_footer(text="🐱 Powered by api.alexflipnote.dev")
        await ctx.reply(embed=em_cat, mention_author=False)

    @commands.command(name="shiba", aliases=["inu"])
    async def randomshiba(self, ctx: commands.Context):
        """
        Imágenes aleatorias de shibas inu. 🐕
        """
        async with ctx.typing() and self.session.get(
            "https://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true"
        ) as r:
            data = await r.json()
            shiba = data[0]
        em_shiba = discord.Embed(color=0xF6C436)
        em_shiba.set_image(url=shiba)
        em_shiba.set_footer(text="🐕 Powered by shibe.online")
        await ctx.reply(embed=em_shiba, mention_author=False)


async def setup(bot: commands.Bot):
    await bot.add_cog(apis(bot))
