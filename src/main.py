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

@bot.command()
async def version(ctx):
    '''fetch the version of this bot'''
    await ctx.send(embed=discord.Embed(
            title="SWC Python Bot",
            description="1.0"))

@bot.event
async def on_message(message):
    if message.author != bot.user:
        if "vim" in message.content.lower():
            await message.channel.send("The best editor!!!")
    
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print("Unrecognized command")
        await ctx.send(embed=discord.Embed(
            title="Error",
            description="Unrecognized command!!!",
            color=0xff0000
            ))

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=prefix + "help"))

bot.add_cog(git.fetches())
bot.run(os.environ["token"])
