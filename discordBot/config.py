from dotenv import load_dotenv
import os

# Charge les variables d’environnement du fichier .env
load_dotenv()

# Lit la variable DISCORD_TOKEN définie dans .env
TOKEN = os.getenv("DISCORD_TOKEN")
APPLICATION_ID = os.getenv("APPLICATION_ID")
PREFIX = "/"            
