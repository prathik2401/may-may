import discord
from dotenv import load_dotenv
import os
import requests
import json
load_dotenv()

def get_meme():
        response = requests.get('https://meme-api.com/gimme')
        json_data = json.loads(response.text)
        return json_data['url']

class Myclient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$maymay'):
            await message.channel.send(get_meme())
            
        
intents = discord.Intents.default()
intents.typing = False
intents.message_content = True

client = Myclient(intents=intents)
client.run(os.getenv('DISCORD_TOKEN'))