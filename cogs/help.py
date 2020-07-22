import discord
from discord.ext import commands
import datetime

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *, category="none"):
        current_time = datetime.datetime.now()
        if category == "none":
            embed = discord.Embed(title="Page 1:", description="k!help {page}")
            embed.add_field(name="k!avatar @harrydev#9999", value="Displays the avatar of the user.", inline=False)
            embed.add_field(name="k!setchannel #announcements", value="Sets the announcements channel.", inline=False)
            embed.add_field(name="k!stats", value="Shows Kane\'s stats.", inline=False)
            embed.set_footer(text="Requested by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
                current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif category.lower() == "2":
            embed = discord.Embed(title="Page 2:", description="k!help {page}")
            embed.add_field(name="k!alert Title goes here|Description goes here", value="Sends an alert to the announcements channel.", inline=False)
            embed.add_field(name="k!warning Title goes here|Description goes here", value="Sends a warning to the announcements channel.", inline=False)
            embed.add_field(name="k!announce Title goes here|Description goes here", value="Sends an announcement to the announcements channel.", inline=False)
            embed.add_field(name="k!update Title goes here|Description goes here",
                            value="Sends an update to the announcements channel.", inline=False)
            embed.set_footer(text="Requested by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
                current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif category.lower() == "3":
            embed = discord.Embed(title="Page 3:", description="k!help {page}")
            embed.add_field(name="k!setusername Notch", value="Sets your minecraft username.", inline=False)
            embed.add_field(name="k!bedwars", value="Shows you your bedwars stats.", inline=False)
            embed.add_field(name="k!skywars", value="Shows you your skywars stats.", inline=False)
            embed.add_field(name="k!getname @harrydev#9999", value="Gets their minecraft username.", inline=False)
            embed.set_footer(text="Requested by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
                current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif category.lower() == "4":
            embed = discord.Embed(title="Page 4:", description="k!help {page}")
            embed.add_field(name="k!meme", value="Gives you a random meme from reddit.", inline=False)
            embed.set_footer(text="Requested by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
                current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))