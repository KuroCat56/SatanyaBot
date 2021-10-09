import discord
from discord.ext import commands
import animec

class anime(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 10, commands.BucketType.user)}):
    """
    Comandos relacionados a cosas de anime.
    
    Cooldown: 10s per command
    """
    def __init__(self, bot: commands.Bot):
      self.bot = bot

    @commands.command(aliases=['anisearch', 'animesearch'])
    async def anime(self, ctx, *, name):
      try:
        anime = animec.Anime(name)
      except:
        await ctx.send(embed=discord.Embed(description = "<:notlikethis:868575058283597904> No encontré el anime que estás buscando.", color=discord.Color.red()))
        return
      embed = discord.Embed(title=f"{anime.title_jp}\n{anime.title_english}", url=anime.url, description=f"{anime.description[:200]}...", color=discord.Color.random())
      embed.add_field(name="#️⃣ Episodios:", value=str(anime.episodes()))
      embed.add_field(name="📊 Calificación:", value=str(anime.rating()))
      embed.add_field(name="🔎 Estado:", value=str(anime.status()))
      embed.add_field(name="🏷️ Género:", value=str(anime.type()))
      embed.set_thumbnail(url=anime.poster)
      await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(anime(bot))