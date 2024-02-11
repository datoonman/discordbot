import os
import discord
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))  # Set this to the ID of the channel where you want the messages to be sent

intents = discord.Intents.default()
intents.messages = True  # Enable message-related intents

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

async def send_message_to_channel(message):
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(message)

async def read_input():
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, input, "Enter a message to send to the server: ")

# Command-line interface
async def main():
    while True:
        user_input = await read_input()
        if user_input.lower() == 'exit':
            break
        await send_message_to_channel(user_input)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.gather(main(), client.start(TOKEN)))
    finally:
        loop.close()
