import discord
from discord.ext import commands
import datetime

class Impersonate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def impersonate(self, ctx, user:discord.User, *, message):
        await ctx.send("Under development")

def setup(bot):
    bot.add_cog(Impersonate(bot))