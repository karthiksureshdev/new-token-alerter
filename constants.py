import os
from dotenv import load_dotenv

load_dotenv()

DEX_SCREENER_URL: str = "https://dexscreener.com"
NEW_PAIRS: str = "/new-pairs"
TELEGRAM_BOT_TOKEN: str = os.getenv('TELEGRAM_BOT_TOKEN')
