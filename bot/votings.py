import logging
from configurations import config
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from bot import (llamadas,globaltoken)
import json



LOGIN, STORE, VOTINGS, VOTING = range(4)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def votings(update, context):
    print('token ' + globaltoken.token)
    response = llamadas.get_user(globaltoken.token)
    usuario = json.loads(response.text)

    response2 = llamadas.get_votings(usuario["id"])

    vots = json.loads(response2.text)
    print(vots)
    reply_keyboard = ['a']
    update.message.reply_text(update.message.text, reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True))

    return VOTING
