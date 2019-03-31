import json
import os
import discord
import asyncio

class Handlers:
    class JSON:
        def __init__(self, bot):
            self.bot = bot

        def read():
            with open('data.json', 'r', encoding="utf8") as file:
                data = json.load(file)
            return data

        def dump(data):
            with open('data.json', 'w', encoding="utf8") as file:
                    json.dump(data, file, indent=4)

        def setPrefix(guild: int, prefix: str):
            data = Handlers.JSON.read()
            data["guilds"][str(guild)]["prefix"] = prefix
            Handlers.JSON.dump(data)


        async def startUserTimelyCooldown():
            while True:
                data = Handlers.JSON.read()
                for i in data["guilds"]:
                    try:
                        for j in data["guilds"][str(i)]["economy"]["users"]:
                            if not int(data["guilds"][str(i)]["economy"]["users"][j]["userCooldown"]) == 0:
                                data["guilds"][str(i)]["economy"]["users"][j]["userCooldown"] -= 1
                    except:
                        pass

                Handlers.JSON.dump(data)
                await asyncio.sleep(1)


        def getBalance(guild: int, user: int):
            data = Handlers.JSON.read()
            return int(data["guilds"][str(guild)]["economy"]["users"][str(user)]["balance"])


        def changeBalance(guild: int, user: int, amount: int):
            data = Handlers.JSON.read()
            try:
                beforeMoney = data["guilds"][str(guild)]["economy"]["users"][str(user)]["balance"]
                data["guilds"][str(guild)]["economy"]["users"][str(user)]["balance"] = beforeMoney + amount
            except:
                bal = amount
                data["guilds"][str(guild)]["economy"]["users"][str(user)] = {"balance": bal, "timelyCooldown": 0}
            Handlers.JSON.dump(data)


        def getBank(guild: int):
            data = Handlers.JSON.read()
            return int(data["guilds"][str(guild)]["economy"]["bank"])


        def changeBank(guild: int, amount: int):
            data = Handlers.JSON.read()
            beforeBank = data["guilds"][str(guild)]["economy"]["bank"]
            data["guilds"][str(guild)]["economy"]["bank"] = beforeBank + amount
            Handlers.JSON.dump(data)


        def setSign(guild: int, sign: str):
            data = Handlers.JSON.read()
            data["guilds"][str(guild)]["economy"]["sign"] = sign
            Handlers.JSON.dump(data)


        def getSign(guild: int):
            data = Handlers.JSON.read()
            return str(data["guilds"][str(guild)]["economy"]["sign"])


        def setTimelyAmount(guild: int, amount: int):
            data = Handlers.JSON.read()
            data["guilds"][str(guild)]["economy"]["timelyAmount"] = amount
            Handlers.JSON.dump(data)


        def getTimelyAmount(guild: int):
            data = Handlers.JSON.read()
            return int(data["guilds"][str(guild)]["economy"]["timelyAmount"])


        def setTimelyTime(guild: int, time: int):
            data = Handlers.JSON.read()
            data["guilds"][str(guild)]["economy"]["timelyTime"] = time
            Handlers.JSON.dump(data)


        def getTimelyTime(guild: int):
            data = Handlers.JSON.read()
            return int(data["guilds"][str(guild)]["economy"]["timelyTime"])


        def setUserCooldown(guild: int, user: int, amount: int):
            data = Handlers.JSON.read()
            data["guilds"][str(guild)]["economy"]["users"][str(user)]["userCooldown"] = amount
            Handlers.JSON.dump(data)


        def getUserCooldown(guild: int, user: int):
            data = Handlers.JSON.read()
            return int(data["guilds"][str(guild)]["economy"]["users"][str(user)]["userCooldown"])

        def settings_setup(bot):
            if not "data.json" in os.listdir('./'):
                os.system('touch data.json')
            else:
                return
            token = os.getenv('token')
            youtube_api_key = os.getenv('youtube_api_key')
            prefix = os.getenv('prefix')

            with open('data.json', 'w', encoding="utf8") as file:
                data = {
                    "settings": {
                        "token": token,
                        "default_prefix": prefix,
                        "youtube_api_key": youtube_api_key
                    },
                    "guilds": {}
                }
                json.dump(data, file, indent=4)


        def guild_setup(bot):
            data = Handlers.JSON.read()
            prefix = data["settings"]["default_prefix"]
            for guild in bot.guilds:
                if not str(guild.id) in data["guilds"]:
                    data["guilds"][str(guild.id)] = {
                        "prefix": prefix,
                        "economy": {
                            "sign": "💵",
                            "timelyAmount": 50,
                            "timelyTime": 1800,
                            "bank": 0,
                            "users": {}
                        }
                    }
                else:
                    pass
                for user in guild.members:
                        if not str(user.id) in data["guilds"][str(guild.id)]["economy"]["users"]:
                            data["guilds"][str(guild.id)]["economy"]["users"][str(user.id)] = {"balance": 0,
                                                                                               "userCooldown": 0}
                        else:
                            pass
            Handlers.JSON.dump(data)


        async def on_member_join(self, member):
            Handlers.JSON.guild_user_setup(self.bot)

        async def on_guild_join(self, guild):
            Handlers.JSON.guild_user_setup(self.bot)
