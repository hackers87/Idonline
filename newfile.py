import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="")#select your prefix
TOKEN = 'NjQwMTUxMjI1OTgzMTcyNjA4.XxAJYQ.vHzi-udBKKZSqzaeUwChUP-61OE'#place your token
@bot.event
async def on_ready():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming,name="SELLING QUIPP AND HQ NUMBER "))
        await asyncio.sleep(5)

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming,name="LIFE AND RECHARGE 1250RS 1 YEAR"))
        await asyncio.sleep(5)

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f'''{len(bot.guilds)} servers'''))
        await asyncio.sleep(5)
        print("READY !\n{0.user.name}\n{0.user.id}".format(bot))

bot.run(TOKEN, bot=False)
