import discord
from discord.ext import commands
from util import Bot, Handlers
import os

if "data.json" in os.listdir('./'):
    settings = Handlers.JSON.read()["settings"]
    token = settings["token"]
else:
    token = os.getenv('token')

def get_pre(bot, message):
    id = bot.user.id
    l = [f"<@{id}> ", f"<@!{id}> ", Handlers.JSON.read()["guilds"][str(message.guild.id)]["prefix"]]
    return l


bot = Bot(command_prefix=get_pre, owner_id=166630166825664512)

if __name__ == '__main__':
    bot.run(token)
