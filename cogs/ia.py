import discord
from discord.ext import commands
import os
from openai import Client
import typing as t
import time


class IA(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.client = Client(api_key=os.getenv('OPENAI_API_KEY'))

    z: t.Dict[int, int] = {}

    @commands.hybrid_command(name="ask", description="Preguntale algo a ChatGPT")
    async def _ask(self, ctx: commands.Context, *, prompt: str):
        collected_messages = []
        message = await ctx.send("...")
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "user", "content": prompt}
            ],
            stream=True,
            max_tokens=256
        )
        for chunk in response:
            self.z[message.id] = int(time.time())
            chunk_content = chunk.choices[0].delta.content
            if chunk_content:
                collected_messages.append(chunk_content)
            if int(time.time()) - self.z[message.id] > 2:
                await message.edit(content="".join(collected_messages) + chunk_content + "...")

        await message.edit(content="".join(collected_messages))


async def setup(bot: commands.Bot):
    await bot.add_cog(CogIA(bot))
