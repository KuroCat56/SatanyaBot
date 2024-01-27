import asyncio
import random
import aiohttp
from bs4 import BeautifulSoup
import discord
from discord.ext import commands


def random_love():
    love = random.randint(0, 100)
    return love


def text_to_owo(text):
    return (
        text.replace('l', 'w')
        .replace('r', 'w')
        .replace('L', 'W')
        .replace('R', 'W')
    )  # esto lo hice en unos 5 minutos XD


async def get_memes() -> list:
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    images = []
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('https://es.memedroid.com/memes/latest') as response:
            response.raise_for_status()
            data = await response.read()
            soup = BeautifulSoup(data, 'html.parser')
            for item in soup.find_all(class_="item-aux-container"):
                img_tag = item.find('img')
                if img_tag and 'video-play-button' not in img_tag.get('class', []):
                    images.append(img_tag['src'])
    return images


eightballresponses = [
    'Ciertamente.',
    'Es decididamente así.',
    'Sin duda.',
    'Sí - definitivamente.',
    'Puedes confiar en ello.',
    'Como yo lo veo, sí.',
    'Es lo más probable.',
    'Si.',
    'Las señales dicen que si.',
    'Respuesta confusa, intenta otra vez.',
    'Pregunta de nuevo más tarde.',
    'Mejor no decirte ahora.',
    'No se puede predecir ahora.',
    'Concéntrate y pregunta otra vez.',
    'No cuentes con eso',
    'Mi respuesta es no.',
    'Mis fuentes dicen que no.',
    'Muy dudoso.',
]


