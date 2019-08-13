import discord
from discord.ext import commands

class errorhandle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            return await ctx.send(f':no_entry:  | This command is on cooldown... **[{int(error.retry_after)} seconds]**')
        if isinstance(error, commands.NotOwner):
            return await ctx.send('**You do not own this bot!**')
        if isinstance(error, commands.BadArgument):
            return await ctx.send(f'**{error}**')
        if isinstance(error, commands.MissingPermissions):
            return await ctx.send('**You are missing permission to execute this command!**')
        if isinstance(error, commands.BotMissingPermissions):
            return await ctx.send('**I am missing permission to perform this command!**')

            raise error



def setup(bot):
    bot.add_cog(errorhandle(bot))


