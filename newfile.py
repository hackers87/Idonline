import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="")#select your prefix
TOKEN = ''#place your token
@bot.event
async def on_ready():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming,name="Welcome Members!"))
        await asyncio.sleep(5)

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming,name="$help"))
        await asyncio.sleep(5)

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f'''{len(bot.guilds)} servers'''))
        await asyncio.sleep(5)
        print("READY !\n{0.user.name}\n{0.user.id}".format(bot))

bot.run(TOKEN, bot=False)