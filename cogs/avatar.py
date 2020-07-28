import discord
from discord.ext import commands


class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, *, avamember: discord.Member = None):
        userAvatarUrl = avamember.icon_url
        await ctx.send(userAvatarUrl)

    @commands.command()
    async def guildimage(self, ctx):
        userAvatarUrl = ctx.guild.avatar_url
        await ctx.send(userAvatarUrl)


def setup(bot):
    bot.add_cog(Avatar(bot))