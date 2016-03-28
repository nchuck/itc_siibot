# coding=utf-8
from telegram import InlineQueryResultArticle
from telegram.ext import Updater
import os


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text="Bot para el SII (No Oficial) del ITC")


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(os.environ['TELEGRAM_BOT_API_KEY'])

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addTelegramCommandHandler("start", start)

    # on noncommand i.e message - echo the message on Telegram
    #dp.addTelegramInlineHandler(inlinequery)
    #dp.addTelegramMessageHandler(handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
