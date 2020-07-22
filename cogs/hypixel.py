import discord
from discord.ext import commands
import requests
import json

class Hypixel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setusername(self, ctx, *, username = None):
        try:
            request = "https://api.hypixel.net/player?key=ab6c24f1-d5f4-4b88-9a99-c7bfa67d55dd&name=" + username
            r = requests.get(request)
            a = json.loads(r.text)
            ab = str(a["player"]["displayname"])
            with open('data/mcnames.json', 'r') as f:
                webhooks = json.load(f)

            webhooks[str(ctx.author.id)] = username

            with open('data/mcnames.json', 'w') as f:
                json.dump(webhooks, f, indent=4)
            await ctx.send(f"Successfully set your Minecraft username to `{ab}`.")
        except:
            await ctx.send("An error occurred while attempting to perform that command.")

    @commands.command()
    async def getname(self, ctx, user:discord.User="None"):
        try:
            if user == "None":
                user = ctx.author
            with open('data/mcnames.json', 'r') as f:
                mcnames = json.load(f)
            await ctx.send(f"{user.mention}\'s Minecraft name is `{str(mcnames[str(user.id)])}`.")
        except:
            await ctx.send(f"{user.mention} has not added their Minecraft account.\nThey can set this up with `k!setusername Notch`.")


    @commands.command()
    async def bedwars(self, ctx, *, username="none"):
        try:
            if username == "none":
                try:
                    with open('data/mcnames.json', 'r') as f:
                        mcnames = json.load(f)
                    username = mcnames[str(ctx.author.id)]
                    request = "https://api.hypixel.net/player?key=ab6c24f1-d5f4-4b88-9a99-c7bfa67d55dd&name=" + username
                    r = requests.get(request)
                    a = json.loads(r.text)
                    ab = str(a["player"]["displayname"])
                    abc = str(a["player"]["stats"]["Bedwars"]["wins_bedwars"])
                    abc1 = str(a["player"]["stats"]["Bedwars"]["kills_bedwars"])
                    abc2 = str(a["player"]["stats"]["Bedwars"]["losses_bedwars"])
                    abc3 = str(a["player"]["stats"]["Bedwars"]["winstreak"])
                    embed = discord.Embed(title="Hypixel Bedwars Stats", description=f"Stats for {ab}", color=0xff6961)
                    embed.add_field(name="Wins:", value=abc, inline=False)
                    embed.add_field(name="Kills:", value=abc1, inline=False)
                    embed.add_field(name="Losses:", value=abc2, inline=False)
                    embed.add_field(name="Winstreak:", value=abc3, inline=False)
                    await ctx.send(embed=embed)
                except:
                    await ctx.send("Please use `k!setusername Notch` first!")
            else:
                request = "https://api.hypixel.net/player?key=ab6c24f1-d5f4-4b88-9a99-c7bfa67d55dd&name=" + username
                r = requests.get(request)
                a = json.loads(r.text)
                ab = str(a["player"]["displayname"])
                abc = str(a["player"]["stats"]["Bedwars"]["wins_bedwars"])
                abc1 = str(a["player"]["stats"]["Bedwars"]["kills_bedwars"])
                abc2 = str(a["player"]["stats"]["Bedwars"]["losses_bedwars"])
                abc3 = str(a["player"]["stats"]["Bedwars"]["winstreak"])
                embed = discord.Embed(title="Hypixel Bedwars Stats", description=f"Stats for {ab}", color=0xff6961)
                embed.add_field(name="Wins:", value=abc, inline=False)
                embed.add_field(name="Kills:", value=abc1, inline=False)
                embed.add_field(name="Losses:", value=abc2, inline=False)
                embed.add_field(name="Winstreak:", value=abc3, inline=False)
                await ctx.send(embed=embed)
        except:
            await ctx.send("An error occurred while attempting to perform that command.")

    @commands.command()
    async def skywars(self, ctx, *, username="none"):
        try:
            if username == "none":
                try:
                    with open('data/mcnames.json', 'r') as f:
                        mcnames = json.load(f)
                    username = mcnames[str(ctx.author.id)]
                    request = "https://api.hypixel.net/player?key=ab6c24f1-d5f4-4b88-9a99-c7bfa67d55dd&name=" + username
                    r = requests.get(request)
                    a = json.loads(r.text)
                    ab = str(a["player"]["displayname"])
                    abc = str(a["player"]["stats"]["SkyWars"]["wins"])
                    abc1 = str(a["player"]["stats"]["SkyWars"]["kills"])
                    abc2 = str(a["player"]["stats"]["SkyWars"]["losses"])
                    abc3 = str(a["player"]["stats"]["SkyWars"]["win_streak"])
                    embed = discord.Embed(title="Hypixel Skywars Stats", description=f"Stats for {ab}", color=0xafeeee)
                    embed.add_field(name="Wins:", value=abc, inline=False)
                    embed.add_field(name="Kills:", value=abc1, inline=False)
                    embed.add_field(name="Losses:", value=abc2, inline=False)
                    embed.add_field(name="Winstreak:", value=abc3, inline=False)
                    await ctx.send(embed=embed)
                except:
                    await ctx.send("Please use `k!setusername Notch` first!")
            else:
                request = "https://api.hypixel.net/player?key=ab6c24f1-d5f4-4b88-9a99-c7bfa67d55dd&name=" + username
                r = requests.get(request)
                a = json.loads(r.text)
                ab = str(a["player"]["displayname"])
                abc = str(a["player"]["stats"]["SkyWars"]["wins"])
                abc1 = str(a["player"]["stats"]["SkyWars"]["kills"])
                abc2 = str(a["player"]["stats"]["SkyWars"]["losses"])
                abc3 = str(a["player"]["stats"]["SkyWars"]["win_streak"])
                embed = discord.Embed(title="Hypixel Skywars Stats", description=f"Stats for {ab}", color=0xafeeee)
                embed.add_field(name="Wins:", value=abc, inline=False)
                embed.add_field(name="Kills:", value=abc1, inline=False)
                embed.add_field(name="Losses:", value=abc2, inline=False)
                embed.add_field(name="Winstreak:", value=abc3, inline=False)
                await ctx.send(embed=embed)
        except:
            await ctx.send("An error occurred while attempting to perform that command.")

def setup(bot):
    bot.add_cog(Hypixel(bot))