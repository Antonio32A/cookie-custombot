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
    l = [f"<@{id}> ", f"<@!{id}> "]
    # In case it fails for some reason
    for i in range(0, 5):
        try:
            prefix = Handlers.JSON.read()["guilds"][str(message.guild.id)]["prefix"]
            l.append(prefix)
        except:
            continue
        break
    return l


bot = Bot(command_prefix=get_pre, owner_id=166630166825664512)

if __name__ == '__main__':
    bot.run(token)
