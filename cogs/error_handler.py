#Extraído de https://vcokltfre.dev/tutorial/12-errors/
from discord.ext import commands
import discord
from difflib import get_close_matches

class ErrorHandler(commands.Cog):
    """A cog for global error handling."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler cog."""
        try:
            if isinstance(error, commands.CommandNotFound):
                cmd = ctx.invoked_with
                cmds = [cmd.name for cmd in self.bot.commands if not cmd.hidden] # use this to stop showing hidden commands as suggestions
                matches = get_close_matches(cmd, cmds)
                if len(matches) > 0:
                    await ctx.send(f'<:okaynt:846612437637660702> No encontré el comando **"{cmd}"**, ¿Quisiste decir **"{matches[0]}"**?', delete_after=10)
                else:
                    await ctx.send(f'<:nope:846611758445625364> No encontré el comando **"{cmd}"**. Usa el comando de ayuda para saber que comandos están disponibles.', delete_after=10)
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
            elif isinstance(error, commands.BotMissingPermissions):
                message = f"<:okaynt:846612437637660702> No puedo ejecutar este comando, me faltan ciertos permisos: {error.missing_perms}"
        except Exception as e:
            message = (f'**`ERROR:`** {type(e).__name__} - {e}')
        embed = discord.Embed(
            title = "UN ERROR SALVAJE APARECIÓ",
            description = message,
            color = 0xFF0000
        )
        await ctx.send(embed=embed, delete_after=10)

def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
