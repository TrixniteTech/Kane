import discord
from discord.ext import commands
import datetime
import psutil
from pathlib import Path
from psutil import virtual_memory

class System(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['si', 'server', 'harryserver', 'sinfo', 'system'])
    async def systeminfo(self, ctx):
        if ctx.author.id == 428450288668508160:
                ram_usage = round(psutil.virtual_memory().percent,1)
                cpu_usage = round(psutil.cpu_percent(),1)
                disk = psutil.disk_usage('/')
                if cpu_usage < 49:
                    embed=discord.Embed(color=0x35e35c)
                    embed.add_field(name="Memory usage:", value=str(ram_usage)+"%", inline=True)
                    embed.add_field(name="CPU usage:", value=str(cpu_usage)+"%", inline=True)
                    embed.add_field(name="Core used:", value=str(psutil.Process().cpu_num()), inline=False)
                    embed.add_field(name="Process:", value=str(psutil.Process().exe()), inline=False)
                    embed.add_field(name="Disk used:", value=str(disk.percent) + "%", inline=False)
                    embed.add_field(name="Boot time:", value=str(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")), inline=False)
                    await ctx.send(embed=embed)
                else:
                    embed=discord.Embed(color=0xeb452e)
                    embed.add_field(name="Memory usage:", value=str(ram_usage)+"%", inline=True)
                    embed.add_field(name="CPU usage:", value=str(cpu_usage)+"%", inline=True)
                    embed.add_field(name="Core used:", value=str(psutil.Process().cpu_num()), inline=False)
                    embed.add_field(name="Process:", value=str(psutil.Process().exe()), inline=False)
                    embed.add_field(name="Boot time:", value=str(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")), inline=False)
                    await ctx.send(embed=embed)        

    @commands.command()
    async def reload(self, ctx, item="all"):
        if ctx.author.id == 428450288668508160:
            if item == "all":
                cogs = [x.stem for x in Path('cogs').glob('*.py')]
                for extension in cogs:
                    try:
                        self.bot.reload_extension(f'cogs.{extension}')
                        print(f'reloaded {extension}')
                        embed=discord.Embed(title=f"reloaded {extension}", color=0x35e35c)
                        await ctx.send(embed=embed)
                    except Exception as e:
                        error = f'{extension}\n {type(e).__name__} : {e}'
                        print(f'failed to reload extension {error}')
                        embed=discord.Embed(title=f"failed to reload extension {error}", color=0xeb452e)
                        await ctx.send(embed=embed)
                    print('-' * 10)
            else:
                try:
                    self.bot.reload_extension(f'cogs.{item}')
                    print(f'reloaded {item}')
                    embed=discord.Embed(title=f"reloaded {item}", color=0x35e35c)
                    await ctx.send(embed=embed)
                except Exception as e:
                    error = f'{item}\n {type(e).__name__} : {e}'
                    print(f'failed to reload extension {error}')
                    embed=discord.Embed(title=f"failed to reload extension {error}", color=0xeb452e)
                    await ctx.send(embed=embed)
                print('-' * 10)
                




def setup(bot):
    bot.add_cog(System(bot))