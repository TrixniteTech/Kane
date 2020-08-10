import discord
from discord.ext import commands
import datetime

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        current_time = datetime.datetime.now()
        embed = discord.Embed(title=f"You kicked {discord.Member}", description=f"Reason: {reason}", color=0x0692ea)
        embed.set_author(name="Member Successfully Kicked")
        embed.set_footer(text="User kicked by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
            current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        await member.kick(reason=reason)
        
        
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{ctx.author.mention} You should have mentioned the user to be kicked!') 
        
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{ctx.author.mention} Uh oh! You have no permission to use this command!')    

        else:
            raise(error)
        
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        current_time = datetime.datetime.now()
        embed = discord.Embed(title=f"You banned {discord.Member}", description=f"Reason: {reason}", color=0x0692ea)
        embed.set_author(name="Member Successfully Banned")
        embed.set_footer(text="User kicked by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
            current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        await member.ban(reason=reason)
        
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{ctx.author.mention}You should have mentioned the user to be banned!')   
        
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{ctx.author.mention}  Uh oh! You have no permission to use this command!')    

        else:
            raise(error)        

def setup(bot):
    bot.add_cog(Moderation(bot))
