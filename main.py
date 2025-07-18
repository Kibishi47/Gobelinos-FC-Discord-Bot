import discord
from discord.ext import commands
import discordBot.config as config
import os
from discordBot.bot import FootBot

# Création du bot avec intents explicites
intents = discord.Intents.default()
intents.message_content = True

bot = FootBot(command_prefix=config.PREFIX, intents=intents, app_id=config.APPLICATION_ID)
bot.run(config.TOKEN)