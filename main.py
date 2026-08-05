import os
import discord
from dotenv import load_dotenv
from config import CHANNEL_ID

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    channel = client.get_channel(CHANNEL_ID)

    if channel:
        await channel.send("🚀 WarEra Bot Started Successfully")


client.run(TOKEN)

