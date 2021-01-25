from discord.ext import commands
from discord.ext.commands import has_permissions
import discord

import helpers

class utilities(commands.Cog):
    '''a bunch of useful tools'''
    @commands.command()
    @has_permissions(manage_messages=True) 
    async def clear(self, ctx, amount):
        '''clear a number of messages'''
        print(amount)
        await ctx.channel.purge(limit=int(amount) + 1)
