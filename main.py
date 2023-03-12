from discord.ext import commands
import discord

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Ready !")

@bot.command()
async def coucou(ctx):
    await ctx.send("🍣 Coucou !")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! Latency: {round(bot.latency * 1000)}ms")

@bot.command()
async def ping(ctx):
    await ctx.send(f"La latence du bot est de {round(bot.latency * 1000)}ms")

@bot.command()
async def sushi(ctx):
    await ctx.send("https://img.freepik.com/premium-photo/set-sushi-rolls-with-eel-salmon-avocado-cucumber-nori-leaves-cream-cheese-inside-isolated-white_85601-187.jpg")

bot.run("")
