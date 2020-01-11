import logging
from configurations import config
from utilities import parser
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from bot import (llamadas)
from utilities import (global_vars)
import json

LOGIN, STORE, VOTINGS, VOTING, SAVE_VOTE  = range(5)

#TODO: Necesitamos almacenar ID del usuario, Id de votación, opción elegida y pub_key
def save_vote(update,context):  
    update.message.reply_text(
        'La votación ha sido realizada con éxito.', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END