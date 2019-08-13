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
import os
import ast
import json
from utils.HelpPaginator import HelpPaginator, CannotPaginate



class math(commands.Cog):
        def __init__(self, bot):
                self.bot = bot

        @commands.command()
        async def add(self, ctx, a: int, b: int):
            await ctx.send(a + b)

        
        @commands.command()
        async def remove(self, ctx, a: int, b: int):
            await ctx.send(a - b)           

        @commands.command()
        async def multiply(self, ctx, a: int, b: int):
            await ctx.send(a * b)

        @commands.command()
        async def devide(self, ctx, a: int, b: int):
            await ctx.send(a / b)


def setup(bot):
        bot.add_cog(math(bot))
