from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

# Logging configuration
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    user_first_name = update.message.chat.first_name
    text = "Привет, " + user_first_name + "! С помощью бота ты можешь вызывать команды /start и /howareyou, а также получать ответы на свои сообщения"
    logging.info('Вызван /start')
    update.message.reply_text(text)

def today(bot, update):
    text = 'ЗБС!'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me (bot, update):
    user_first_name = update.message.chat.first_name
    user_text = update.message.text
    user_reply = "Привет {}! Ты написал: {}".format(user_first_name, update.message.text)
    logging.info('Пользователь ' + user_first_name + ' написал в чат: ' + user_text)
    update.message.reply_text(user_reply)

def main ():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))
    dp.add_handler(CommandHandler("howareyou", today))
    dp.add_handler(MessageHandler(Filters.text,talk_to_me))

    mybot.start_polling()
    mybot.idle()



main()
