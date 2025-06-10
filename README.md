# Gobelinos-FC-Discord-Bot

## Description
Gobelinos FC Discord Bot est un bot Discord conçu pour gérer des matchs de football à 5 entre amis. Il permet de créer des équipes équilibrées, suivre les statistiques des joueurs, et maintenir un système d'ELO pour évaluer le niveau de chacun.

⚠️ Remarque importante : Le bot ne gère aucune logique métier ni de base de données. Il sert uniquement d’interface entre Discord et une API externe, qui contient la logique de gestion des matchs, joueurs et statistiques.

## Fonctionnalités
- Création et gestion de joueurs avec système d'ELO
- Organisation de matchs avec équipes équilibrées
- Suivi des statistiques individuelles et d'équipe
- Classement des joueurs

## Installation

### Prérequis
- Python 3.8+
- pip
- Un compte développeur Discord avec un bot enregistré

### Configuration
1. Clonez ce dépôt:
```bash
git clone https://github.com/Kibishi47/Gobelinos-FC-Discord-Bot.git
cd Gobelinos-FC-Discord-Bot
```

2. Installez les dépendances:
```bash
pip install -r requirements.txt
```

3. Créez un fichier `.env` à la racine du projet avec:
```
API_URL=https://votre-api-url/
DISCORD_TOKEN=votre_token_discord
```

4. Lancez le bot:
```bash
python bot.py
```

## Commandes

### Commandes essentielles

### Commandes secondaires

## Structure du projet
```
Gobelinos-FC-Discord-Bot/
├── bot.py                 # Point d'entrée principal
├── requirements.txt       # Dépendances
└── .env                   # Variables d'environnement
```

## Contribution
Les contributions sont les bienvenues! N'hésitez pas à ouvrir une issue ou une pull request.

## Licence
MIT
