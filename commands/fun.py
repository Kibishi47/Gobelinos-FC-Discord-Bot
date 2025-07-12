import discord
from discord.ext import commands
from discord import app_commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(description='Say pong') 
    async def ping(self, interaction: discord.Interaction):
       await interaction.response.send_message("pong")

    @app_commands.command(description='Say hello')
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Bonjour, {interaction.user.mention} !')

async def setup(bot):
    await bot.add_cog(Fun(bot))