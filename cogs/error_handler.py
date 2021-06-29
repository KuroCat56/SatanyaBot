#Extraído de https://vcokltfre.dev/tutorial/12-errors/
from discord.ext import commands
import traceback


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
            message = f"⏳ Has usado este comando demasiado rápido. Intenta de nuevo en **{round(error.retry_after, 1)} segundos.**"
        elif isinstance(error, commands.MissingPermissions):
            message = "🚫 ¿Qué intentas hacer? Te faltan permisos para usar este comando."
        elif isinstance(error, commands.UserInputError):
            message = "🤔 Mmmm, creo que no usaste bien el comando. Asegúrate de checar como usarlo checando `nya>help [comando]`"
        else:
            # get data from exception
            etype = type(exc)
            trace = exc.__traceback__

            # 'traceback' is the stdlib module, `import traceback`.
            lines = traceback.format_exception(etype, exc, trace)

            # format_exception returns a list with line breaks embedded in the lines, so let's just stitch the elements together
            message = ''.join(lines)

            # now we can send it to the user
            # it would probably be best to wrap this in a codeblock via e.g. a Paginator
            await ctx.send(message)
            await ctx.send(message, delete_after=7)

def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
