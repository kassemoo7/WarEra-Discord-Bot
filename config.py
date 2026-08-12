import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

print("TOKEN VALUE:", TOKEN)

CHANNEL_ID = 1534597948766294189