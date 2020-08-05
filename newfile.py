import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="")#select your prefix

@bot.event
async def on_ready():
	while True:
		await bot.change_presence(activity=discord.Activity(type=1,name="Welcome Members!"))
		await asyncio.sleep(5)
		
		await bot.change_presence(activity=discord.Activity(type=1,name="$help"))
		await asyncio.sleep(5)
		
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'''{len(bot.guilds)} servers'''))
		await asyncio.sleep(5)
		print("READY !\n{0.user.name}\n{0.user.id}".format(bot))

bot.run(',bot=False')#place your token