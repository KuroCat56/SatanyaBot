#Extraído de https://vcokltfre.dev/tutorial/12-errors/
from discord.ext import commands
import discord


class ErrorHandler(commands.Cog):
    """A cog for global error handling."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler cog."""
        try:
            if isinstance(error, commands.CommandNotFound):
                return
            elif isinstance(error, commands.CommandOnCooldown):
                message = f"⏳ Has usado este comando demasiado rápido. Intenta de nuevo en **{round(error.retry_after, 1)} segundos.**"
            elif isinstance(error, commands.MissingPermissions):
                message = "🚫 Parece que te hacen faltan permisos para usar este comando."
            elif isinstance(error, commands.UserInputError):
                message = "🤔 Mmmm, creo que no usaste bien el comando. Asegúrate de checar como usarlo checando `nya>help [comando]`"
            elif isinstance(error, commands.MissingRequiredArgument):
                message = f"🛑 Espera, no has ejecutado bien el comando. Necesito estos argumentos: **{error.param}**"
            elif isinstance(error, commands.UserNotFound):
                message = "⛔ No soy capaz de encontrar al usuario que has mencionado. ¿Está realmente en este server?"
            elif isinstance(error, commands.NotOwner):
                message = "<:doki_shrug:846548924890349627> Lo siento, pero este comando solo lo puede usar mi creador."
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}', delete_after=10)
        embed = discord.Embed(
            title = "UN ERROR SALVAJE APARECIÓ",
            description = message,
            color = 0xFF0000
        )
        await ctx.send(embed=embed, delete_after=10)

def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
