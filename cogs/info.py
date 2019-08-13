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
import time
import datetime
import json

start_time = time.time()

class Info(commands.Cog):
        def __init__(self, bot):
                self.bot = bot

        @commands.command(aliases=['role-info'])
        @commands.cooldown(1, 3, commands.BucketType.user)
        async def roleinfo(self, ctx, role: discord.Role=None):
                if role is None:
                      return await ctx.send(f"**Ops... Try again with role mention or role name!**")
                if role.mentionable is True:
                      mention = "Yes"
                else:
                      mention = "No"
                if role.hoist is True:
                      hoist = "Yes"
                else:
                      hoist = "No"
                a = role.created_at
                b = ctx.message.created_at
                c = b-a
                embed = discord.Embed(title=role.name, color=role.color)
                embed.add_field(name="Created at", value=f'{a.strftime("%A, %B %d %Y @ %H:%M:%S %p")} ({c.days} days ago)', inline=True)
                embed.add_field(name="Mentionable", value=mention, inline=True)
                embed.add_field(name="ID", value=role.id, inline=True)
                embed.add_field(name="Color", value=role.color, inline=True)
                embed.add_field(name="Members in this role", value=len(role.members), inline=True)
                embed.add_field(name="Displayed separately", value=hoist)
                await ctx.send(embed=embed)

                                
        @commands.command()
        async def avatar(self, ctx, member: discord.Member = None):
            member = ctx.author if not member else member
            roles = [role for role in member.roles]

            embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f"{member}'s avatar:")
            embed.set_image(url=member.avatar_url)

            await ctx.send(embed=embed)
                                
        @commands.command(aliases=['about', 'botinfo'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def stats(self, ctx):
              bot = self.bot
              current_time = time.time()
              difference = int(round(current_time - start_time))
              text = str(datetime.timedelta(seconds=difference))

              embed = discord.Embed(title="Bot Info", color=0xe67e22)
              embed.add_field(name="Total Users", value=len(bot.users), inline=True)
              embed.add_field(name="Total Servers", value=len(bot.guilds), inline=True)
              embed.add_field(name=":crown: bot owner", value=f"<@445234723590242304>", inline=True)
              embed.add_field(name="Uptime", value=text, inline=True)
              embed.add_field(name="Commands", value=len(ctx.bot.commands), inline=True)
              embed.add_field(name='Created at', value=ctx.me.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"))
              embed.add_field(name="Library", value="discord.py", inline=True)
              embed.add_field(name="Discord.py API Version", value=discord.__version__, inline=True)
              embed.set_thumbnail(url=ctx.me.avatar_url)
              embed.timestamp = datetime.datetime.utcnow()
              embed.set_footer(text='Thank you for using goldenbot <3')
              await ctx.send(embed=embed)

        @commands.command()
        @commands.cooldown(1, 3, commands.BucketType.user)
        async def membercount(self, ctx):
            c = 0
            a = 0
            online = 0
            idle = 0
            dnd = 0
            offline = 0
            tonline = 0
            tidle = 0
            tdnd = 0
            toffline = 0
            n = ctx.guild.member_count
            for i in ctx.guild.members:
             if i.bot is True:
              c+=1
            for i in ctx.guild.members:
             if i.bot is False:
              a+=1
            for i in ctx.guild.members:
              if i.status.name == 'online':
                  online += 1
              if i.status.name == 'idle':
                  idle += 1
              if i.status.name == 'dnd':
                  dnd += 1
              if i.status.name == 'offline':
                  offline += 1
            for i in ctx.guild.members:
             if i.bot is False:
              if i.status.name == 'online':
                  tonline += 1
              if i.status.name == 'idle':
                  tidle += 1
              if i.status.name == 'dnd':
                  tdnd += 1
              if i.status.name == 'offline':
                  toffline += 1
              g = online + idle + dnd
              tg = tonline + tidle + tdnd
            ts = f"{tg}\n<:online:536240817602560010> Online - **{tonline}**\n<:dnd:536240817531125760> DND - **{tdnd}**\n<:idle:536240817522868224> Idle - **{tidle}**\n<:offline:536240817552228385> Offline - **{toffline}**"
            s = f"{g}\n<:online:536240817602560010> Online - **{online}**\n<:dnd:536240817531125760> DND - **{dnd}**\n<:idle:536240817522868224> Idle - **{idle}**\n<:offline:536240817552228385> Offline - **{offline}**"
            em = discord.Embed(color=discord.Colour.orange())
            em.add_field(name='Members', value=f'{n}', inline=True)
            em.add_field(name='Bots', value=f'{c}', inline=True)
            em.add_field(name='People', value=f'{a}', inline=True)
            em.add_field(name='Members Online', value=f'{s}', inline=True)
            em.add_field(name='People Online', value=f'{ts}', inline=True)
            em.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=em)

        @commands.command(aliases= ["whois", "uinfo", "playerinfo", "user-info", "memberinfo", "member-info", "info-user", "info"])
        @commands.cooldown(1, 3, commands.BucketType.user)
        async def userinfo(self, ctx, member: discord.Member=None):

            if member is None:
                    member = (ctx.author)
            if member.bot is True:
                  a = "Yes, he's a bot! :robot:"
            if member.bot is False:
                  a = "No, he's not a bot! :grinning:"
            if member.status.name == 'online':
                  b = "<:online:536240817602560010> Online"
            if member.status.name == 'idle':
                  b = "<:idle:536240817522868224> Idle"
            if member.status.name == 'dnd':
                  b = "<:dnd:536240817531125760> DND"
            if member.status.name == 'offline':
                  b = "<:offline:536240817552228385> Offline"
            if member.activity is None:
                  c = 'This user is not playing yet'
            if member.activity is not None:
                  c = member.activity.name
            if not member.is_on_mobile():
                  d = "No"
            if member.is_on_mobile():
                  d = "Yes"
            e = member.created_at
            f = ctx.message.created_at
            h = f-e
            i = member.joined_at
            j = f-i
            joinages = j.days
            ages = h.days
            try:
               embed = discord.Embed(title=f"{member}'s info", color=discord.Colour.blue())
               embed.set_author(name="Who is?")
               embed.add_field(name="Name", value=member.name)
               embed.add_field(name="Is this a bot?", value=a)
               embed.add_field(name="Status", value=b)
               embed.add_field(name="Playing", value=c)
               embed.add_field(name="User is on mobile?", value=d)
               embed.add_field(name="Tag", value=member.discriminator)
               embed.add_field(name="Top Role", value=member.top_role)
               embed.add_field(name="Nick", value=member.nick)
               embed.add_field(name="Joined", value=f"{i.strftime('%A, %B %d %Y @ %H:%M:%S %p')} ({joinages} days)")
               embed.add_field(name="Created at", value=f"{e.strftime('%A, %B %d %Y @ %H:%M:%S %p')} ({ages} days)")
               embed.add_field(name="Roles", value=', '.join(g.name for g in member.roles))
               embed.set_thumbnail(url=member.avatar_url)
               embed.set_footer(text=f'ID: {member.id}')
               embed.timestamp = datetime.datetime.utcnow()
               await ctx.send(embed=embed)
            except discord.HTTPException as uwu:
               embed = discord.Embed(title=f"{member}'s info", color=discord.Colour.blue())
               embed.set_author(name="Who is?")
               embed.add_field(name="Name", value=member.name)
               embed.add_field(name="Is this a bot?", value=a)
               embed.add_field(name="Status", value=b)
               embed.add_field(name="Playing", value=c)
               embed.add_field(name="User is on mobile?", value=d)
               embed.add_field(name="Tag", value=member.discriminator)
               embed.add_field(name="Top Role", value=member.top_role)
               embed.add_field(name="Nick", value=member.nick)
               embed.add_field(name="Joined", value=f"{i.strftime('%A, %B %d %Y @ %H:%M:%S %p')} ({joinages} days)")
               embed.add_field(name="Created at", value=f"{e.strftime('%A, %B %d %Y @ %H:%M:%S %p')} ({ages} days)")
               embed.add_field(name="Roles", value="This user's roles is too many.")
               embed.set_thumbnail(url=member.avatar_url)
               embed.set_footer(text=f'ID: {member.id}')
               embed.timestamp = datetime.datetime.utcnow()
               return await ctx.send(embed=embed)
        

               
  


        @commands.command(aliases= ["sinfo", "server_info"])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def serverinfo(self, ctx):
            c = 0
            a = 0
            g = 0
            online = 0
            idle = 0
            dnd = 0
            n = ctx.guild.member_count
            for i in ctx.guild.members:
             if i.bot is True:
              c+=1
            for i in ctx.guild.members:
             if i.bot is False:
              a+=1
            for i in ctx.guild.members:
              if i.status.name == 'online':
                  online += 1
              if i.status.name == 'idle':
                  idle += 1
              if i.status.name == 'dnd':
                  dnd += 1
              g = online + idle + dnd
            m = ctx.guild.created_at
            sugi = ctx.message.created_at
            o = sugi-m
            em = discord.Embed(color=discord.Colour.orange())
            em.add_field(name='Name', value=f'{ctx.author.guild.name}', inline=True)
            em.add_field(name='Owner', value=f'{ctx.author.guild.owner.mention} [{ctx.author.guild.owner.id}]', inline=True)
            em.add_field(name='Icon', value='Type `,servericon`', inline=True)
            em.add_field(name='Verification level', value=ctx.guild.verification_level, inline=True)
            em.add_field(name='Roles', value=f'{len(ctx.guild.roles)} `,sroles`', inline=True)
            em.add_field(name='Text Channels', value=f'{len(ctx.guild.channels)}', inline=True)
            em.add_field(name='Voice', value=f'{len(ctx.guild.voice_channels)}', inline=True)
            em.add_field(name='Members', value=f'{n}', inline=True)
            em.add_field(name='Bots', value=f'{c}', inline=True)
            em.add_field(name='People', value=f'{a}', inline=True)
            em.add_field(name='Online', value=f'{g}', inline=True)
            em.add_field(name='Created at', value=f'{m.strftime("%A, %B %d %Y @ %H:%M:%S %p")} ({o.days} days ago)', inline=True)
            em.add_field(name='Region', value=ctx.guild.region, inline=True)
            em.set_thumbnail(url=ctx.guild.icon_url)
            em.set_footer(text=f'ID: {ctx.guild.id}')
            em.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=em)

        @commands.command(aliases =['sicon'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def servericon(self, ctx):
            em = discord.Embed(title="", color=discord.Colour.blue())
            em.set_author(name=f"{ctx.guild.name}'s icon")
            em.set_image(url=ctx.guild.icon_url)
            em.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=em)



        @commands.command(aliases=['emojiavatar', 'iconemoji', 'avataremoji'])
        @commands.cooldown(1, 3, commands.BucketType.user)
        async def emojiicon(self, ctx, emoji: discord.Emoji):
            em = discord.Embed(color=discord.Colour.orange())
            em.set_image(url = f"{emoji.url}")
            await ctx.send(embed=em)
        
        @commands.command(aliases=['avdefault', 'avatard', 'avatar-default', 'avd'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def avatardefault(self, ctx, member: discord.Member=None):
            if member is None:
                 member = ctx.author
            owo = member.default_avatar_url
            em = discord.Embed(description=f'{member.mention}\'s [default avatar]({owo})', color=discord.Color.blurple())
            em.set_image(url=owo)
            await ctx.send(embed=em)

        @commands.command(aliases=['emoji_info', 'emoji info'])
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def emojiinfo(self, ctx, emoji: discord.Emoji):
            a = emoji.created_at
            b = ctx.message.created_at
            c = b-a
            await ctx.send(f'`Name:` {emoji.name}\n`ID:` {emoji.id}\n`Preview:` {emoji} (`{emoji}`)\n`URL:` {emoji.url}\n`Created at:` {a.strftime("%A, %B %d %Y @ %H:%M:%S %p")} ({c.days} days ago)')


def setup(bot):
        bot.add_cog(Info(bot))
