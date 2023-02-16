import os

from dotenv import load_dotenv
from tg import TGbot

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

bot = TGbot()
bot.send_message('Тест')