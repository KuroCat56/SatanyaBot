import aiohttp
import discord
from discord.ext import commands
from nekos import NekosLifeClient, SFWImageTags


class rol(
    commands.Cog,
    command_attrs={
        'cooldown': commands.CooldownMapping.from_cooldown(
            1, 5, commands.BucketType.user
        )
    },
):

    """
    Reacciones de anime para rol y cosas divertidas.
    Ten en cuenta que para algunos comandos tendrás que etiquetar a otros ||o puedes probar y no hacerlo para ver que pasa||.

    Cooldown: 5s per command
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
        self.nekos = NekosLifeClient()

    @commands.command(name='hug')
    async def hug(self, ctx, member: discord.Member = None):
        """
        ¡Abrazos virtuales!
        """
        if member is ctx.author:
            message = '¡No puedes abrazarte a tí mismo!\nAunque puedo darte un abrazo si quieres ヽ(・∀・)ﾉ'
            await ctx.reply(message)
        elif member is None:
            await ctx.reply('¡Primero necesitas etiquetar a alguien!')
        else:
            async with ctx.typing():
                hug = await self.nekos.image(SFWImageTags.HUG)
                embed = discord.Embed(
                    description=f'🤗 ¡**{ctx.author.name}** ha abrazado a **{member.name}**!',
                    color=discord.Colour.random(),
                )
                embed.set_image(url=hug.url)
                embed.set_footer(text='Powered by nekos.life')
                await ctx.send(embed=embed)

    @commands.command(name='bite', aliases=['ñam'])
    async def bite(self, ctx, member: discord.Member = None):
        """
        Ñam ñam ñam~
        """
        if member is ctx.author:
            message = '¡No puedes morderte a tí mismo!\nY yo no tengo ganas de morder a nadie (´Д｀υ)'
            await ctx.reply(message)
        elif member is None:
            await ctx.reply('¡Primero necesitas etiquetar a alguien!')
        else:
            async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/bite'
            ) as r:
                data = await r.json()
                bite = data['url']
                embed = discord.Embed(
                    description=f'😏 ¡**{ctx.author.name}** ha mordido a **{member.name}**!',
                    color=discord.Colour.random(),
                )
                embed.set_image(url=f'{bite}')
                embed.set_footer(text='Powered by waifu.pics')
            await ctx.send(embed=embed)

    @commands.command(name='dance', aliases=['party'])
    async def dance(self, ctx, member: discord.Member = None):
        """
        ¡Esto hay que celebrarlo!
        """
        async with ctx.typing() and self.session.get(
            'https://api.waifu.pics/sfw/dance'
        ) as r:
            data = await r.json()
            dance = data['url']
            if member is ctx.author:
                desc = f'🎉 ¡**{ctx.author.name}** se ha puesto a bailar!'
            else:
                desc = f'🎊 ¡**{ctx.author.name}** y **{member.name}** están bailando juntos!'
            embed = discord.Embed(
                description=f'{desc}', color=discord.Colour.random()
            )
            embed.set_image(url=f'{dance}')
            embed.set_footer(text='Powered by waifu.pics')
            await ctx.send(embed=embed)

    @commands.command(name='pat', aliases=['headpat'])
    async def pat(self, ctx, member: discord.Member = None):
        """
        ¿Alguien se merece unos pat-pat?
        """
        if member is ctx.author:
            message = '¡No puedes darte pat-pats a tí mismo!\nPero puede darme unos a mí (o´▽`o)'
            await ctx.reply(message)
        elif member is None:
            await ctx.reply('¡Primero necesitas etiquetar a alguien!')
        else:
            async with ctx.typing():
                pat = await self.nekos.image(SFWImageTags.PAT)
                embed = discord.Embed(
                    description=f'❣️ **{ctx.author.name}** le ha dado unos pat-pats a **{member.name}**',
                    color=discord.Colour.random(),
                )
                embed.set_image(url=pat.url)
                embed.set_footer(text='Powered by nekos.life')
            await ctx.send(embed=embed)

    @commands.command(name='cuddle')
    async def cuddle(self, ctx, member: discord.Member = None):
        """
        Abrazos pero con más cariño~
        """
        if member is ctx.author:
            message = '¡No puedes darte cariños a tí mismo!\nPero puede darme unos a mí (o´▽`o)'
            await ctx.reply(message)
        elif member is None:
            await ctx.reply('¡Primero necesitas etiquetar a alguien!')
        else:
            async with ctx.typing():
                cuddle = await self.nekos.image(SFWImageTags.CUDDLE)
                embed = discord.Embed(
                    description=f'💞 **{ctx.author.name}** abraza con mucho cariño a **{member.name}**',
                    color=discord.Colour.random(),
                )
                embed.set_image(url=cuddle.url)
                embed.set_footer(text='Powered by nekos.life')
                await ctx.send(embed=embed)

    @commands.command(name='slap')
    async def slap(self, ctx, member: discord.Member = None):
        """
        Porque a veces alguien necesita una cachetada (con cariño)
        """
        if member is ctx.author:
            message = (
                '¡No puedes pegarte a tí mismo!\nA no ser que te guste...'
            )
            await ctx.reply(message)
        elif member is None:
            await ctx.reply('¡Primero necesitas etiquetar a alguien!')
        else:
            async with ctx.typing():
                slap = await self.nekos.image(SFWImageTags.SLAP)
                embed = discord.Embed(
                    description=f'💢 **{ctx.author.name}** ha cacheteado a **{member.name}**',
                    color=discord.Colour.random(),
                )
                embed.set_image(url=slap.url)
                embed.set_footer(text='Powered by nekos.life')
            await ctx.send(embed=embed)

    @commands.command(name='tickle')
    async def tickle(self, ctx, member: discord.Member = None):
        """
        Para molestar a los que tienen cosquillas
        """
        if member is ctx.author:
            message = '¡No puedes darte cosquillas a tí mismo!\nAunque puedo darte algunos si quieres (─‿‿─)'
            await ctx.reply(message)
        elif member is None:
            await ctx.reply('¡Primero necesitas etiquetar a alguien!')
        else:
            async with ctx.typing():
                tickle = await self.nekos.image(SFWImageTags.TICKLE)
                embed = discord.Embed(
                    description=f'🤣 ¡**{ctx.author.name}** le hace cosquillas a **{member.name}!**',
                    color=discord.Colour.random(),
                )
                embed.set_image(url=tickle.url)
                embed.set_footer(text='Powered by nekos.life')
            await ctx.send(embed=embed)

    @commands.command(name='poke')
    async def poke(self, ctx, member: discord.Member = None):
        """
        ¿Quieres llamar la atención de alguien?
        """
        if member is ctx.author:
            message = '¡No puedes molestarte a tí mismo!'
            await ctx.reply(message)
        elif member is None:
            await ctx.reply('¡Primero necesitas etiquetar a alguien!')

        else:
            async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/poke'
            ) as r:
                data = await r.json()
                poke = data['url']
                embed = discord.Embed(
                    description=f'👉 **{ctx.author.name}** está molestando a **{member.name}**',
                    color=discord.Colour.random(),
                )
                embed.set_image(url=f'{poke}')
                embed.set_footer(text='Powered by waifu.pics')
            await ctx.send(embed=embed)

    @commands.command(name='blush')
    async def blush(self, ctx):
        """
        Rojo como tomate
        """
        async with ctx.typing() and self.session.get(
            'https://api.waifu.pics/sfw/blush'
        ) as r:
            data = await r.json()
            blush = data['url']
            embed = discord.Embed(
                description=f'😳 **{ctx.author.name}** se ha puesto rojo como tomate',
                color=discord.Colour.random(),
            )
            embed.set_image(url=f'{blush}')
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)

    @commands.command(name='cry', aliases=['sad'])
    async def cry(self, ctx):
        """
        :(
        """
        async with ctx.typing() and self.session.get(
            'https://api.waifu.pics/sfw/cry'
        ) as r:
            data = await r.json()
            cry = data['url']
            embed = discord.Embed(
                description=f'😭 **{ctx.author.name}** está llorando. Que alguien le consuele :(',
                color=discord.Colour.random(),
            )
            embed.set_image(url=f'{cry}')
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)

    @commands.command(name='kiss')
    async def kiss(self, ctx, member: discord.Member = None):
        """
        ¿Son pareja? A ver, bésense
        """
        if member is ctx.author:
            message = '¡No puedes besarte a tí mismo!\nA no ser que uses algún espejo o algo parecido (￣▽￣*)ゞ'
            await ctx.reply(message)
        elif member is None:
            await ctx.reply('¡Primero necesitas etiquetar a alguien!')
        else:
            kiss = await self.nekos.image(SFWImageTags.KISS)
            async with ctx.typing():
                embed = discord.Embed(
                    description=f'💖 **{ctx.author.name}** he besado a **{member.name}**~',
                    color=discord.Colour.random(),
                )
                embed.set_image(url=kiss.url)
                embed.set_footer(text='Powered by nekos.life')
            await ctx.send(embed=embed)

    @commands.command(name='feed')
    async def feed(self, ctx, member: discord.Member = None):
        """
        ¿Quién tiene hambre?
        """
        async with ctx.typing():
            feed = await self.nekos.image(SFWImageTags.FEED)
            if member:
                desc = f'🥄 ¡**{ctx.author.name}** le está dando de comer a **{member.name}**!'
            else:
                desc = f'🍴 **{ctx.author.name}** está comiendo algo rico!'
            embed = discord.Embed(
                description=f'{desc}', color=discord.Colour.random()
            )
            embed.set_image(url=feed.url)
            embed.set_footer(text='Powered by nekos.life')
            await ctx.send(embed=embed)

    @commands.command(name='smug')
    async def smug(self, ctx):
        """
        >;)
        """
        async with ctx.typing():
            smug = await self.nekos.image(SFWImageTags.SMUG)
            embed = discord.Embed(
                description=f'💯 **{ctx.author.name}** tiene mucha malicia',
                color=discord.Colour.random(),
            )
            embed.set_image(url=smug.url)
            embed.set_footer(text='Powered by nekos.life')
        await ctx.send(embed=embed)

    @commands.command(name='hi', aliases=['hola', 'hello', 'wave'])
    async def wave(self, ctx):
        """
        ¡Hola a todos!
        """
        async with ctx.typing() and self.session.get(
            'https://api.waifu.pics/sfw/wave'
        ) as r:
            data = await r.json()
            hi = data['url']
            embed = discord.Embed(
                description=f'👋 **{ctx.author.name}** está saludando',
                color=discord.Colour.random(),
            )
            embed.set_image(url=f'{hi}')
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)

    @commands.command(name='yeet')
    async def yeet(self, ctx, member: discord.Member = None):
        """
        YEET
        """
        if member is ctx.author:
            message = '¡No puedes hacerte yeet a tí mismo!'
            await ctx.reply(message)
        elif member is None:
            await ctx.reply('¡Primero necesitas etiquetar a alguien!')
        else:
            async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/yeet'
            ) as r:
                data = await r.json()
                yeet = data['url']
                embed = discord.Embed(
                    description=f'🚀 ¡**{ctx.author.name}** mandó a volar a **{member.name}**!',
                    color=discord.Colour.random(),
                )
                embed.set_image(url=f'{yeet}')
                embed.set_footer(text='Powered by waifu.pics')
            await ctx.send(embed=embed)

    @commands.command(name='handholding')
    async def handholding(self, ctx, member: discord.Member = None):
        """
        [CENSORED]
        """
        if member is ctx.author:
            message = '¡No puedes tomar tu propia mano!\nBueno, si puedes pero ya sabes a lo que me refiero'
            await ctx.reply(message)
        elif member is None:
            await ctx.reply('¡Primero necesitas etiquetar a alguien!')
        else:
            async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/handhold'
            ) as r:
                data = await r.json()
                hand = data['url']
                embed = discord.Embed(
                    description=f'😳 ¡**{ctx.author.name}** y **{member.name}** se están tomando las manos!',
                    color=discord.Colour.random(),
                )
                embed.set_image(url=f'{hand}')
                embed.set_footer(text='Powered by waifu.pics')
            await ctx.send(embed=embed)

    @commands.command(name='happy', aliases=['smile'])
    async def happy(self, ctx):
        """
        ¡Mira qué feliz soy!
        """
        async with ctx.typing() and self.session.get(
            'https://api.waifu.pics/sfw/happy'
        ) as r:
            data = await r.json()
            happy = data['url']
            embed = discord.Embed(
                description=f'😊 **{ctx.author.name}** se siente muy feliz',
                color=discord.Colour.random(),
            )
            embed.set_image(url=f'{happy}')
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)

    @commands.command(name='wink')
    async def wink(self, ctx):
        """
        ;)
        """
        async with ctx.typing() and self.session.get(
            'https://api.waifu.pics/sfw/wink'
        ) as r:
            data = await r.json()
            wink = data['url']
            embed = discord.Embed(
                description=f'😉 **{ctx.author.name}** está intentando decir algo',
                color=discord.Colour.random(),
            )
            embed.set_image(url=f'{wink}')
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)

    @commands.command(name='cringe')
    async def cringe(self, ctx):
        """
        C R I N G E
        """
        async with ctx.typing() and self.session.get(
            'https://api.waifu.pics/sfw/cringe'
        ) as r:
            data = await r.json()
            cringe = data['url']
            embed = discord.Embed(
                description=f'😒 **{ctx.author.name}** siente demasiado cringe',
                color=discord.Colour.random(),
            )
            embed.set_image(url=f'{cringe}')
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)

    @commands.command(name='bully')
    async def bully(self, ctx, member: discord.Member = None):
        """
        ¿Quieres molestar a alguien?
        """
        if member is ctx.author:
            message = '¡No puedes hacerte bullying a ti mismo!'
            await ctx.reply(message)
        elif member is None:
            await ctx.reply('¡Primero necesitas etiquetar a alguien!')
        else:
            async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/bully'
            ) as r:
                data = await r.json()
                bully = data['url']
                embed = discord.Embed(
                    description=f'🤭 **{ctx.author.name}** le hace bullying a **{member.name}**',
                    color=discord.Colour.random(),
                )
                embed.set_image(url=f'{bully}')
                embed.set_footer(text='Powered by waifu.pics')
            await ctx.send(embed=embed)

    @commands.command(name='highfive', aliases=['five'])
    async def highfive(self, ctx, member: discord.Member = None):
        """
        ¡Chócalas!
        """

        if member is ctx.author:
            message = '¡Necesitas chocar las manos con alguien más!'
            await ctx.reply(message)
        elif member is None:
            await ctx.reply('¡Primero necesitas etiquetar a alguien!')
        else:
            async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/highfive'
            ) as r:
                data = await r.json()
                five = data['url']
                embed = discord.Embed(
                    description=f'🖐️ **{ctx.author.name}** han chocado sus manos **{member.name}**',
                    color=discord.Colour.random(),
                )
                embed.set_image(url=f'{five}')
                embed.set_footer(text='Powered by waifu.pics')
            await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(rol(bot))
