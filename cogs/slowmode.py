import discord
from discord.ext import commands
import datetime

class Slowmode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, delay=3):
        current_time = datetime.datetime.now()
        if not 0 <= delay <= 21600:
            await ctx.send("Invalid delay. Please input delay between 0 (off) and 21600.")
        else:
            await ctx.channel.edit(slowmode_delay=delay)
            embed = discord.Embed(title="Slowmode changed!", description=f"The slowmode is now {delay}.")
            embed.set_footer(text="Requested by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
                current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Slowmode(bot))