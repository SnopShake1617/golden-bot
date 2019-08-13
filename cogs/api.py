import discord
import random
from discord.ext import commands
import logging
import traceback
from datetime import datetime
import asyncio
import os
import aiohttp
from discord import opus
from asyncio import sleep
import datetime
import json



class API(commands.Cog):
        def __init__(self, bot):
                self.bot = bot




        @commands.command(aliases=['shibainu'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def shiba(self, ctx):
                async with aiohttp.ClientSession() as cs:
                        async with cs.get('http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=false') as r:
                                res = await r.json()
                                embed = discord.Embed(color=0x000000)
                                embed.title = "Awww, a doge!"
                                embed.set_image(url=str(res).strip("[']"))
                                embed.set_footer(text=f"{self.bot.user.name}")
                                embed.timestamp = datetime.datetime.utcnow()
                                await ctx.send(embed=embed)




        @commands.command(aliases=['woof'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def dog(self, ctx):
                async with aiohttp.ClientSession() as cs:
                        async with cs.get("http://random.dog/woof.json") as r:
                                res = await r.json()
                                embed = discord.Embed(color=0x000000)
                                embed.title = '\U0001f436 Woof!'
                                embed.set_image(url=res['url'])
                                embed.set_footer(text=f"{self.bot.user.name}")
                                embed.timestamp = datetime.datetime.utcnow()
                                await ctx.send(embed=embed)



        @commands.command(aliases=['meow'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def cat(self, ctx):
                async with aiohttp.ClientSession() as cs:
                        async with cs.get('https://some-random-api.ml/img/cat') as r:
                                res = await r.json()
                                embed = discord.Embed(color=0x000000)
                                embed.title = "\U0001f431 Meoww...!"
                                embed.set_image(url=res['link'])
                                embed.set_footer(text=f"{self.bot.user.name}")
                                embed.timestamp = datetime.datetime.utcnow()
                                await ctx.send(embed=embed)



def setup(bot):
        bot.add_cog(API(bot))
