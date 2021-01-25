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

def read_repo_data(repo):
    log("reading repo data...")
    print(repo)
    print(datetime.datetime.strptime(repo["updated_at"], "%Y-%m-%dT%H:%M:%SZ"))
    last_commit = datetime.datetime.strptime(repo["updated_at"], "%Y-%m-%dT%H:%M:%SZ")
    created = datetime.datetime.strptime(repo["created_at"], "%Y-%m-%dT%H:%M:%SZ")
    log("fetched information...")
    language = max(requests.get(repo["languages_url"]).json())
    fetch = discord.Embed(title=repo["full_name"], description="https://github.com/" + repo["full_name"] + "\n\n" + repo["description"])
                
    fetch.set_thumbnail(url=get_google_img(language + " lang icon png"))
    fetch.add_field(name="created", value=created.strftime('%A %b %d, %Y at %H:%M GMT'), inline=True)
    fetch.add_field(name="last commit", value=last_commit.strftime('%A %b %d, %Y at %H:%M GMT'), inline=True)
    fetch.add_field(name="owner", value=repo["owner"]["login"], inline=True)

    fetch.add_field(name="main language", value=language)
    log("sucessfully fetched information about " + repo["full_name"])
    return fetch               


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
        
        if "/" in name:
            repositories = requests.get("https://api.github.com/repos/" + name)
            await ctx.send(embed=read_repo_data(repositories.json()))
            print("https://api.github.com/repos/" + name)
            return
        else:
            repositories = requests.get("https://api.github.com/orgs/SWC-Python-Club/repos")

        for repo in repositories.json():
            if name.lower() in repo["name"].lower():
                await ctx.send(embed=read_repo_data(repo))
                return
        log("could not locate repository")
        await ctx.send(embed=discord.Embed( 
            title="Error",
            description="unable to fetch repository"))
    
    @commands.command()
    async def python(self, ctx, query):
        '''fetch help from the official python documentation'''
