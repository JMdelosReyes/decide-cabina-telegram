#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
from configurations import config
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
vots = ['A','B','C','D']
vs = ['1','2','3','4']
LOGIN, STORE, VOTINGS, VOTING = range(4)


def start(update, context):
    reply_keyboard = [['Login']]

    update.message.reply_text(
        'Hi! My name is Bot. Lets to vote',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return LOGIN


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
    update.message.reply_text(update.message.text,reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
    return VOTINGS


def votings(update, context):
    reply_keyboard = vots
    update.message.reply_text(update.message.text,reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return VOTING




def voting(update, context):
    reply_keyboard = vs
    update.message.reply_text(update.message.text,reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return ConversationHandler.END


def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(config.BOT_TOKEN, use_context=True)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            LOGIN: [MessageHandler(Filters.regex('^(Login)$'), login)],

            STORE: [MessageHandler(Filters.text, store)],

            VOTINGS: [MessageHandler(Filters.regex('^(Vote)$'), votings)],

            VOTING: [MessageHandler(Filters.text, voting)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

  
    updater.idle()


if __name__ == '__main__':
    main()