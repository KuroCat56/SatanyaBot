# pequeño "snippet" de https://github.com/AlexFlipnote/discord_bot.py/blob/master/utils/default.py, tqm alexflipnote
import traceback


def traceback_maker(err):
    """A way to debug your code anywhere"""
    _traceback = ''.join(traceback.format_tb(err.__traceback__))
    error = ('```py\n{1}{0}: {2}\n```').format(
        type(err).__name__, _traceback, err
    )
    return error
