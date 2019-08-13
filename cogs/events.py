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
import datetime
from youtube_dl import YoutubeDL
from discord import opus
from asyncio import sleep
import sqlite3
import logging
from datetime import datetime
import random
from discord import opus
import traceback

class Greetings(commands.Cog, name="jin-leave"):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention} make sure to read the rules.'.format(member))
            
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        channel = self.bot.get_channel(605698279975419904)
        embed = discord.Embed(title=f"some command got an error:", color=discord.Color.red(), timestamp=ctx.message.created_at)
        embed.add_field(name="guild:", value=ctx.message.guild, inline=False)
        embed.add_field(name="author:", value=ctx.message.author, inline=False)
        embed.add_field(name="command:", value=ctx.message.content, inline=False)
        embed.add_field(name="error:", value=error)
        await channel.send(embed=embed)


    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        channel = after.channel
        e = discord.Embed(title=f"a message got edited by {after.author}", color=discord.Color.red(), timestamp=after.created_at)
        e.add_field(name="before:", value=before.content, inline=False)
        
        e.add_field(name="after:", value=after.content, inline=False)
        
        e.add_field(name="from:", value=f"{channel}",inline=False)
        ch = discord.utils.get(after.guild.channels, name="golden-logs")
        await ch.send(embed=e)
        
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = message.channel
        embed = discord.Embed(title=f"a message got deleted", color=discord.Color.red(), timestamp=message.created_at)
        embed.add_field(name="author:", value=f"{message.author.mention}",inline=False)
        
        embed.add_field(name="Message:", value=message.content, inline=False)
        
        embed.add_field(name="from:", value=f"{channel}", inline=False)
        ch = discord.utils.get(message.guild.channels, name="golden-logs")
        await ch.send(embed=embed)


    @commands.Cog.listener()
    async def on_member_remove(self, member, args="no reason"):
        ch = discord.utils.get(member.guild.channels, name="golden-logs")
        guild = member.guild
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'{member} just left the server lets hope he/she comes back'.format(member))

    @commands.Cog.listener()
    async def on_member_ban(self, guild, member, args="no reason"):
        ch = discord.utils.get(member.guild.channels, name="golden-logs")
        async for entry in guild.audit_logs(action=discord.AuditLogAction.ban):
            embed = discord.Embed(title=f"{entry.target} got banned:".format(entry), color=discord.Color.red())
            embed.add_field(name="by:", value=f"{entry.user}".format(entry),inline=False)
            
            embed.add_field(name="reason:", value=args, inline=False)
            await ch.send(embed=embed)
            await self.bot.process_commands()
        

    @commands.Cog.listener()
    async def on_member_unban(self, guild, member, args="no reason"):
        ch = discord.utils.get(guild.channels, name="golden-logs")
        async for entry in guild.audit_logs(action=discord.AuditLogAction.unban):
            embed = discord.Embed(title=f"{entry.target} got unbanned:".format(entry), color=discord.Color.red())
            embed.add_field(name="by:", value=f"{entry.user}".format(entry),inline=False)
            
            embed.add_field(name="reason:", value=args, inline=False)
            await ch.send(embed=embed)
            await self.bot.process_commands()
    




def setup(bot):
    bot.add_cog(Greetings(bot))
