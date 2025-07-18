import discord
from discord.ext import commands
import discordBot.config as config
import os
import pathlib

class FootBot(commands.Bot):
    
    def __init__(self, command_prefix, intents, app_id):
        super().__init__(command_prefix=command_prefix, intents=intents, id=app_id)
        self.remove_command("help")  # Optional: override with custom help
        self.COGS_DIR = pathlib.Path(__file__).parent / "cogs"

    async def setup_hook(self):
        print("Loading cogs ...")
        for filename in os.listdir(self.COGS_DIR):
            if filename.endswith('.py') and filename != '__init__.py':
                print(f"Try import {filename}")
                try:
                    await self.load_extension(f'/{filename[:-3]}')
                    print(f'Cog loaded: {filename[:-3]}')
                except Exception as e:
                    print(f'Error loading cog {filename[:-3]}: {e}')
        await self.tree.sync()

    async def on_ready(self):
        print(f"{self.user} est connecté !")

    async def on_message(self, message):
        if message.author == self.user:
            return
        print(message.content)
        await self.process_commands(message)