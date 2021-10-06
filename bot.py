import discord
from discord.ext import commands
import asyncio
import psutil
from uptime import uptime

async def status_task():
    while True:
        #CPU \ Load
        #activity = discord.Game(name="CPU: " + str(psutil.cpu_percent()) + "%   \nLoad avg: " + str(getloadavg())[1:-1], type=4)
        #activity = discord.Activity(type=discord.ActivityType.watching, name="CPU: " + str(psutil.cpu_percent()) + "%") #		\nLoad avg: " + str(getloadavg))[1:-1]
        activity = discord.Activity(type=discord.ActivityType.watching, name="CPU: " + str(psutil.cpu_percent()) + "%		\nLoad avg: " + str(psutil.getloadavg())[1:-1])
        try:
            #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="CPU: " + str(psutil.cpu_percent()) + "%   \nLoad avg: " + str(getloadavg())[1:-1]))
            await bot.change_presence(status=discord.Status.idle, activity=activity)
        except ConnectionResetError:
            print ("ConnectionResetError: Ignoring..")
            pass
        #await bot.change_presence(status=discord.Status.idle, activity=activity)
        await asyncio.sleep(4)
        #RAM
        total = psutil.virtual_memory().total/1024
        available = psutil.virtual_memory().available/1024
        used = total - available
        ram = "RAM: " + str(round(used/1024,1)) + "M/" + str(round(total/1024)) + "M   "
        #uptime
        m, s = divmod(int(uptime()), 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        up = str(d) + " days, " + str(h) + ":" + str(m) + ":" + str(s)
        activity = discord.Activity(type=discord.ActivityType.watching, name=ram + "		\nUptime: " + up + "s")
        #activity = discord.Game(name=ram + "\nUptime: " + up + "s", type=3)
        try:
            await bot.change_presence(status=discord.Status.idle, activity=activity)
        except ConnectionResetError:
            print ("ConnectionResetError: Ignoring..")
            pass
        await asyncio.sleep(4)
        #UPTIME
        #activity = discord.Game(name=("Uptime: " + str(uptime()) + "s"), type=3)
        #await bot.change_presence(status=discord.Status.idle, activity=activity)
        #await asyncio.sleep(5)

TOKEN = ' !!! BOT TOKEN !!! '

description = '''Runnin\' from lava OwO'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
#    activity = discord.Game(name="Netflix", type=3)
#    await bot.change_presence(status=discord.Status.idle, activity=activity)
    looping = True
    while looping:
        try:
            await bot.change_presence(status=discord.Status.idle)
            bot.loop.create_task(status_task())
            print('Logged in as')
            print(bot.user.name)
            print(bot.user.id)
            print('------')
            looping = False
        except ConnectionResetError:
            print ("ConnectionResetError: Ignoring..")
            pass

@bot.command()
async def hello(ctx):
    """Says world"""
    await ctx.send("world")


@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left + right)

bot.run(TOKEN)
