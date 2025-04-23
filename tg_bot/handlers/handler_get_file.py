import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from src.parsing_data import ParseChat
from src.telegram_manager import TelegramManager



async def get_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document

    if not file or not file.file_name.endswith('.session'):
        await update.message.reply_text("Пожалуйста, пришли файл .session")
    else:
        try:
            file_session = await update.message.document.get_file()
            file_path = await file_session.download_to_drive()
            await update.message.reply_text('Файл успешно загружен!')

            abs_path = os.path.abspath(file_path)
            path = os.path.splitext(abs_path)[0]
            context.user_data["session_path"] = path
            session_path = context.user_data.get("session_path")

            manager = TelegramManager(session_path)

            after_getting_file_buttons = InlineKeyboardMarkup([
                [InlineKeyboardButton('Просмотреть список групп/каналов', callback_data="get_channel_groups")]
            ])

            await update.message.reply_text("Файл успешно загружен!", reply_markup=after_getting_file_buttons)


        except Exception as e:
            logging.error(f'Ошибка: {e}')