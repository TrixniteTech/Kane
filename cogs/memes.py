import discord
from discord.ext import commands
import datetime
import requests
import json
import random

class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        try:
            while True:
                request = "https://meme-api.herokuapp.com/gimme"
                r = requests.get(request)
                a = r.json()
                if a["nsfw"] == False:
                    title = a["title"] + " from r/" + a["subreddit"]
                    embed = discord.Embed(title=title)
                    embed.set_image(url=a["url"])
                    current_time = datetime.datetime.now()
                    embed.set_footer(text="Requested by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
                        current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    break
                else:
                    pass
        except Exception as e:
            await ctx.send(f"An error occurred while attempting to perform that command.\nInfo: `{e}`")

    @commands.command()
    async def tech(self, ctx):
        try:
            while True:
                request = "https://meme-api.herokuapp.com/gimme/ProgrammerHumor"
                r = requests.get(request)
                a = r.json()
                if a["nsfw"] == False:
                    title = a["title"] 
                    embed = discord.Embed(title=title)
                    embed.set_image(url=a["url"])
                    current_time = datetime.datetime.now()
                    embed.set_footer(text="Requested by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
                        current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    break
                else:
                    pass
        except Exception as e:
            await ctx.send(f"An error occurred while attempting to perform that command.\nInfo: `{e}`")

    @commands.command()
    async def homelab(self, ctx):
        try:
            while True:
                request = "https://meme-api.herokuapp.com/gimme/homelab"
                r = requests.get(request)
                a = r.json()
                if a["nsfw"] == False:
                    title = a["title"]
                    embed = discord.Embed(title=title)
                    embed.set_image(url=a["url"])
                    current_time = datetime.datetime.now()
                    embed.set_footer(text="Requested by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
                        current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    break
                else:
                    pass
        except Exception as e:
            await ctx.send(f"An error occurred while attempting to perform that command.\nInfo: `{e}`")

    @commands.command(aliases=['midly', 'm'])
    async def mildlyinfuriating(self, ctx):
        try:
            while True:
                request = "https://meme-api.herokuapp.com/gimme/mildlyinfuriating"
                r = requests.get(request)
                a = r.json()
                if a["nsfw"] == False:
                    title = a["title"]
                    embed = discord.Embed(title=title)
                    embed.set_image(url=a["url"])
                    current_time = datetime.datetime.now()
                    embed.set_footer(text="Requested by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(
                        current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    break
                else:
                    pass
        except Exception as e:
            await ctx.send(f"An error occurred while attempting to perform that command.\nInfo: `{e}`")


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("r/"):
            msg = message.split("/")
            subreddit = msg[1]
            try:
                while True:
                    request = "https://meme-api.herokuapp.com/gimme/" + subreddit
                    r = requests.get(request)
                    a = r.json()
                    if a["nsfw"] == False:
                        title = a["title"]
                        embed = discord.Embed(title=title)
                        embed.set_image(url=a["url"])
                        current_time = datetime.datetime.now()
                        embed.set_footer(text="Requested by " + message.author.name + " • " + str(current_time.day) + "/" + str(
                            current_time.month) + "/" + str(current_time.year), icon_url=message.author.avatar_url)
                        await message.channel.send(embed=embed)
                        break
                else:
                    pass
            except Exception as e:
                await message.channel.send(f"An error occurred while attempting to perform that command.\nInfo: `{e}`")
        await self.bot.process_commands(message)
def setup(bot):
    bot.add_cog(Memes(bot))