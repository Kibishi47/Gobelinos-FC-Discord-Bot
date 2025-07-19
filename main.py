import discord
from discord.ext import commands
import config as config
import os
from discordBot.bot import FootBot
from GobelinosAPI.ApiService import GobelinosAPI


# Initialisation de l'API Gobelinos
if not config.Gobelinos_API_URL:
    raise ValueError("Gobelinos API URL is not set in the config.")
api = GobelinosAPI(config.Gobelinos_API_URL)
import asyncio
async def initAPI():
    response = await api.login()
    print("API initialized:", response)
asyncio.run(initAPI())


# Création du bot avec intents explicites
intents = discord.Intents.default()
intents.message_content = True

bot = FootBot(command_prefix=config.PREFIX, intents=intents, app_id=config.APPLICATION_ID, apiService=api)
bot.run(config.TOKEN)