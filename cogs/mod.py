import discord
import random
from discord.ext import commands
import logging
import traceback
from datetime import time
import asyncio
import os
import aiohttp
from discord import opus
from asyncio import sleep
import datetime
import json

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    def timeout(self, time):
        if time.endswith("s"):
            time = time.replace("s", "")
            return int(time)
        elif time.endswith("m"):
            time = time.replace("m", "")
            time = int(time)
            return time * 60
        elif time.endswith("h"):
            time = time.replace("h", "")
            time = int(time)
            return time * 60 * 60
        elif time.endswith("d"):
            time = time.replace("d", "")
            time = int(time)
            return time * 60 * 60 * 24
        elif time.endswith("w"):
            time = time.replace("w", "")
            time = int(time)
            return time * 60 * 60 * 24 * 7

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member, args="no reason"):
        ch = discord.utils.get(ctx.guild.channels, name="golden-logs")
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'unbanned {user.mention}')
                embed = discord.Embed(title=f"{member} got unbanned", color=discord.Color.red(), timestamp=ctx.message.created_at)
                embed.add_field(name="by:", value=ctx.message.author, inline=False)             
                embed.add_field(name="reason:", value=args, inline=False)
                await ch.send(embed=embed)
                return
            
     
    @commands.group(invoke_without_command=True)
    @commands.has_permissions(manage_roles=True)
    async def mutedrole(self, ctx):
        await ctx.send("commands are:\ncreate\ndelete")
        
    @mutedrole.command()
    @commands.has_permissions(manage_roles=True)
    async def create(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name="muted")
        if role is not None:
            await ctx.send("role already exists")
        else:        
            guild = ctx.message.guild
            await guild.create_role(name="muted")
            await ctx.send("muted role created successfuly")
        
    @mutedrole.command()
    @commands.has_permissions(manage_roles=True)
    async def delete(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name="muted")
        if role is None:
            await ctx.send("role doesnt exist")
        else:
            await role.delete()
            await ctx.send("muted role got deleted")
    
    





    

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member = None, *, args="no reason"):
        ch = discord.utils.get(ctx.guild.channels, name="golden-logs")
        if member ==None or member ==ctx.message.author:
            await ctx.send("i wont ban u")
            return
        if args == None:
            args = "no reason at all!"
        message = f"you have been banned from {ctx.guild.name} for {args}"
        await member.send(message)
        await ctx.guild.ban(member)
        await ctx.send(f"{member} is banned by{ctx.author.mention} for {args}")
        embed = discord.Embed(title=f"{member} got banned", color=discord.Color.red(), timestamp=ctx.message.created_at)
        embed.add_field(name="by:", value=ctx.message.author)
        
        embed.add_field(name="reason:", value=args,inline=False)
        await ch.send(embed=embed)


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member = None, *, args="no reason"):
        ch = discord.utils.get(ctx.guild.channels, name="golden-logs")
        if member ==None or member ==ctx.message.author:
            await ctx.send("identify who u want to kick")
            return
        if args == None:
            args = "no reason at all!"
        message = f"you have been kicked from {ctx.guild.name} for {args}"
        await member.send(message)
        await ctx.guild.ban(member)
        await ctx.send(f"{member} is kicked by{ctx.author.mention} for {args}")
        embed = discord.Embed(title=f"{member} got kicked", color=discord.Color.red(), timestamp=ctx.message.created_at)
        embed.add_field(name="by:", value=ctx.message.author,inline=False)
        
        embed.add_field(name="reason:", value=args,inline=False)
        await ch.send(embed=embed)
 




    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member:discord.Member):
        ch = discord.utils.get(ctx.guild.channels, name="golden-logs")
        role = discord.utils.get(member.guild.roles, name = "muted")
        await member.remove_roles(role)
        await ctx.send("member unmuted successfuly")
        embed = discord.Embed(title=f"{member} got unmuted:", color=discord.Color.red(), timestamp=ctx.message.created_at)
        embed.add_field(name="by:", value=ctx.message.author)
        await ch.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member:discord.Member, time: str, *, args="no reason"):
        ch = discord.utils.get(ctx.guild.channels, name="golden-logs")
        role = discord.utils.get(member.guild.roles, name = "muted")
        embed = discord.Embed(title=f"{member} got muted:", color=discord.Color.red(), timestamp=ctx.message.created_at)
        embed.add_field(name="by:", value=ctx.message.author,inline=False)
        embed.add_field(name="duration:", value=time, inline=False)
        embed.add_field(name="reason:", value=args, inline=False)
        await ch.send(embed=embed)
        await member.add_roles(role)
        await ctx.send(f"member muted successfuly")
        await asyncio.sleep(self.timeout(time))
        await member.remove_roles(role)
        return

        


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self ,ctx, amount: int):
        channel = ctx.message.channel
        ch = discord.utils.get(ctx.guild.channels, name="golden-logs")
        await ctx.channel.purge(limit=amount + 1)
        msg = await ctx.send(f"successfuly cleared {amount} messages", delete_after=5)
        embed = discord.Embed(title=f"a channel got pruned:", color=discord.Color.red(), timestamp=ctx.message.created_at)
        embed.add_field(name="channel:", value=f"{channel}",inline=False)
        
        embed.add_field(name="by:", value=ctx.message.author,inline=False)
        
        embed.add_field(name="amount:", value=amount,inline=False)
        await ch.send(embed=embed)

    @commands.command(aliases=["echo"])
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, words):
        await ctx.send(words)
        await ctx.message.delete()

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("you need to specify the amount")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("give an integer")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("you dont have permissions to use this command")

        raise error
    


    @ban.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("you have to specify the member")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("you have to specify the member")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("you dont have permissions to use this command")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send('I am missing permission to perform this command!')

        raise error

    @kick.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("you have to specify the member")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("you have to specify the member")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("you dont have permissions to use this command")
        if isinstance(error, commands.BotMissingPermissions):
            return await ctx.send('I am missing permission to perform this command!')


        raise error

    @say.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("what message do u want me to say?")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("you dont have permissions to use this command")

        raise error
        
    @unban.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("you have to specify the member's name and tag")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("you have to specify the member's name and tag")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("you dont have permissions to use this command")


        raise error
        
    @unban.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("you have to specify the member's name and tag")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("you have to specify the member's name and tag")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("you dont have permissions to use this command")
        if isinstance(error, commands.BotMissingPermissions):
            return await ctx.send('I am missing permission to perform this command!')


        raise error

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member:discord.User = None, *, args="Nothing"):
        if member ==None or member ==ctx.message.author:
            await ctx.send("idntify who u want to warn")
            return
        if reason ==None:
            reason = "no reason at all"
        await ctx.send(f"{member} is warned by {ctx.author.mention} for {args}")



def setup(bot):
    bot.add_cog(mod(bot))
