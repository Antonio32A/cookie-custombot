import discord
from discord.ext import commands
import os
import time
import random


class Commands:
    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        channel = discord.utils.get(guild.channels, id=291558908978397184)
        await channel.send(f"Welcome {member.mention} to {member.guild}! Before you chat read <#458922597049171988>. Enjoy your stay!")

    async def on_member_remove(self, member):
        channel = discord.utils.get(guild.channels, id=291558908978397184)
        m = await channel.send(f"**{member}** just left **{member.guild.name}**. Press :regional_indicator_f: to pay respects.")
        await m.add_reaction('🇫')

    @commands.command()
    async def ping(self, ctx):
        b = time.monotonic()
        message = await ctx.send("Pinging...")
        await ctx.trigger_typing()
        ping = (time.monotonic() - b) * 1000
        ping = round(ping)
        await message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="Pong! 🏓", value=f"My ping is **{ping}ms!**", inline=False)
        gifs = ["http://smashinghub.com/wp-content/uploads/2014/08/cool-loading-animated-gif-3.gif",
        "https://s-media-cache-ak0.pinimg.com/originals/ec/9b/16/ec9b161cf1b2b6d1145933246a723541.gif"
        "https://i.pinimg.com/originals/90/80/60/9080607321ab98fa3e70dd24b2513a20.gif",
        "https://codemyui.com/wp-content/uploads/2016/08/circular-water-fill-loading-animation.gif",
        "https://i.pinimg.com/originals/bf/34/61/bf34611d89cb4e9e62fc4997a1d329f2.gif",
        "http://smashinghub.com/wp-content/uploads/2014/08/cool-loading-animated-gif-8.gif",
        "http://i.imgur.com/24S2Cqk.gif",
        "https://i.gifer.com/BipM.gif",
        "https://vignette.wikia.nocookie.net/spaceagency/images/9/9e/U0UnOge.gif",
        "https://digitalsynopsis.com/wp-content/uploads/2016/06/loading-animations-preloader-gifs-ui-ux-effects-29.gif"]
        gif = random.choice(gifs)
        embed.set_thumbnail(url=gif)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Commands(bot))
