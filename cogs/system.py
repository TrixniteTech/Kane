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

    @commands.command()
    async def reload(self, ctx):
        if ctx.author.id == 428450288668508160:
            cogs = [x.stem for x in Path('cogs').glob('*.py')]
            for extension in cogs:
                try:
                    self.reload_extension(f'cogs.{extension}')
                    print(f'reloaded {extension}')
                except Exception as e:
                    error = f'{extension}\n {type(e).__name__} : {e}'
                    print(f'failed to reload extension {error}')
                print('-' * 10)
                




def setup(bot):
    bot.add_cog(System(bot))