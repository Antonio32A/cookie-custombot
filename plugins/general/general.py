import discord
from discord.ext import commands
import os
import time
import random
from util import Handlers

class General:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def prefix(self, ctx):
        prefix = Handlers.JSON.read()["guilds"][str(ctx.guild.id)]["prefix"]
        return await ctx.send(f"My prefix is {prefix}".replace("@", "@\u200B"))



    async def on_member_join(self, member):
        if member.guild.id == 291558782755012610:
            channel = discord.utils.get(member.guild.channels, id=291558908978397184)
            await channel.send(f"Welcome {member.mention} to {member.guild}! Before you chat read <#458922597049171988>. Enjoy your stay!")
            await self.bot.update_activity()

    async def on_member_remove(self, member):
        if member.guild.id == 291558782755012610:
            channel = discord.utils.get(member.guild.channels, id=291558908978397184)
            m = await channel.send(f"**{member}** just left **{member.guild.name}**. Press :regional_indicator_f: to pay respects.")
            await m.add_reaction('🇫')
            await self.bot.update_activity()

    @commands.command()
    async def subcount(self, ctx, color: str=None):
        if color == None:
            color = "random"
        await ctx.trigger_typing()
        await ctx.bot.send_subcount(destination=ctx.channel,
                                    name="SICKmania",
                                    subs=None,
                                    id="UCvVI98ezn4TpX5wDMZjMa3g",
                                    color=color)


    @commands.command(aliases=["m6r"])
    async def mee6rank(self, ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author
        msg = await ctx.send("Getting data...")
        users = await ctx.bot.get_mee6_users(ctx.guild.id)
        await msg.delete()
        id = member.id
        place = 0
        for user in users:
            place += 1
            if int(user['id']) == id:
                avatar = f"https://media.discordapp.net/avatars/{str(user['id'])}/{user['avatar']}.png"
                username = f"{user['username']}#{user['discriminator']}"
                level = str(user['level'])
                xp = user['xp']
                xp = "{:,}".format(xp)
                xp1 = user['detailed_xp'][0]
                xp2 = user['detailed_xp'][1]
                xp_to_levelup = xp2 - xp1
                xp_percentage = 100 - round((xp1/xp2)*100)
                xp1 = "{:,}".format(xp1)
                xp2 = "{:,}".format(xp2)
                messages = round(xp_to_levelup/20)
                messages = "{:,}".format(messages)
                xp_to_levelup = "{:,}".format(xp_to_levelup)

                embed = discord.Embed(color=ctx.author.color)
                embed.set_author(icon_url=avatar, name=f"Mee6 Level Stats for {member}")
                embed.add_field(name="Level", value=level, inline=False)
                embed.add_field(name="Place on Leaderboard", value="#" + str(place), inline=False)
                embed.add_field(name="Total XP", value=str(xp) + " XP", inline=False)
                embed.add_field(name="Level XP", value=f"**{str(xp1)}** XP out of **{str(xp2)}** XP\n"
                                                       f"**{str(xp_to_levelup)}** XP (**{str(xp_percentage)}%**) needed to levelup.\n"
                                                       f"Thats about **{str(messages)}** messages!")
                embed.set_thumbnail(url=avatar)
                await ctx.send(embed=embed)


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
        return await ctx.send(embed=embed)
