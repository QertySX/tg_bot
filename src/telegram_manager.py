
from telethon.sync import TelegramClient
from src.config.config import api_id, api_hash


class TelegramManager:
    def __init__(self, session_path):
        if session_path:
            self.session_path = session_path
            self.manager = TelegramClient(session_path, api_id, api_hash)



