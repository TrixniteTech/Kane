import aiohttp
import discord
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
import json
from discord.ext.commands import has_permissions, MissingPermissions
import datetime


class Announcements(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setchannel(self, ctx, *, channel: discord.TextChannel = None):
        try:
            webhook = await channel.create_webhook(name='Kane Announcements')

            with open('data/webhooks.json', 'r') as f:
                webhooks = json.load(f)

            webhooks[str(ctx.guild.id)] = webhook.url

            with open('data/webhooks.json', 'w') as f:
                json.dump(webhooks, f, indent=4)
            await ctx.send(f"Successfully set the announcements channel to `#{channel.name}`.")
        except:
            await ctx.send("An error occurred while attempting to perform that command.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def alert(self, ctx, *, message):
        try:
            current_time = datetime.datetime.now()
            a = message.split("|")
            title = a[0]
            desc = a[1]
            embed = discord.Embed(title=title, description=desc, color=0xfd0000)
            embed.set_footer(text="Sent by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
            with open('data/webhooks.json', 'r') as f:
                webhooks = json.load(f)

            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(webhooks[str(ctx.guild.id)], adapter=AsyncWebhookAdapter(session))
                await webhook.send(embed=embed, username='Alert', avatar_url="https://cdn.discordapp.com/attachments/734839165363159160/734860617768370247/warning-icon.png")

        except:
            await ctx.send("Please make sure you have completed the following and also have permission:\n`k!setchannel #channel`\n`k!alert Title goes here|Description goes here`")

    @commands.command(aliases=['announce'])
    @commands.has_permissions(manage_messages=True)
    async def announcement(self, ctx, *, message):
        try:
            current_time = datetime.datetime.now()
            a = message.split("|")
            title = a[0]
            desc = a[1]
            embed = discord.Embed(title=title, description=desc, color=0x35c8c8)
            embed.set_footer(text="Sent by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
            with open('data/webhooks.json', 'r') as f:
                webhooks = json.load(f)

            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(webhooks[str(ctx.guild.id)], adapter=AsyncWebhookAdapter(session))
                await webhook.send(embed=embed, username='Announcement', avatar_url="https://cdn.discordapp.com/attachments/734839165363159160/734863471942041731/announcement-icon.png")

        except:
            await ctx.send("Please make sure you have completed the following and also have permission:\n`k!setchannel #channel`\n`k!announcement Title goes here|Description goes here`")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def update(self, ctx, *, message):
        try:
            current_time = datetime.datetime.now()
            a = message.split("|")
            title = a[0]
            desc = a[1]
            embed = discord.Embed(title=title, description=desc, color=0xc1bf6c)
            embed.set_footer(text="Sent by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
            with open('data/webhooks.json', 'r') as f:
                webhooks = json.load(f)

            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(webhooks[str(ctx.guild.id)], adapter=AsyncWebhookAdapter(session))
                await webhook.send(embed=embed, username='Update', avatar_url="https://icons.iconarchive.com/icons/graphicloads/100-flat/128/pencil-icon.png")

        except:
            await ctx.send("Please make sure you have completed the following and also have permission:\n`k!setchannel #channel`\n`k!update Title goes here|Description goes here`")

    @commands.command(aliases=['warn'])
    @commands.has_permissions(manage_messages=True)
    async def warning(self, ctx, *, message):
        try:
            current_time = datetime.datetime.now()
            a = message.split("|")
            title = a[0]
            desc = a[1]
            embed = discord.Embed(title=title, description=desc, color=0xe39b4a)
            embed.set_footer(text="Sent by " + ctx.author.name + " • " + str(current_time.day) + "/" + str(current_time.month) + "/" + str(current_time.year), icon_url=ctx.author.avatar_url)
            with open('data/webhooks.json', 'r') as f:
                webhooks = json.load(f)

            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(webhooks[str(ctx.guild.id)], adapter=AsyncWebhookAdapter(session))
                await webhook.send(embed=embed, username='Warning', avatar_url="https://icons.iconarchive.com/icons/graphicloads/100-flat/128/warning-icon.png")

        except:
            await ctx.send("Please make sure you have completed the following and also have permission:\n`k!setchannel #channel`\n`k!warning Title goes here|Description goes here`")

def setup(bot):
    bot.add_cog(Announcements(bot))