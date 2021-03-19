import telebot

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

# Программа для погоды
config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('dc7d9d9941fb9f31355bd9cf64e05a32', config_dict)
mgr = owm.weather_manager()

# Программа для бота
bot = telebot.TeleBot(
    "1762691970:AAHXg3fLZNGLw-vfx1cK_d6GRwCI4USwYO8", parse_mode=None)


@bot.message_handler(content_types=['text', 'help'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    weather = w.detailed_status
    temperature = w.temperature('celsius')['temp']
    wind = w.wind()['speed']

    answer = 'В городе ' + message.text + ' сейчас ' + str(temperature) + \
        ' градусов и ' + weather + \
        ', а также скорость ветра ' + str(wind) + ' м/с.'

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
