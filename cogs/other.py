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



class other(commands.Cog, name='other'):
    

    def __init__(self, bot):
        self.bot = bot
  
    @commands.command()
    async def suggest(self, ctx, *, args):
        pro = self.bot.get_channel(553233309371727884)
        embed = discord.Embed(title=f"a suggestion has been added by {ctx.message.author}", colour=discord.Colour.green())
        embed.add_field(name="suggestion:", value=args)
        msg = await pro.send(embed=embed)
        await ctx.send("suggestion successfuly sent")
        emoji='👍', '👎'
        for e in emoji:           
            await msg.add_reaction(e)
        
def setup(bot):
    bot.add_cog(other(bot))
