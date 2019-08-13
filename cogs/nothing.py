import discord
import logging
from discord.utils import get
from discord.ext.commands import Bot, Greedy
from discord.ext import commands
from itertools import cycle
import time
import typing
import random
import asyncio
import aiohttp
import os
import ast
from youtube_dl import YoutubeDL
import praw
import asyncpg

            
from setuptools import setup, find_packages

import json
import re
import urllib.request

        
prefix="f!"
bot = commands.Bot(prefix)
bot.load_extension("cogs.music")
bot.load_extension("cogs.economy")

async def create_db_pool():
    bot.pg_con = await asyncpg.create_pool(database="trash", user="postgres", password="amazigh20")

async def play_():
        await bot.wait_until_ready()
        while not bot.is_closed():
            a = 0
            for i in bot.guilds:
                for u in i.members:
                    if u.bot == False:
                        a = a + 1

            await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="candy crush"))
            await asyncio.sleep(5)
            await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="to other moms talking about children"))
            await asyncio.sleep(5)
            await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=f"vids about ho to take care of children"))
            await asyncio.sleep(5)
            await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=f"vids about how to cook lasagna"))
            




bot.loop.run_until_complete(create_db_pool())
bot.loop.create_task(play_())
with open(r'C:\Users\golde\OneDrive\Bureau\hackweek bot\data\config.json') as f:
    r = json.load(f)
bot.run("NjAzNzAxMDE4MTIyNzgwNjky.XTjQqQ.xFSAbBrrSSNunVuTnyBSHGWQsXw")

f.close()
