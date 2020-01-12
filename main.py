import logging
from configurations import config
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from bot import (login, start, voting, votings,error,cancel,llamadas,save_vote,cancel)
from utilities import global_vars
import os



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

LOGIN, STORE, VOTINGS, VOTING, SAVE_VOTE  = range(5)


def main():
    updater = Updater(config.BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start.start)],

        states={
            LOGIN: [MessageHandler(Filters.regex('^(Login)$'), login.login)],

            STORE: [MessageHandler(Filters.text, login.store)],

            VOTINGS: [MessageHandler(Filters.regex('^(Vote)$'), votings.votings)],

            VOTING: [MessageHandler(Filters.text, voting.voting)],

            SAVE_VOTE: [MessageHandler(Filters.text,save_vote.save_vote)]
        },

        fallbacks=[CommandHandler('cancel', cancel.cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error.error)

    if(config.WEBHOOK):
        logger.info("WEBHOOK ACTIVADO")
        PORT = int(os.environ.get("PORT", config.PORT))
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=config.BOT_TOKEN)
        updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(config.HEROKU_APP_NAME, config.BOT_TOKEN))
    else:
        updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
