#!../bin/python3

import discord
from discord.ext import commands

import requests
import json
import os

import git

import helpers

prefix = '.'
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=prefix + "help"))

bot.add_command(git.version)
bot.add_command(git.git)
bot.run(os.environ["token"])
