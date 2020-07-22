import asyncio
import datetime
import json
import logging
import sqlite3
from pathlib import Path

import discord
from discord.ext import commands

def get_prefix(client, message):
    try:
        with open('data/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        return prefixes[str(message.guild.id)]
    except:
        return 'k!'




async def run():
    bot = Bot(description="a")
    bot.remove_command("help")

    try:
        await bot.start("TOKEN_GOES_HERE")
    except KeyboardInterrupt:
        await bot.logout()


class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(
            command_prefix="k!",
            description=kwargs.pop('description')
        )
        self.start_time = None
        self.app_info = None

        self.loop.create_task(self.track_start())
        self.loop.create_task(self.load_all_extensions())

    async def status_task(self):
        while True:
            await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="k!help"))
            await asyncio.sleep(60)
            await self.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"with {len(self.users)} people"))
            await asyncio.sleep(60)
            await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.guilds)} guilds"))
            await asyncio.sleep(60)

    async def track_start(self):
        await self.wait_until_ready()
        self.start_time = datetime.datetime.utcnow()


    async def load_all_extensions(self):
        await self.wait_until_ready()
        await asyncio.sleep(1)
        cogs = [x.stem for x in Path('cogs').glob('*.py')]
        for extension in cogs:
            try:
                self.load_extension(f'cogs.{extension}')
                print(f'loaded {extension}')
            except Exception as e:
                error = f'{extension}\n {type(e).__name__} : {e}'
                print(f'failed to load extension {error}')
            print('-' * 10)

    async def on_ready(self):
        print('-' * 10)
        self.app_info = await self.application_info()
        print(f'Logged in as: {self.user.name}\n'
              f'Using discord.py version: {discord.__version__}\n'
              f'Owner: {self.app_info.owner}')
        print('-' * 10)
        self.loop.create_task(self.status_task())

    async def on_guild_join(self, guild):

        embed = discord.Embed(title="Kane",
                              description="Thank you for inviting Kane!\n\nPlease use `?help` for a list of commands")

        await guild.text_channels[0].send(embed=embed)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
