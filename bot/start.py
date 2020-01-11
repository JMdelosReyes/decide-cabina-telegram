import logging
from configurations import config
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)


LOGIN, STORE, VOTINGS, VOTING = range(4)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    reply_keyboard = [['Login']]
    update.message.reply_text(
        'Hi! My name is Decide-Moltres-Bot. Lets vote',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return LOGIN
