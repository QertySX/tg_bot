import logging
from telegram.ext import ApplicationBuilder
from tg_bot.config.bot_config import token
from tg_bot.handlers.register_command_handlers import register_handlers

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)



if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    register_handlers(application)

    application.run_polling()