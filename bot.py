import logging

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import config
from commands.find import search_query
from commands.buttonhandler import button

def start(bot, update):
    chat_id = update.message.chat.id
    keyboard = [[
        InlineKeyboardButton('Support Chat',
                             url=config.supportChatUrl)
    ],
        [
            InlineKeyboardButton('Android App Link',
                                 url=config.appUrl)
        ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.sendMessage(chat_id, "<b>Hi, I Can Search Torrent Database For Your Query.</b>\n\n"
                             "Supports Inline Mode \n-/help For More Info\n",
                    parse_mode='HTML',
                    reply_markup=reply_markup)

def help(bot, update):
    chat_id = update.message.chat.id
    keyboard = [[
        InlineKeyboardButton('Support Chat',
                             url=config.supportChatUrl)
    ],
        [
            InlineKeyboardButton('Android App Link',
                                 url=config.appUrl)
        ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.sendMessage(chat_id, "<b>Available commands are: </b>\n" +
                    "-/find - <code>Searches Torrent Database</code>\n"
                    "Ask/Report In Support Group If You Have Any Problem With This Bot. Kthnxbye",
                    parse_mode='HTML',
                    reply_markup=reply_markup)

def main():
    updater = Updater(config.botToken)
    dp = updater.dispatcher

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    logger = logging.getLogger(__name__)

    dp.add_handler(CommandHandler('find', search_query, pass_args=True))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CallbackQueryHandler(button))
    
    updater.start_polling()
    logger.info('Listening humans as %s..' % updater.bot.username)
    updater.idle()
    logger.info('Bot stopped gracefully')


def error(update, context):
    """Log Errors caused by Updates."""
    logger = logging.getLogger(__name__)
    logger.warning('Update "%s" caused error "%s"', update, context.error)


if __name__ == '__main__':
    main()
