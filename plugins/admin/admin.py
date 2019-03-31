import discord
from discord.ext import commands
from util import Checks, Handlers

class Admin(commands.Cog, name="Admin"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @Checks.is_admin()
    async def setprefix(self, ctx, *, prefix: str=None):
        if prefix is None:
            return await ctx.send("You need to specify a prefix.")
        Handlers.JSON.setPrefix(ctx.guild.id, prefix)
        return await ctx.send(f"Successfully set prefix to {prefix}".replace("@", "@\u200B"))

    @commands.command()
    @Checks.is_admin()
    async def setsign(self, ctx, *, sign: str=None):
        if sign is None:
            return await ctx.send("You need to specify a sign.")
        Handlers.JSON.setSign(ctx.guild.id, sign)
        return await ctx.send(f"Successfully set sign to {sign}".replace("@", "@\u200B"))


    @commands.command()
    @Checks.is_admin()
    async def settimelyamount(self, ctx, amount: int=None):
        if amount is None:
            return await ctx.send("You need to specify an amount.")
        Handlers.JSON.setTimelyAmount(ctx.guild.id, amount)
        return await ctx.send(f"Successfully set Timely amount to {amount}.")


    @commands.command()
    @Checks.is_admin()
    async def settimelytime(self, ctx, time: int=None):
        if time is None:
            return await ctx.send("You need to specify the time.")
        Handlers.JSON.setTimelyTime(ctx.guild.id, time)
        return await ctx.send(f"Successfully set Timely time to {time} seconds.")


    @commands.command()
    @Checks.is_admin()
    async def award(self, ctx, member: discord.Member=None, amount: int=None):
        sign = Handlers.JSON.getSign(ctx.guild.id)
        if member is None:
            return await ctx.send("You need to specify a member.")
        if amount is None:
            return await ctx.send("You need to specify an amount.")

        amount = abs(amount)
        Handlers.JSON.changeBalance(ctx.guild.id, member.id, amount)
        return await ctx.send(f"Successfully awarded {amount} {sign} to {member}.")


    @commands.command()
    @Checks.is_admin()
    async def take(self, ctx, member: discord.Member=None, amount: int=None):
        sign = Handlers.JSON.getSign(ctx.guild.id)
        if member is None:
            return await ctx.send("You need to specify a member.")
        if amount is None:
            return await ctx.send("You need to specify an amount.")

        amount = abs(amount)
        balance = int(Handlers.JSON.getBalance(ctx.guild.id, member.id))
        if amount > balance:
            amount = balance
        Handlers.JSON.changeBalance(ctx.guild.id, member.id, -amount)
        return await ctx.send(f"Successfully took {amount} {sign} from {member}.")
