import discord

import asyncio

from rasa.core.agent import Agent
 
agent = Agent.load("C:/Users/DELL/Desktop/chatbot/ChatBot/models/20241027-200103-plastic-razorbill.tar.gz")
 
intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)
 
@client.event

async def on_ready():

    print(f'Bot connecté en tant que {client.user}')
 
@client.event

async def on_message(message):

    print(f"Message reçu de {message.author}: {message.content}")


    if message.author == client.user:

        return
 
    response = await agent.handle_text(message.content)

    if response:

        print(f"Réponse de Rasa : {response[0].get('text')}")

        await message.channel.send(response[0].get("text"))
 
client.run("your acces token")

 