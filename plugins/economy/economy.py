import discord
from discord.ext import commands
from util import Handlers, Checks
import random

class Economy(commands.Cog, name="Economy"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["$", "bal", "money"])
    async def balance(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author

        sign = Handlers.JSON.getSign(ctx.guild.id)
        balance = str(Handlers.JSON.getBalance(ctx.guild.id, member.id))
        return await ctx.send(f"{member} has {balance} {sign}.")


    @commands.command()
    async def bank(self, ctx):
        sign = Handlers.JSON.getSign(ctx.guild.id)
        bank = str(Handlers.JSON.getBank(ctx.guild.id))
        return await ctx.send(f"There are {bank} {sign} in the bank.")


    @commands.command(aliases=["lb"])
    async def leaderboard(self, ctx, page: int=None):
        m = await ctx.send("Loading...")
        sign = Handlers.JSON.getSign(ctx.guild.id)
        if page is None:
            page = 1
        elif page is 0:
            page = 1
        else:
            page = abs(page)

        users = Handlers.JSON.read()["guilds"][str(ctx.guild.id)]["economy"]["users"]
        users2 = {}
        for user in users.keys():
            users2[str(user)] = users[user]["balance"]
        sorted_users = sorted(users2, key=users2.get, reverse=True)
        embed = discord.Embed(color=ctx.author.color)
        embed.set_author(name="Leaderboard", icon_url=ctx.guild.icon_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)

        if page == 1:
            start = page
        else:
            start = page * 10 - 9
        end = start + 10
        n = start

        for i in sorted_users:
            if n < end:
                try:
                    user = await ctx.bot.get_user_info(int(sorted_users[n-1]))
                    name = f"{n}. {user}"
                    value = str(users[sorted_users[n-1]]["balance"]) + " " + sign
                    embed.add_field(name=name, value=value, inline=False)
                    n += 1
                except:
                    break
            else:
                break
        try:
            await m.delete()
        except:
            pass
        return await ctx.send(embed=embed)


    @commands.command()
    async def timely(self, ctx):
        sign = Handlers.JSON.getSign(ctx.guild.id)
        amount = str(Handlers.JSON.getTimelyAmount(ctx.guild.id))
        userCooldown = int(Handlers.JSON.getUserCooldown(ctx.guild.id, ctx.author.id))
        timelyTime = int(Handlers.JSON.getTimelyTime(ctx.guild.id))

        if userCooldown == 0:
            Handlers.JSON.changeBalance(ctx.guild.id, ctx.author.id, int(amount))
            m, s = divmod(timelyTime, 60)
            time = "%02d minutes and %02d seconds" % (m, s)
            Handlers.JSON.setUserCooldown(ctx.guild.id, ctx.author.id, timelyTime)
            return await ctx.send(f"Successfully claimed {amount} {sign}.\nCome back in {time} minutes to claim your Timely.")
        else:
            m, s = divmod(userCooldown, 60)
            time = "%02d minutes and %02d seconds" % (m, s)
            time = time.replace(" 0", " ")
            return await ctx.send(f"You have to wait {time} to claim you timely.")


    @commands.command()
    async def gamble(self, ctx, amount: str=None):
        balance = int(Handlers.JSON.getBalance(ctx.guild.id, ctx.author.id))
        sign = Handlers.JSON.getSign(ctx.guild.id)
        if amount is None:
            return await ctx.send("You need to specify an amount to gamble.")

        if str(amount).lower() == "all":
            amount = balance
        elif str(amount).lower() == "half":
            if not balance == 0:
                amount = int(round(balance/2))
            else:
                return await ctx.send(f"You don't have enough {sign} to gamble.")
        amount = abs(int(amount))
        if balance < amount or balance == 0 or amount == 0:
            return await ctx.send(f"You don't have enough {sign} to gamble.")

        won = random.choice([True, False])
        if won == True:
            Handlers.JSON.changeBank(ctx.guild.id, -amount)
            Handlers.JSON.changeBalance(ctx.guild.id, ctx.author.id, amount)
            return await ctx.send(f"Congratulations! You just won {str(amount*2)} {sign}!")
        elif won == False:
            Handlers.JSON.changeBank(ctx.guild.id, amount)
            Handlers.JSON.changeBalance(ctx.guild.id, ctx.author.id, -amount)
            return await ctx.send(f"You just lost {str(amount)} {sign}. Better luck next time!")


    @commands.command(aliases=["bf"])
    async def betflip(self, ctx, choice: str=None, amount: str=None):
        sign = Handlers.JSON.getSign(ctx.guild.id)
        balance = int(Handlers.JSON.getBalance(ctx.guild.id, ctx.author.id))
        choice = choice.lower()
        if amount is None:
            return await ctx.send("You need to specify an amount to gamble.")
        if choice is None:
            return await ctx.send("You need to specify a choice (**T**ails or **H**eads).")
        if choice.startswith("h"):
            choice = "h"
        elif choice.startswith("t"):
            choice = "t"
        else:
            return

        if str(amount).lower() == "all":
            amount = balance
        elif str(amount).lower() == "half":
            if not balance == 0:
                amount = int(round(balance/2))
            else:
                return await ctx.send(f"You don't have enough {sign} to gamble.")
        amount = abs(int(amount))
        if balance < amount or balance == 0 or amount == 0:
            return await ctx.send(f"You don't have enough {sign} to gamble.")

        won = random.choice(["h", "t"])
        if won == choice:
            Handlers.JSON.changeBank(ctx.guild.id, -amount)
            Handlers.JSON.changeBalance(ctx.guild.id, ctx.author.id, amount)
            return await ctx.send(f"Congratulations! You just won {str(amount*2)} {sign}!")
        elif not won == choice:
            Handlers.JSON.changeBank(ctx.guild.id, amount)
            Handlers.JSON.changeBalance(ctx.guild.id, ctx.author.id, -amount)
            return await ctx.send(f"You just lost {str(amount)} {sign}. Better luck next time!")
