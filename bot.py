import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os

bot=commands.Bot(command_prefix="?")

@bot.check
async def globally_block_bots(ctx):
    return not ctx.author.bot

@bot.event
async def on_ready():
    modules = ["Owner", "Commands"]
    print(f"Logged in as {bot.user} ({bot.user.id}).")
    await bot.change_presence(status='dnd', activity=discord.Activity(name=f"Starting...", type=3))
    bot.remove_command('help')
    for module in modules:
        bot.load_extension(f"modules.{module}")
        print(f"Loaded {module}!")
    await bot.change_presence(activity=discord.Activity(name=f"?help", type=discord.ActivityType.listening))
    print("Ready!")


bot.run(os.getenv('TOKEN'))
