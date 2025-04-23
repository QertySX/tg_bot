from telegram.ext import CommandHandler, Application, MessageHandler, filters
from tg_bot.commands.start import start
from tg_bot.commands.help import help as help_command
from telegram.ext import CallbackQueryHandler
from tg_bot.handlers.button_start_handler import inline_button_handler
from tg_bot.handlers.handler_get_file import get_file

'''
1. register_command_handlers() - РЕГИСТРАЦИЯ ХЭНДЛЕРА И КНОПКИ 
'''

def register_handlers(app: Application):

    #РЕГИСТРАЦИЯ /start
    app.add_handler(CommandHandler("start", start))
    #РЕГИСТРАЦИЯ КНОПОК
    app.add_handler(CallbackQueryHandler(inline_button_handler))

    # РЕГИСТРАЦИЯ ХЭНДЛЕРА ПО ПРИНЯТИЮ ФАЙЛА
    app.add_handler(MessageHandler(filters.Document.ALL, get_file))

    # РЕГИСТРАЦИЯ /help
    app.add_handler(CommandHandler("help", help_command))






