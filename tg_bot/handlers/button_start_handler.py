from telegram import Update
from telegram.ext import ContextTypes
import logging

from src.parsing_data import ParseChat

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

'''
В ДАННОМ ФАЙЛЕ ПРОИСХОДИТ ОБРАБОТКА КНОПОК ПО КОМАНДЕ /start
'''


async def inline_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # обязательно! чтобы Telegram не крутил "загрузка..."

    if query.data == "list_func":
        await query.edit_message_text("Что будем искать? 🔍")
    if query.data == 'session_file':
        await query.edit_message_text("Отправь .session файл документом 📄")
    if query.data == 'help':
        await query.edit_message_text('''
        ИНСТРУКЦИЯ: 
Что бы начать работу вставьте файл .session и выберите вид рассылки который вам нужен.
        ''')

    if query.data == 'get_channel_groups':
        # Получаем session_path из user_data
        user_id = update.effective_user.id
        session_path = context.user_data.get(user_id)

        # Если session_path существует, создаем объект и вызываем функцию
        try:
            parse_chat = ParseChat(session_path)
            await parse_chat.get_chat_id()
        except Exception as e:
            logging.error(f"Ошибка при получении данных чатов: {e}")
            await query.edit_message_text("Произошла ошибка при обработке запроса.")



