from discord.ext import commands
import discord

import requests
import json

import helpers

@commands.command()
async def version(ctx):
    '''fetch the version of this bot'''
    await ctx.send(embed=discord.Embed(
            title="SWC Python Bot",
            description="1.0"))

@commands.command()
async def git(ctx, name=None):
    '''fetch information from a git repository on our official github organization (SWC-Python-Club)''' 
    if name is None:
        await ctx.send(embed=helpers.ArgumentError(1).as_embed())
        return
    repositories = requests.get("https://api.github.com/orgs/SWC-Python-Club/repos")
    print(repositories.json())
    if name not in repositories.json():
        await ctx.send(embed=discord.Embed(
            title="Error",
            description="unable to fetch repository"))
    else:
        pass
