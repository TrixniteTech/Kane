import discord
from discord.ext import commands
import datetime

class InviteGen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invitegen(self, ctx, id=734839312675242116):
        await ctx.send(f"https://discord.com/api/oauth2/authorize?client_id={id}&permissions=8&scope=bot")

def setup(bot):
    bot.add_cog(InviteGen(bot))