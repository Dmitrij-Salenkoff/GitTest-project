import os
import requests


class TGbot:

    def __init__(self):
        self.token = self._get_token()
        self.chat_id = self._get_chat_id()
        self.api_url = f'https://api.telegram.org/bot{self.token}/'

    def _get_token(self):
        return os.getenv('TOKEN')

    def _get_chat_id(self):
        return os.getenv('CHAT_ID')

    def send_message(self, text: str):
        method_name = 'sendMessage'
        res = requests.get(self.api_url + method_name,
                           params={
                               'chat_id': self.chat_id,
                               'text': text
                           })
        return res.status_code
