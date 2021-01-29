#!../bin/python3

import discord
from discord.ext import commands, tasks

import requests
from requests.auth import HTTPBasicAuth

import json
import os
import datetime

import utilities
import fetches
import helpers
from helpers import log

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
    if message.content  == "...":
        return

    if message.author != bot.user:
        if "vim" in message.content.lower():
            await message.channel.send("The best editor!!!")
       
        await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        log("Unrecognized Command!!") 
        await ctx.send(embed=helpers.UnknownCommandError(ctx.message.content).embed())

@bot.event
async def on_ready():
    requests.get('https://api.github.com/', auth=HTTPBasicAuth('AndreiSva', os.environ["passwd"]))
    log("bot successfully authenticated")
    bot.add_cog(fetches.fetches())
    bot.add_cog(utilities.utilities())

    bot.add_cog(event_cog())
    await bot.change_presence(activity=discord.Game(name=prefix + "help"))


class event_cog(commands.Cog):
    def __init__(self):
        self.mario_death.start()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention} to the SWC Python Club!!!'.format(member))

    @tasks.loop(hours=24)
    async def mario_death(self):
        log("mario is dying")
        mario_death = datetime.date(2021, 3, 31)
        channel = bot.guilds[0].get_channel(796905868343902239)
        
        days = mario_death - datetime.date.today() 
        print(days.days)
        if days.days > 1:
            await channel.send(f"mario will die in {days.days} days")
        elif days.days == 1:
            await channel.send(f"mario will die tomorrow")
        else:
            return
        

log("starting bot")
log("bot online")
bot.run(os.environ["token"])
