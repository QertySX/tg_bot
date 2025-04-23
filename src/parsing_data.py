import logging
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import PeerChannel, ChannelParticipantsSearch
from src.telegram_manager import TelegramManager

'''

1. get_chat_id - запрашивает список чатов пользователя и возвращает - название -> ID -> тип обьекта (чат, канал (новые чаты отмечены как канал))
2. parse_chat_users - Принимает в параметр ID нужного чата и парсит link участников группы/супергруппы

'''

logging.basicConfig(level=logging.DEBUG)

class ParseChat(TelegramManager):
    def __init__(self, session_path: str):
        super().__init__(session_path)

    async def get_chat_id(self):
        try:
            await self.manager.start()
            logging.info("Авторизация прошла успешно!")

            dialogs = await self.manager.get_dialogs()
            logging.info('[INFO] Получаем список чатов и каналов!')
            for dialog in dialogs:
                try:
                    entity = dialog.entity

                    if hasattr(entity, 'title'):
                        print(f'{entity.title} | ID: -> {entity.id} | Type: -> {type(entity)}')

                except Exception as e:
                    logging.error('[INFO] Ошибка', e)
        except Exception as e:
            logging.error('[INFO] Ошибка', e)


    async def parse_chat_users(self, id_channel):
        try:
            await self.manager.start()
            logging.info('Авторизация прошла успешно!')
            channel = await self.manager.get_entity(PeerChannel(id_channel))

            offset = 0
            limit = 10000
            all_participants = []

            while True:
                try:
                    participants = await self.manager(GetParticipantsRequest(
                        channel=channel,
                        filter=ChannelParticipantsSearch(''),
                        offset=offset,
                        limit=limit,
                        hash=0
                    ))

                    if not participants.users:
                        logging.info('Не удалось найти пользователей')
                        break

                    all_participants.extend(participants.users)
                    offset += len(participants.users)
                except Exception as e:
                    logging.error(f'Ошибка в цикле while: {e}')

            for user in all_participants:
                print(user.username)
            print(len(all_participants))

        except Exception as e:
            logging.error(f'Ошибка: {e}')

