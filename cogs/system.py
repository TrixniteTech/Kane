import discord
from discord.ext import commands
import datetime
import psutil

class System(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def systeminfo(self, ctx):
        if ctx.author.id == 428450288668508160:
                cpu_per = round(psutil.cpu_percent(),1) # Get CPU Usage
                mem = psutil.virtual_memory()
                mem_per = round(psutil.virtual_memory().percent,1)
                embed=discord.Embed(title="Server stats")
                embed.add_field(name="Memory usage:", value=str(mem_per)+"%", inline=False)
                embed.add_field(name="CPU usage:", value=str(cpu_per)+"%", inline=True)
                await ctx.send(embed=embed)
                




def setup(bot):
    bot.add_cog(System(bot))