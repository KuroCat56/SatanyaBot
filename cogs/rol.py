import aiohttp
import discord
from discord.ext import commands
import typing as t


class Rol(
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

    @commands.hybrid_command(name='hug', description="¡Abrazos virtuales!")
    async def hug(self, ctx: commands.Context, member: discord.Member = None):
        if member == ctx.author:
            message = '¡No puedes abrazarte a tí mismo!\nAunque puedo darte un abrazo si quieres ヽ(・∀・)ﾉ'
            return await ctx.reply(message)

        elif not member:
            return await ctx.reply('¡Primero necesitas etiquetar a alguien!')

        async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/hug'
        ) as r:
            data = await r.json()
            hug = data['url']

            embed = discord.Embed(
                description=f'🤗 ¡**{ctx.author.name}** ha abrazado a **{member.name}**!',
                color=discord.Colour.random(),
            )
            embed.set_image(url=hug)
            embed.set_footer(text='Powered by nekos.life')
            await ctx.send(embed=embed)

    @commands.hybrid_command(name='bite', aliases=['ñam'], description="Ñam ñam ñam~")
    async def bite(self, ctx: commands.Context, member: t.Optional[discord.Member] = None):
        if member == ctx.author:
            message = '¡No puedes morderte a tí mismo!\nY yo no tengo ganas de morder a nadie (´Д｀υ)'
            return await ctx.reply(message)

        elif not member:
            return await ctx.reply('¡Primero necesitas etiquetar a alguien!')

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

    @commands.hybrid_command(name='dance', aliases=['party'], description="¡Esto hay que celebrarlo!")
    async def dance(self, ctx: commands.Context, member: t.Optional[discord.Member] = None):
        async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/dance'
        ) as r:
            data = await r.json()
            dance = data['url']
            if not member or member == ctx.author:
                desc = f'🎉 ¡**{ctx.author.name}** se ha puesto a bailar!'
            else:
                desc = f'🎊 ¡**{ctx.author.name}** y **{member.name}** están bailando juntos!'
            embed = discord.Embed(
                description=f'{desc}', color=discord.Colour.random()
            )
            embed.set_image(url=f'{dance}')
            embed.set_footer(text='Powered by waifu.pics')
            await ctx.send(embed=embed)

    @commands.hybrid_command(name='pat', aliases=['headpat'], description="¿Alguien se merece unos pat-pat?")
    async def pat(self, ctx: commands.Context, member: t.Optional[discord.Member] = None):
        if member == ctx.author:
            message = '¡No puedes darte pat-pats a tí mismo!\nPero puede darme unos a mí (o´▽`o)'
            return await ctx.reply(message)

        elif not member:
            return await ctx.reply('¡Primero necesitas etiquetar a alguien!')

        async with ctx.typing() and self.session.get(
                'https://nekos.best/api/v2/pat?amount=1'
        ) as r:
            data = await r.json()
            pat = data['results'][0]['url']

            embed = discord.Embed(
                description=f'❣️ **{ctx.author.name}** le ha dado unos pat-pats a **{member.name}**',
                color=discord.Colour.random(),
            )
            embed.set_image(url=pat)
            embed.set_footer(text='Powered by nekos.best')
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='cuddle', description="Abrazos pero con más cariño~")
    async def cuddle(self, ctx: commands.Context, member: t.Optional[discord.Member] = None):
        if member == ctx.author:
            message = '¡No puedes darte cariños a tí mismo!\nPero puede darme unos a mí (o´▽`o)'
            return await ctx.reply(message)

        elif not member:
            return await ctx.reply('¡Primero necesitas etiquetar a alguien!')

        async with ctx.typing() and self.session.get(
                'https://nekos.best/api/v2/cuddle?amount=1'
        ) as r:
            data = await r.json()
            cuddle = data['results'][0]['url']
            embed = discord.Embed(
                description=f'💞 **{ctx.author.name}** abraza con mucho cariño a **{member.name}**',
                color=discord.Colour.random(),
            )
            embed.set_image(url=cuddle)
            embed.set_footer(text='Powered by nekos.best')
            await ctx.send(embed=embed)

    @commands.hybrid_command(name='slap', description="Porque a veces alguien necesita una cachetada (con cariño)")
    async def slap(self, ctx: commands.Context, member: t.Optional[discord.Member] = None):
        if member == ctx.author:
            message = (
                '¡No puedes pegarte a tí mismo!\nA no ser que te guste...'
            )
            return await ctx.reply(message)

        elif not member:
            return await ctx.reply('¡Primero necesitas etiquetar a alguien!')

        async with ctx.typing() and self.session.get(
            'https://nekos.best/api/v2/slap?amount=1'
        ) as r:
            data = await r.json()
            slap = data['results'][0]['url']
            embed = discord.Embed(
                description=f'💢 **{ctx.author.name}** ha cacheteado a **{member.name}**',
                color=discord.Colour.random(),
            )
            embed.set_image(url=slap)
            embed.set_footer(text='Powered by nekos.best')
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='tickle', description="Para molestar a los que tienen cosquillas")
    async def tickle(self, ctx: commands.Context, member: t.Optional[discord.Member] = None):
        if member == ctx.author:
            message = '¡No puedes darte cosquillas a tí mismo!\nAunque puedo darte algunos si quieres (─‿‿─)'
            return await ctx.reply(message)

        elif not member:
            return await ctx.reply('¡Primero necesitas etiquetar a alguien!')

        async with ctx.typing() and self.session.get(
            'https://nekos.best/api/v2/tickle?amount=1'
        ) as r:
            data = await r.json()
            tickle = data['results'][0]['url']
            embed = discord.Embed(
                description=f'🤣 ¡**{ctx.author.name}** le hace cosquillas a **{member.name}!**',
                color=discord.Colour.random(),
            )
            embed.set_image(url=tickle)
            embed.set_footer(text='Powered by nekos.best')
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='poke', description="¿Quieres llamar la atención de alguien?")
    async def poke(self, ctx: commands.Context, member: t.Optional[discord.Member] = None):
        if member == ctx.author:
            message = '¡No puedes molestarte a tí mismo!'
            return await ctx.reply(message)

        elif not member:
            return await ctx.reply('¡Primero necesitas etiquetar a alguien!')

        async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/poke'
        ) as r:
            data = await r.json()
            poke = data['url']
            embed = discord.Embed(
                description=f'👉 **{ctx.author.name}** está molestando a **{member.name}**',
                color=discord.Colour.random(),
            )
            embed.set_image(url=poke)
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='blush', description="Rojo como tomate")
    async def blush(self, ctx: commands.Context):
        async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/blush'
        ) as r:
            data = await r.json()
            blush = data['url']
            embed = discord.Embed(
                description=f'😳 **{ctx.author.name}** se ha puesto rojo como tomate',
                color=discord.Colour.random(),
            )
            embed.set_image(url=blush)
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='cry', aliases=['sad'], description=":(")
    async def cry(self, ctx: commands.Context):
        async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/cry'
        ) as r:
            data = await r.json()
            cry = data['url']
            embed = discord.Embed(
                description=f'😭 **{ctx.author.name}** está llorando. Que alguien le consuele :(',
                color=discord.Colour.random(),
            )
            embed.set_image(url=cry)
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='kiss', description="¿Son pareja? A ver, bésense")
    async def kiss(self, ctx: commands.Context, member: t.Optional[discord.Member] = None):
        if member == ctx.author:
            message = '¡No puedes besarte a tí mismo!\nA no ser que uses algún espejo o algo parecido (￣▽￣*)ゞ'
            return await ctx.reply(message)

        elif not member:
            return ctx.reply('¡Primero necesitas etiquetar a alguien!')

        async with ctx.typing() and self.session.get(
            'https://nekos.best/api/v2/kiss?amount=1'
        ) as r:
            data = await r.json()
            kiss = data['results'][0]['url']
            embed = discord.Embed(
                description=f'💖 **{ctx.author.name}** he besado a **{member.name}**~',
                color=discord.Colour.random(),
            )
            embed.set_image(url=kiss)
            embed.set_footer(text='Powered by nekos.best')
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='feed', description="¿Quién tiene hambre?")
    async def feed(self, ctx: commands.Context, member: t.Optional[discord.Member] = None):
        async with ctx.typing() and self.session.get(
                'https://nekos.best/api/v2/feed?amount=1'
        ) as r:
            data = await r.json()
            feed = data['results'][0]['url']

            if member and member != ctx.author:
                desc = f'🥄 ¡**{ctx.author.name}** le está dando de comer a **{member.name}**!'
            else:
                desc = f'🍴 **{ctx.author.name}** está comiendo algo rico!'
            embed = discord.Embed(
                description=f'{desc}', color=discord.Colour.random()
            )
            embed.set_image(url=feed)
            embed.set_footer(text='Powered by nekos.best')
            await ctx.send(embed=embed)

    @commands.hybrid_command(name='smug', description=">;)")
    async def smug(self, ctx: commands.Context):
        async with ctx.typing() and self.session.get(
            'https://nekos.best/api/v2/smug?amount=1'
        ) as r:
            data = await r.json()
            smug = data['results'][0]['url']
            embed = discord.Embed(
                description=f'💯 **{ctx.author.name}** tiene mucha malicia',
                color=discord.Colour.random(),
            )
            embed.set_image(url=smug)
            embed.set_footer(text='Powered by nekos.best')
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='hi', aliases=['hola', 'hello', 'wave'], description="¡Hola a todos!")
    async def wave(self, ctx: commands.Context):
        async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/wave'
        ) as r:
            data = await r.json()
            hi = data['url']
            embed = discord.Embed(
                description=f'👋 **{ctx.author.name}** está saludando',
                color=discord.Colour.random(),
            )
            embed.set_image(url=hi)
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='yeet', description="YEET")
    async def yeet(self, ctx: commands.Context, member: t.Optional[discord.Member] = None):
        if member == ctx.author:
            message = '¡No puedes hacerte yeet a tí mismo!'
            return await ctx.reply(message)

        elif not member:
            return await ctx.reply('¡Primero necesitas etiquetar a alguien!')

        async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/yeet'
        ) as r:
            data = await r.json()
            yeet = data['url']
            embed = discord.Embed(
                description=f'🚀 ¡**{ctx.author.name}** mandó a volar a **{member.name}**!',
                color=discord.Colour.random(),
            )
            embed.set_image(url=yeet)
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='handholding', description="[CENSORED]")
    async def handholding(self, ctx: commands.Context, member: t.Optional[discord.Member] = None):
        if member == ctx.author:
            message = '¡No puedes tomar tu propia mano!\nBueno, si puedes pero ya sabes a lo que me refiero'
            return await ctx.reply(message)

        elif not member:
            return await ctx.reply('¡Primero necesitas etiquetar a alguien!')

        async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/handhold'
        ) as r:
            data = await r.json()
            hand = data['url']
            embed = discord.Embed(
                description=f'😳 ¡**{ctx.author.name}** y **{member.name}** se están tomando las manos!',
                color=discord.Colour.random(),
            )
            embed.set_image(url=hand)
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='happy', aliases=['smile'], description="¡Mira qué feliz soy!")
    async def happy(self, ctx: commands.Context):
        async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/happy'
        ) as r:
            data = await r.json()
            happy = data['url']
            embed = discord.Embed(
                description=f'😊 **{ctx.author.name}** se siente muy feliz',
                color=discord.Colour.random(),
            )
            embed.set_image(url=happy)
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='wink', description=";)")
    async def wink(self, ctx: commands.Context):
        async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/wink'
        ) as r:
            data = await r.json()
            wink = data['url']
            embed = discord.Embed(
                description=f'😉 **{ctx.author.name}** está intentando decir algo',
                color=discord.Colour.random(),
            )
            embed.set_image(url=wink)
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='cringe', description="C R I N G E")
    async def cringe(self, ctx: commands.Context):
        async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/cringe'
        ) as r:
            data = await r.json()
            cringe = data['url']
            embed = discord.Embed(
                description=f'😒 **{ctx.author.name}** siente demasiado cringe',
                color=discord.Colour.random(),
            )
            embed.set_image(url=cringe)
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='bully', description="¿Quieres molestar a alguien?")
    async def bully(self, ctx: commands.Context, member: t.Optional[discord.Member] = None):
        if member == ctx.author:
            message = '¡No puedes hacerte bullying a ti mismo!'
            return await ctx.reply(message)

        elif not member:
            return await ctx.reply('¡Primero necesitas etiquetar a alguien!')

        async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/bully'
        ) as r:
            data = await r.json()
            bully = data['url']
            embed = discord.Embed(
                description=f'🤭 **{ctx.author.name}** le hace bullying a **{member.name}**',
                color=discord.Colour.random(),
            )
            embed.set_image(url=bully)
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='highfive', aliases=['five'], description="¡Chócalas!")
    async def highfive(self, ctx: commands.Context, member: t.Optional[discord.Member] = None):
        if member == ctx.author:
            message = '¡Necesitas chocar las manos con alguien más!'
            return await ctx.reply(message)
        elif not member:
            return await ctx.reply('¡Primero necesitas etiquetar a alguien!')

        async with ctx.typing() and self.session.get(
                'https://api.waifu.pics/sfw/highfive'
        ) as r:
            data = await r.json()
            five = data['url']
            embed = discord.Embed(
                description=f'🖐️ **{ctx.author.name}** han chocado sus manos **{member.name}**',
                color=discord.Colour.random(),
            )
            embed.set_image(url=five)
            embed.set_footer(text='Powered by waifu.pics')
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Rol(bot))
