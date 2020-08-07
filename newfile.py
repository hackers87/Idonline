import discord
from discord.ext import commands


TOKEN = 'NTU0OTE5MTg0MzEyODI3OTIy.XyzkzA.Q2Qz8K2KkqegfjL4Vyrb5JD3g4E'#place your token
@bot.event
async def on_ready():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming,name="SELLING QUIPP AND HQ NUMBER "))
        await asyncio.sleep(5)

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming,name="LIFE AND RECHARGE 1250RS 1 YEAR"))
        await asyncio.sleep(5)



        print("READY !\n{0.user.name}\n{0.user.id}".format(bot))

bot.run(TOKEN, bot=False)
