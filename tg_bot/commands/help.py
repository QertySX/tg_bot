from telegram import Update
from telegram.ext import ContextTypes



async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='''
/get_chat_id - выдает ID всех групп/каналов на которые вы подписаны
/parse_username - парсит группу по указанному ID 
/spam_username - спам по указанным username
/invite_group - добавляет пользователей в указанную группу/канал
/spam_contacts - спамит пользователей по контактам
    ''')