class Fun(
    commands.Cog,
    group_name="fun",
    command_attrs={
        'cooldown': commands.CooldownMapping.from_cooldown(
            1, 5, commands.BucketType.user
        )
    },
):
    """
    Comandos divertidos muy variados. ¡Pruébalos todos!

    Cooldown: 5s per command
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        self.bot.mention = ['satanya', 'satanyabot']
        mention = self.bot.mention
        if msg.author.bot:
            return
        if any(word in msg.content.lower() for word in mention):
            emoji_nya = '<:SatanyaBot:858480664143331338>'
            await msg.add_reaction(emoji_nya)
            await self.bot.process_commands(msg)

    @commands.hybrid_command(name='meme', description="Obtén un meme de r/memes")
    async def meme(self, ctx: commands.Context):
        async with ctx.typing():
            meme = await get_memes()
            url = random.choice(meme)
            embed = discord.Embed(color=0xa8f1b8)
            embed.set_image(url=url)
            embed.set_footer(text="Extraído de memedroid")
            await ctx.send(embed=embed)

    @commands.command(name="owo",
                      description="Escribe lo que quieras al usar este comando para que lo owofique.")
    async def owo(self, ctx: commands.Context, *, text):
        await ctx.message.delete()
        await ctx.send(text_to_owo(text))

    @commands.hybrid_command(name="say", descriptioN="¿Quieres que diga algo por ti?")
    async def say(self, ctx: commands.Context, *, text):
        await ctx.message.delete()
        await ctx.send(text)

    @commands.command(name="love", description="Calcula tus posibilidades con otro usuario")
    async def love(self, ctx: commands.Context, member: discord.Member = None):
        calc_love = random_love()
        if not member:
            return await ctx.reply('¡Primero necesitas etiquetar a alguien!')

        elif member == ctx.author:
            message = '∞ [█████████████████████]\n**Tienes el suficiente ego como para aceptarte y amarte como eres.**'
            return await ctx.reply(message)

        if calc_love == 0:
            love_messsage = f'{calc_love}% [ . . . . . . . . . . ]\n🚫 No existe compatibilidad entre **{ctx.author.name}** y **{member.name}**'
        elif 1 <= calc_love <= 10:
            love_messsage = f'{calc_love}% [█ . . . . . . . . . ]\n🙅‍♀️ La compatibilidad entre **{ctx.author.name}** y **{member.name}** es demasiado baja'
        elif 11 <= calc_love <= 20:
            love_messsage = f'{calc_love}% [█ . . . . . . . . . ]\n🤔 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es demasiado baja'
        elif 21 <= calc_love <= 30:
            love_messsage = f'{calc_love}% [██ . . . . . . . ]\n😶 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es baja'
        elif 31 <= calc_love <= 40:
            love_messsage = f'{calc_love}% [███ . . . . . . ]\n💌 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es baja'
        elif 41 <= calc_love <= 50:
            love_messsage = f'{calc_love}% [████ . . . . . ]\n💑 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es normal'
        elif 51 <= calc_love <= 60:
            love_messsage = f'{calc_love}% [█████ . . . . ]\n❤️ La compatibilidad entre **{ctx.author.name}** y **{member.name}** es normal'
        elif 61 <= calc_love <= 70:
            love_messsage = f'{calc_love}% [██████ . . . ]\n💕 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es decemte'
        elif 71 <= calc_love <= 80:
            love_messsage = f'{calc_love}% [███████ . . ]\n💝 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es decemte'
        elif 81 <= calc_love <= 90:
            love_messsage = f'{calc_love}% [████████ . ]\n💘 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es muy buena'
        elif 91 <= calc_love <= 99:
            love_messsage = f'{calc_love}% [█████████]\n💞 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es muy buena'
        elif calc_love == 100:
            love_messsage = f'{calc_love}% [██████████]\n💖 La compatibilidad entre **{ctx.author.name}** y **{member.name}** es perfecta'
        embed = discord.Embed(description=f'{love_messsage}', color=0xFF9999)
        await ctx.reply(embed=embed)

    @commands.hybrid_command(aliases=['shipname'],
                             description="Descubre el cómo sería el shipname entre dos usuarios 💘")
    async def ship(
            self, ctx, member: discord.Member, member2: discord.Member = None
    ):
        if not member2:
            member2 = ctx.author

        if len(member.display_name) < 4:
            N = len(member.display_name) / 2

            firstmember = member.display_name
            firstship = firstmember[0: int(N)]

            secondmember = member2.display_name
            secondship = secondmember[0:4]

        elif len(member2.display_name) < 4:
            N = len(member2.display_name) / 2

            firstmember = member.display_name
            firstship = firstmember[0:4]

            secondmember = member2.display_name
            secondship = secondmember[0: int(N)]

        else:

            firstmember = member.display_name
            firstship = firstmember[0:4]

            secondmember = member2.display_name
            secondship = secondmember[0:4]

        shipname = firstship + secondship

        embed = discord.Embed(
            description=f'{member.display_name} + {member2.display_name} = **{shipname}** 💘',
            colour=0xFFB5F7,
        )

        await ctx.send(embed=embed)

    @commands.hybrid_command(name='8ball', aliases=['ball8'],
                             description="Hazme una pregunta y yo te daré una respuesta.")
    async def _8ball(self, ctx, *, question):
        eightball = discord.Embed(
            title='Tu pregunta:',
            description=f'{question}',
            color=discord.Colour.random(),
        )
        eightball.add_field(
            name='La respuesta:',
            value=f'||{(random.choice(eightballresponses))}||',
        )

        await ctx.reply('🎱 Sacudiendo...', embed=eightball)

    # @commands.command(aliases=['oog'])
    # async def oogway(self, ctx, *, msg: str):
    #   """
    #   Como dice el maestro Oogway
    #   """
    #   msg = msg.replace(" ", "+")
    #   async with ctx.typing():
    #     em_oo = discord.Embed(color = ctx.author.color)
    #     em_oo.set_image(url=f"https://api.popcat.xyz/oogway?text={msg}")
    #     em_oo.set_footer(text="🐱 Powered by Pop Cat API")
    #   await ctx.send(embed = em_oo)

    # @commands.command(aliases=['gatosad'])
    # async def sadcat(self, ctx, *, msg: str):
    #   """
    #   Demuestra que andas triste con un meme
    #   """
    #   msg = msg.replace(" ", "+")
    #   async with ctx.typing():
    #     em_sadcat = discord.Embed(color = ctx.author.color)
    #     em_sadcat.set_image(url=f"https://api.popcat.xyz/sadcat?text={msg}")
    #     em_sadcat.set_footer(text="🐱 Powered by Pop Cat API")
    #   await ctx.send(embed = em_sadcat)


async def setup(bot):
    await bot.add_cog(Fun(bot))