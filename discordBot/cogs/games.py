import discord
from discord.ext import commands
from discord import app_commands

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(description='List all games')
    @app_commands.describe(
        search="Nom d'une partie à trouvé",
        is_finished="Afficher uniquement les parties terminés"
    )
    async def games(self, interaction: discord.Interaction, search:str = "", is_finished:bool = False):
        
        # Construct the API request
        params = {"search":search, "isFinished": "1" if is_finished == True else "0"}
        apiResponse = await self.bot.apiService.get(endpoint="games")

        # Check if the response is valid and create the embed
        embed = discord.Embed(
            title="🎲 Liste des parties",
            description="Voici les parties déja jouées ou en cours.",
            color=discord.Color.blue()
        )

        for game in apiResponse['data']:
            status = "✅ Terminée" if game["isFinished"] == True else "🕹️ En cours"
            played_at = game.get("playedAt", "N/A")

            embed.add_field(
                name=f"{game['name']} ({status})",
                value=(
                    f"**Terrain :** {game['fieldName']}\n"
                    f"**Durée :** {game['playTime']} min\n"
                    f"**Date :** {played_at}"
                ),
                inline=False
            )
        
        # response to the interaction
        if not apiResponse['data']:
            embed.description = "Aucune partie trouvée."
            embed.color = discord.Color.red()
        await interaction.response.send_message(embed=embed)

    @app_commands.command(description='Create a new game session that players can later join.')
    async def new_game(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Bonjour, {interaction.user.mention} !')

async def setup(bot):
    await bot.add_cog(Games(bot))