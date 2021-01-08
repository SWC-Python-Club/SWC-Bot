import discord
from discord.ext import commands

import requests
import json

bot = commands.Bot(command_prefix='$')

@bot.command()
async def version():
    await ctx.send(embed=discord.Embed(
            title="SWC Python Bot",
            description="1.0"))

@bot.command()
async def git(name):
    repositories = requests.get("https://api.github.com/orgs/SWC-Python-Club/repos")
    if name not in json.dump(repositories):
        ctx.send(embed=discord.Embed(
            title="Error",
            description="unable to fetch repository"))
    else:
        pass

