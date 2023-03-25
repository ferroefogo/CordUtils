import os
from dotenv.main import load_dotenv

load_dotenv()

PREFIX = "/"
BOT_NAME = "DevUtils"
BOT_TOKEN = os.getenv("TOKEN")
GUILD = os.getenv("GUILD_ID")