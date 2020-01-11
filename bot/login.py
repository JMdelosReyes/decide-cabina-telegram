import logging
from configurations import config
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)


LOGIN, STORE, VOTINGS, VOTING = range(4)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def login(update, context):
    user = update.message.from_user
    logger.info("%s  %s", user.first_name, update.message.text)
    update.message.reply_text("Indique su nombre de usuario y tu contraseña de la siguiente forma. \nUsername \nContraseña",
                              reply_markup=ReplyKeyboardRemove())
    return STORE


def store(update, context):

    user = update.message.from_user
    logger.info("Usuario  %s logged", user.first_name)
    reply_keyboard = [['Vote']]
    update.message.reply_text(update.message.text, reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True))

    return VOTINGS
