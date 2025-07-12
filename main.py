import discord
from discord.ext import commands
import config
import os

# Création du bot avec intents explicites
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

# Événement de démarrage
@bot.event
async def on_ready():
    print(f"{bot.user} est connecté !")

@bot.event
async def on_message(message):
    print(message.content)

    # Traitement des commandes activé
    await bot.process_commands(message)


@bot.command()  # Appel avec !salut
async def test(ctx):
    print("Commande okayyy")
    await ctx.send(f"Salut {ctx.author.display_name} 👋")

# Lancement du bot
bot.run(config.TOKEN)
