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
import requests
import ast
import json
from youtube_dl import YoutubeDL
import sqlite3 
from utils.HelpPaginator import HelpPaginator, CannotPaginate

bot = commands.Bot(command_prefix="e!")


bot.remove_command("help")
bot.load_extension("cogs.errorhandle")
bot.load_extension("cogs.other")
bot.load_extension("cogs.mod")
bot.load_extension("cogs.math")
bot.load_extension("cogs.xoxo")
bot.load_extension("cogs.hehe")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.info")
bot.load_extension("cogs.events")
bot.load_extension("cogs.dbl")
 
@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping =  round(ping_ * 1000)
    await ctx.send(f"my ping is {ping}ms")

@bot.event
async def on_ready():
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS main(
        guild_id TEXT,
        msg TEXT,
        channel_id TEXT
        )
        ''')
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')









@bot.command()
async def logout(ctx):
    ath=ctx.message.author.id
    if ath==445234723590242304:
        await ctx.send("Bye nubs")
        await bot.logout()
    else:
        await ctx.send("only the owner can use this command")
        pass












@bot.command()
async def nothing(ctx):
    msg = await ctx.send("u gay dont waste my time >:c")
    await msg.edit(content = "u fking gay why bully me ;(")
    await msg.edit(content = "plox leave me alone palis")
    await msg.edit(content = "leave me alone and i will give u my phone number c:")
    await msg.edit(content = "jk no one gonna have my number even ma owner wont ;p")
    await msg.delete()


@bot.command() 
async def vote(ctx):
    emoji='👍', '👎'
    for e in emoji:
        await ctx.message.add_reaction(e)



@bot.command()
async def server(ctx):
    await ctx.send("https://discord.gg/Qh6AVR8")

@bot.command()
async def wtf(ctx):
    await ctx.send("https://1.bp.blogspot.com/-8o693FmtIUo/W4qw1dQjshI/AAAAAAAACC8/CY_uwkvWG8U-JtWiWrZWPhPLyCbtywxVACLcBGAs/s320/FB_IMG_15351295134003148.jpg")

@bot.command()
async def invite(ctx):
    await ctx.send("https://discordapp.com/oauth2/authorize?client_id=481489864626536458&permissions=8&scope=bot")


















@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def help(ctx, *, command: str = None):
    """Shows help about a command or the bot"""
    try:
        if command is None:
            p = await HelpPaginator.from_bot(ctx)
        else:
            entity = self.bot.get_cog(command) or self.bot.get_command(command)

            if entity is None:
                clean = command.replace('@', '@\u200b')
                return await ctx.send(f'Command or category "{clean}" not found.')
            elif isinstance(entity, commands.Command):
                p = await HelpPaginator.from_command(ctx, entity)
            else:
                p = await HelpPaginator.from_cog(ctx, entity)

        await p.paginate()
    except Exception as e:
        await ctx.send(e)












async def play_():
        await bot.wait_until_ready()
        while not bot.is_closed():
            a = 0
            for i in bot.guilds:
                for u in i.members:
                    if u.bot == False:
                        a = a + 1
            await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="with everyone"))
            await asyncio.sleep(15)
            await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="everyone's secrets"))
            await asyncio.sleep(15)
            await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="ur mom"))
            await asyncio.sleep(15)
            await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.users)} taking a shower"))
            await asyncio.sleep(15)
            await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=f"everyone's mom having sex"))



bot.loop.create_task(play_())
with open(r'data/config.json') as f:
    r = json.load(f)
bot.run(str(os.environ.get("BOT_TOKEN")))
f.close()
