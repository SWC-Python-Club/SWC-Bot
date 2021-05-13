from discord.ext import commands
from discord.ext.commands import has_permissions
import discord
import datetime

import helpers

cooldowns = {}

class utilities(commands.Cog):
    '''a bunch of useful tools'''
    @commands.command()
    @has_permissions(manage_messages=True) 
    async def clear(self, ctx, amount):
        '''clear a number of messages'''
        print(amount)
        await ctx.channel.purge(limit=int(amount) + 1)

    @commands.command()
    async def summonjoe(self, ctx):
        if ctx.author.id not in cooldowns:
            cooldowns[ctx.author.id] = datetime.datetime(2021, 3, 31) 
            helpers.log("adding new user to cooldowns")
            print(cooldowns)
        print((cooldowns[ctx.author.id] - datetime.datetime.now()).total_seconds())
        if (datetime.datetime.now() - cooldowns[ctx.author.id]).total_seconds() >= 10:
            cooldowns[ctx.author.id] = datetime.datetime.now()
            for i in range(3):
                await ctx.send("<@621907351267442698>")
        else:
            await ctx.send(embed=helpers.error("cooldown", "this command is on a cooldown!!!").embed())
