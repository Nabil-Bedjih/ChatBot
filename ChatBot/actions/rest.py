import discord

import asyncio

from rasa.core.agent import Agent
 
# Charger le modèle Rasa

agent = Agent.load("C:/Users/DELL/Desktop/chatbot/ChatBot/models/20241027-200103-plastic-razorbill.tar.gz")
 
# Initialisation du client Discord avec les intents pour lire les messages

intents = discord.Intents.default()

intents.message_content = True  # Activer la lecture des messages pour que le bot puisse les traiter

client = discord.Client(intents=intents)
 
@client.event

async def on_ready():

    print(f'Bot connecté en tant que {client.user}')
 
@client.event

async def on_message(message):

    # Affiche le message reçu dans la console pour confirmer la réception

    print(f"Message reçu de {message.author}: {message.content}")

    # Éviter de traiter les messages envoyés par le bot lui-même

    if message.author == client.user:

        return
 
    # Envoi du message utilisateur à Rasa pour obtenir une réponse

    response = await agent.handle_text(message.content)

    # Si une réponse est reçue de Rasa, elle est renvoyée sur Discord

    if response:

        print(f"Réponse de Rasa : {response[0].get('text')}")

        await message.channel.send(response[0].get("text"))
 
# Démarrer le bot avec le token

client.run("MTMwMDE0OTY1MjMzNDU3NTc0OA.Gd-lYg.UkOuFET6WhLU6FTEhK_9tnh8iQGGq8DT8vi5nY")

 