from telegram import Update
from telegram.ext import ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton('🔍 Список доступных функций ', callback_data="list_func")],
        [InlineKeyboardButton('Отправить файл .session', callback_data='session_file')],
        [InlineKeyboardButton('Помощь', callback_data='help')]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выбери действие:", reply_markup=reply_markup)