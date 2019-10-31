import discord
from discord.ext import commands
import os
import json
import asyncio
from PIL import Image, ImageDraw, ImageFont
import aiohttp
import random
from util.handlers import Handlers

class Bot(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def update_activity(self):
        member_count = len(self.get_all_members())
        activity = discord.Activity(name=f"to {member_count} members!",
                                    type=discord.ActivityType.listening)
        await self.change_presence(activity=activity)


    async def send_subcount(self, destination: discord.TextChannel=None, name: str=None, subs: int=None, id: str=None, color: str=None):
        key = os.getenv("youtube_api_key")
        if not id == None:
            url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+id+"&key="+key
            async with aiohttp.ClientSession() as session:
                r = await session.get(url=url)
                data = await r.read()
                r.close()
            subs = int(json.loads(data)["items"][0]["statistics"]["subscriberCount"])

        if color == "random":
                color = tuple((random.randint(0, 255), random.randint(0, 255),  random.randint(0, 255)))
        elif color.startswith("#"):
                color = color.lstrip('#')
                lv = len(color)
                color = tuple(int(color[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

        img = Image.new('RGB', (462, 206), color = color)
        fnt = ImageFont.truetype('Whitney.ttf', 70)
        fnt2 = ImageFont.truetype('Whitney.ttf', 50)
        d = ImageDraw.Draw(img)
        d.text((50, 30), name, font=fnt, fill=(255, 255, 255))
        subs = "{:,}".format(subs).replace(",", ", ")
        d.text((50, 120), str("has " + str(subs) + " subs"), font=fnt2, fill=(255, 255, 255))
        img.save('sm.png')
        await destination.send(file=discord.File('sm.png'))


    async def get_mee6_users(self, guild_id):
        page = 0
        users = []
        url = 'https://mee6.xyz/api/plugins/levels/leaderboard/' + str(guild_id) + '?limit=999&page='
        while True:
            url2 = url + str(page)
            async with aiohttp.ClientSession() as session:
                r = await session.get(url=url2)
                data = json.loads(await r.read())
                r.close()
            if data['players'] == []:
                break
            elif data['players'] != []:
                users += data['players']
                page += 1
        return users


    async def on_command_error(self, ctx, error):
        command = ctx.command
        error = getattr(error, 'original', error)

        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, discord.errors.Forbidden):
            return await ctx.send("I lack permissions to execute this command.")
        else:
            print(f"Exception in command {command}:\n{error}")

    async def load_plugins(self):
        plugins = ["owner", "general", "admin", "economy"]
        for plugin in plugins:
            self.load_extension(f"plugins.{plugin}")
            print(f"Loaded {plugin}.")
        print("Starting...")


    async def on_ready(self):
        print("Starting...")
        Handlers.JSON.settings_setup(self)
        Handlers.JSON.guild_setup(self)
        Handlers.JSON.read()
        print("Setup the Database and started timely cooldown timer.")
        await self.load_plugins()
        await self.update_activity()
        print(f"Logged in as {self.user} ({self.user.id})")
        await Handlers.JSON.startUserTimelyCooldown()
