from discord.ext import commands
import discord

import requests
import json

import helpers

class fetches(commands.Cog):
    '''a set of tools to display about a number of things'''
    @commands.command()
    async def git(ctx, name=None):
        '''fetch information from a git repository on our official github organization (SWC-Python-Club)''' 
        if name is None:
            await ctx.send(embed=helpers.ArgumentError(1).as_embed())
            return
        repositories = requests.get("https://api.github.com/orgs/SWC-Python-Club/repos")
        for repo in repositories.json():
            if name in repo["name"]:
                pass
                return
        await ctx.send(embed=discord.Embed( 
            title="Error",
            description="unable to fetch repository"))
