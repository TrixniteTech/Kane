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

def setup(bot):
    bot.add_cog(Moderation(bot))
