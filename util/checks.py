from discord.ext import commands

class Checks:
    def is_admin():
        async def pred(ctx):
            for i in ctx.author.roles:
                if i.permissions.administrator == True:
                    return True

            if ctx.author.id == ctx.bot.owner_id:
                return True
            elif ctx.author.id == ctx.guild.owner.id:
                return True
            else:
                return False 
        return commands.check(pred)