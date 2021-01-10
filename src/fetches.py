from discord.ext import commands
import discord

import requests
import json

import helpers

class fetches(commands.Cog):
    '''a set of tools to display about a number of things'''
    @commands.command()
    async def git(self, ctx, name=None):
        '''fetch information from a git repository on our official github organization (SWC-Python-Club)'''
        print(name)
        if name is None:
            print("arg err")
            await ctx.send(embed=helpers.ArgumentError(0, 1).as_embed())
            return
        repositories = requests.get("https://api.github.com/orgs/SWC-Python-Club/repos")
        for repo in repositories.json():
            if name in repo["name"]:
                print(name)
                print(repo)
                return
        await ctx.send(embed=discord.Embed( 
            title="Error",
            description="unable to fetch repository"),
            color=helpers.colors["error"]
            )
