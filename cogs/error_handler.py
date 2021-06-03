#Extraído de https://vcokltfre.dev/tutorial/12-errors/
from discord.ext import commands


class ErrorHandler(commands.Cog):
    """A cog for global error handling."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler cog."""

        if isinstance(error, commands.CommandNotFound):
            return  # Return because we don't want to show an error for every command not found
        elif isinstance(error, commands.CommandOnCooldown):
            message = f"Has usado este comando demasiado rápido. Intenta de nuevo en **{round(error.retry_after, 1)} segundos.**"
        elif isinstance(error, commands.MissingPermissions):
            message = "¿Qué intentas hacer? Te faltan permisos para usar este comando."
        elif isinstance(error, commands.UserInputError):
            message = "Mmmm, creo que no usaste bien el comando. Asegúrate de checar como usarlo checando `nya>help [comando]`"
        else:
            message = "*Hmmm*, ni siquiera yo sé porqué no funcionó este comando."

        await ctx.send(message, delete_after=5)
        await ctx.message.delete(delay=5)

def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
