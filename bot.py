
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os

bot=commands.Bot(description='SM Custom Bot made by Antonio32A#0001',command_prefix="?")

@bot.event
async def on_ready():
    print('Connected!')
    print('Username: ' + bot.user.name)
    print('Version:' + discord.__version__)
    print("-----------------------------")
    bot.load_extension("Admin")
    bot.load_extension("Blurple.blurple")


@bot.command(hidden=False)
async def ping(ctx):
    embed = discord.Embed(color=0x4bfab4, title="Pong! :ping_pong:")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def rules(ctx):
    embed=discord.Embed(color=0x4bfab4)
    embed.set_author(name="Rules", icon_url="http://images.all-free-download.com/images/graphiclarge/judge_gavel_312468.jpg")
    embed.add_field(name="1. Respect everyone including yourself.", value="""This means that you don't hate, harass, be rude and racist anyone or anything. This also includes making drama and lying. Control your anger, be friendly!\n\n""", inline=False)
    embed.add_field(name="\n2. Advertising is not allowed.", value="""Don't post invites to other servers, your YouTube channel, etc. This also includes DM Advertising or setting your Discord invite as your playing status.""", inline=False)
    embed.add_field(name="\n3. Spamming/Raiding is not allowed.", value="""This includes:\n• Zalgo Text. Example: `Z̡͢͠a̶̧̛ļ̨͝ģ̶͟o͞͏` \n• Vertical Typng. • XP farmiing.Example `.` `k`\n• Mentioning role, Spam mentioning, Mentioning more than 3 members\n•Having non-taggable names or nicknames.\n• Repeating messages.\n• Copypastas. Example:\n`Discord is deleting accounts! If you don't send this message to 17 servers Discord will delete your account.`\n• Spamming Audio. Example: Playing loud music, playing same music more than 3 times in row.\n• Blowing in Microphone and annyoing other people in voice channel.\n• Shitposting.\n\n""", inline=False)
    embed.add_field(name="\n4. Respect Channel Topics and Pins.", value="""Going offtopic will result in punishment, Staff are allowed to use commands everywhere but not too mutch.\n\n""", inline=False)
    embed.add_field(name="\n5. Don't post NSFW (Not Safe For Work) content.", value="""This includes:\n• Pornografic Images, Videos, etc. \n• Scary, Disgusting, Gore, Violence Images, Videos... This includes posting Images and Videos with blood in them, etc. \n• Posting someone's private information wihtout their approval.\n• Constatly swearing, posting NSFW comments and reacting with NSFW emojis.\n• Using NSFW Playing Status, Nickname or Profile Picture.\n\n""", inline=False)
    embed.add_field(name="\n6. No impersonating others.", value="""This means that you aren't allowed to use same Profile Picture, Nickname/Name as someone else. This includes Bots.\n\n""", inline=False)
    embed.add_field(name="7. Follow Diep rules.", value="""Don't use any Tank wich isnt optainable in Normal Modes (FFA/Maze/Tag/Domination etc.) in Sandbox if the Host don't allow them. No Teaming in FFA/Maze/Sandbox.""", inline=False)
    embed.add_field(name="\n**__License of staff conduct__**", value="""This server is not subject to your definition of "fairness" I and my staff here reserve the right to ban / kick / mute / demote or punish anyone anywhere in any form for any reason at any time as they see fit.""", inline=False)
    embed.set_footer(text="Embed created by Antonio32A#0001 and Spectrix#0001")
    await ctx.send(embed=embed)




@bot.command(hidden=False)
async def tos(ctx):
    emb=discord.Embed(color=0x4bfab4)
    emb.add_field(name=""":warning:  __End User License Agreement (EULA)/Terms Of Service (TOS)__  :warning:""", value="""By joining this server and using this server's bots, **in addition to agreeing to following the rules above, you acknowledge and express irrevocable consent to the unlimited access to and usage of your public discord information by our bots**, including but not limited to your user id, messages sent by you, and directly interacting with your member (such as role management or mentions), other message metadata, or voice metadata. **Failure to agree to these terms may result in punishment including but not limited to permanent eviction from the server.**""", inline=False)
    emb.add_field(name="\u200b", value="""\nUse of bots is provided without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement *anywhere*. **Your understanding and acceptance of these rules implies that you understand and are able to communicate in the English language.**\n""", inline=False)
    emb.add_field(name="\u200b", value="""Furthermore, this server and affiliated bots, bot owners, support servers, and intellectual or real property are, in no event, liable for any claim, special, direct, indirect, consequential, or other damages or other liability, whether in action of contract, tort or otherwise, arising out of or in connection with such property or from loss of use, data, or profits.\n""", inline=False)
    emb.add_field(name="\u200b", value="""**You agree that you will held accountable for actions that break Discord's terms of service and developer terms of service **which can be found here:\nhttps://discordapp.com/terms\nhttps://discordapp.com/developers/docs/legal\n\nFor issues or questions please contact a staff member if you cannot find how to operate it in this channel.""", inline=False)
    await ctx.send(embed=emb)

#--------events-----------
@bot.event
async def on_member_join(member):
   guild = member.guild
   channel = discord.utils.get(guild.channels, id=291558908978397184)
   await channel.send('Welcome {0.mention} to {1.name}! Before you chat read <#458922597049171988>. Enjoy your stay!'.format(member, guild))
   await member.send("Welcome to **Group of SICKness**!\nRead <#391571539193233410> and <#400722327500881930>.\nIf you can't speak in <#291558908978397184> then:\n1. Click resend verification e-mail.\n2. Go to https://gmail.com or other site on which you registered your e-mail.\n3. Login there if you aren't already.\n4. Go to latest email from discordapp\n5. Click verify e-mail (and wait 5 minutes if you made account right now.)\n\nIf you don't know how to do this click on this link to see easier tutorial: https://discordapp.tech/antonio32a/7qlio2.gif")

@bot.event
async def on_member_remove(member):
   guild = member.guild
   channel = discord.utils.get(guild.channels, id=291558908978397184)
   fmt = "{0.mention} just left Group of SICKness ... Press :regional_indicator_f: to pay respects."
   msg = await channel.send(fmt.format(member, guild))
   await msg.add_reaction('🇫')


bot.run(os.getenv('TOKEN'))
