from discord.ext import commands
import discord

import requests
from requests.auth import HTTPBasicAuth

import os
import json
import datetime
import operator

import helpers
from helpers import log

from gimages import get_google_img

import subprocess

class fetches(commands.Cog):
    '''a set of tools to display information about a number of things'''
    @commands.command()
    async def git(self, ctx, name=None):
        '''fetch information from a git repository on our official github organization (SWC-Python-Club)'''
        log(name)
        if name is None:
            log("arg err")
            await ctx.send(embed=helpers.ArgumentError(0, 1).as_embed())
            return
        repositories = requests.get("https://api.github.com/orgs/SWC-Python-Club/repos")
        for repo in repositories.json():
            if name.lower() in repo["name"].lower():
                last_commit = datetime.datetime.strptime(repo["updated_at"], "%Y-%m-%dT%H:%M:%SZ")
                created = datetime.datetime.strptime(repo["created_at"], "%Y-%m-%dT%H:%M:%SZ")
                language = max(requests.get(repo["languages_url"]).json())
        
                fetch = discord.Embed(title=repo["full_name"], description="https://github.com/" + repo["full_name"] + "\n\n" + repo["description"])
                
                # this is an absolutely atrocious way of doing this... but I've already spent 2 hours trying to get this to work in a better way :/ 
                fetch.set_thumbnail(url=subprocess.run(['~/Downloads/git/SWC-Bot/src/gimages.py', '{language} Programming Language Icon PNG'], stdout=subprocess.PIPE).stdout)
                fetch.add_field(name="created", value=created.strftime('%A %b %d, %Y at %H:%M GMT'), inline=True)
                fetch.add_field(name="last commit", value=last_commit.strftime('%A %b %d, %Y at %H:%M GMT'), inline=True)
                fetch.add_field(name="owner", value=repo["owner"]["login"], inline=True)

                fetch.add_field(name="main language", value=language)
                await ctx.send(embed=fetch)
               
                log("sucessfully fetched information about " + repo["full_name"])
                return
        log("could not locate repository")
        await ctx.send(embed=discord.Embed( 
            title="Error",
            description="unable to fetch repository"))
