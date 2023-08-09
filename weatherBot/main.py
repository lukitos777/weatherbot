import telebot
import requests
import json

bot = telebot.TeleBot('6677774549:AAFA_CC8I5AdAKZX_bgA4RJoAdlhRSF1qDs')
API = 'b2aa55c66cd946199804b0f15e298eb6'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi enter city name')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()

    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric'
    )

    if res.status_code == 200:
        data = json.loads(res.text)

        temp = data['main']['temp']
        emoji = '🌞' if temp > 5.0 else '🥶'

        bot.reply_to(message, f"temp: {temp} | {emoji}")
    else:
        bot.reply_to(message, 'Invalid name ⚠️')


bot.polling(none_stop=True)
