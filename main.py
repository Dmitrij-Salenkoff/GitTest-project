import os

from dotenv import load_dotenv
from tg import TGbot
from tink import Tink

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


if __name__ == "__main__":
    tink = Tink()

    tink.get_candle_history()