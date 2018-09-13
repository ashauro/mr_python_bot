from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import datetime

# Logging configuration
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    user_first_name = update.message.chat.first_name
    text = 'Привет, {}! С помощью бота ты можешь вызывать ' \
           'команды /start, /howareyou и /planet (Марс, Венера, Сатурн), а также получать ответы ' \
           'на свои сообщения'.format(user_first_name)
    logging.info('Вызван /start')
    update.message.reply_text(text)

def mood(bot, update):
    text = 'ЗБС!'
    logging.info(text)
    update.message.reply_text(text)

def planet(bot, update):
    splitted_string = update.message.text.split(' ')
    try:
        planet_name = str(splitted_string[1]).lower()

        logging.info ('Пользователь ввел: {}'.format(planet_name))

        today_date = datetime.datetime.today()
        us_date = today_date.strftime('%Y/%m/%d')

        if planet_name == 'марс':
            mars_today = ephem.Mars (us_date)
            update.message.reply_text ('Марс:  {}'.format(ephem.constellation(mars_today)))
        elif planet_name == 'венера':
            venus_today = ephem.Venus (us_date)
            update.message.reply_text ('Венера:  {}'.format(ephem.constellation(venus_today)))
        elif planet_name == 'сатурн':
            saturn_today = ephem.Saturn (us_date)
            update.message.reply_text ('Сатурн:  {}'.format(ephem.constellation(saturn_today)))
        else:
            update.message.reply_text('У меня нет данных :(')
    except IndexError:
        update.message.reply_text('Пожалуйста, введите название планеты! Например /planet Марс')
        logging.info ('Пользователь не указал планету')

def talk_to_me (bot, update):
    user_first_name = update.message.chat.first_name
    user_text = update.message.text
    user_reply = "Привет {}! Ты написал: {}".format(user_first_name, user_text)
    logging.info('Пользователь ' + user_first_name + ' написал в чат: ' + user_text)
    update.message.reply_text(user_reply)

def main ():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))
    dp.add_handler(CommandHandler("howareyou", mood))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text,talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
