import discord
from discord.ext import commands
import asyncio
import time
prefix = "."
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')



@bot.event
async def on_ready():
    print(bot.user.name)
    print('Online')
    print('started.......')
    print('Created with ꧁༒• ⚘!ϻR.ᎻᎯᏨᏦᎬᏒᴼᴾ •༒꧂#9090 ')
    while True:
    	await bot.change_presence(activity=discord.Activity(type=1,name="all VPN and number life "))
    	await asyncio.sleep(3)
    	
    	await bot.change_presence(activity=discord.Activity(type=2,name="selling scripts "))
    	await asyncio.sleep(3)
	
    	await bot.change_presence(activity=discord.Activity(type=2,name="1year recharge"))
    	await asyncio.sleep(3)
    	
    	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Vedantu!"))
    	await asyncio.sleep(3)
    	
    	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="HQ Trivia!"))
    	await asyncio.sleep(3)
    	
    	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Swagbucks Live!"))
    	await asyncio.sleep(3)
    	
    	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Quipp!"))
    	await asyncio.sleep(3)
    	
    	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Flipkart!"))
    	await asyncio.sleep(3)
    	
    	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Everyone!"))
    	await asyncio.sleep(3)
	
    	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="LBS!"))
    	await asyncio.sleep(3)
	
    	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Qureka!"))
    	await asyncio.sleep(3)
    	
    	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Quiz91!"))
    	await asyncio.sleep(3)

    	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="21537 Members!"))
    	await asyncio.sleep(3)
    	
    	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f'''With {len(bot.guilds)} Servers'''))
    	await asyncio.sleep(3)

@bot.command(name="ping")
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)
		

bot.run("BOT_TOKEN")  # Where 'TOKEN' is 
