import discord
from discord.ext import commands
import os
import json
import asyncio
from PIL import Image, ImageDraw, ImageFont
import aiohttp
import random

class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or("?"),
                         owner_id=166630166825664512)

    async def update_activity(self):
        guild = discord.utils.get(self.guilds, id=291558782755012610)
        member_count = str(len(guild.members))
        activity = discord.Activity(name=f"with {member_count} members!",
                                    type=discord.ActivityType.playing)
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


    async def on_command_error(self, ctx, error):
        command = ctx.command
        error = getattr(error, 'original', error)

        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, discord.errors.Forbidden):
            return await ctx.send("I lack permissions to execute this command.")
        else:
            print(f"Exception in command {command}:\n{error}")


    def start_bot(self):
        modules = ["owner", "general"]
        for module in modules:
            self.load_extension(f"modules.{module}")
            print(f"Loaded {module}.")
        print("Starting...")
        token = os.getenv('token')
        super().run(token)

    async def on_ready(self):
        guild = discord.utils.get(self.guilds, id=291558782755012610)
        channel = discord.utils.get(guild.channels, id=291558908978397184)
        await self.update_activity()
        #await self.send_subcount(destination=channel,
        #                             name="SICKmania",
        #                             subs=None,
        #                             id="UCvVI98ezn4TpX5wDMZjMa3g",
        #                             color="random")
        print(f"Logged in as {self.user} ({self.user.id})")

if __name__ == '__main__':
    Bot().start_bot()
