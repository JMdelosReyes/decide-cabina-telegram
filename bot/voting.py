import logging
from configurations import config
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from utilities import (global_vars, parser)

LOGIN, STORE, VOTINGS, VOTING, SAVE_VOTE  = range(5)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def voting(update, context):
    global_vars.voting_selected = update.message.text.split("-")[0]
    voting = parser.parseVoting()
    reply_keyboard = parser.createKeyOption(voting['question']['options'])

    update.message.reply_text(update.message.text, reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True))
    logger.info("Listing voting options")
    
    return SAVE_VOTE
