import logging
from configurations import config
from utilities import parser,global_vars,crypto
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from bot import (llamadas)
from utilities import (global_vars)
import json

LOGIN, STORE, VOTINGS, VOTING, SAVE_VOTE  = range(5)

def save_vote(update,context):
    selected_option_id=update.message.text.split('-')[0]
    pub_key_encrypt=crypto.PublicKey(int(global_vars.pub_key.get('p')),int(global_vars.pub_key.get('g')),int(global_vars.pub_key.get('y')))
    vote_encrypt=crypto.encrypt(pub_key_encrypt,selected_option_id)

    user_by_token=llamadas.get_user(global_vars.token)
    usuario = json.loads(user_by_token.text)
    user_id=usuario['id']

    vote_encrypt=vote_encrypt.split()

    data_dict={'vote':{'a':vote_encrypt[0],'b': vote_encrypt[1]},
    'voting' :global_vars.voting_selected,
    'voter':user_id,
    'token': global_vars.token
    }

    llamadas.save_vote_data(data_dict)

    update.message.reply_text('La votación ha sido realizada con éxito.', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END