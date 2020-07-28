import discord
from discord.ext import commands
import datetime

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def harrybrokeit(self, ctx):
        await ctx.send("wow epix")

def setup(bot):
    bot.add_cog(Misc(bot))