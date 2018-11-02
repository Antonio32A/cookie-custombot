import discord
from discord.ext import commands
from util.bot import Bot
import os

bot = Bot(command_prefix=commands.when_mentioned_or("?"), owner_id=166630166825664512)

if __name__ == '__main__':
    token = os.getenv('token')
    bot.run(token)
