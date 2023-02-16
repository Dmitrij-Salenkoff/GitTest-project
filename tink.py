import os
from datetime import timedelta

from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.utils import now


class Tink:
    def __init__(self):
        self.token: str = self._get_token()

    def _get_token(self) -> str:
        return os.getenv('INVEST_TOKEN')

    def get_candle_history(self):
        with Client(self.token) as client:
            for candle in client.get_all_candles(
                    figi="BBG004730N88",
                    from_=now() - timedelta(days=5),
                    interval=CandleInterval.CANDLE_INTERVAL_HOUR,
            ):
                print(candle)

        return 0
