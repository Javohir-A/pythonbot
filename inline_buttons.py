import telebot
import requests
from telebot import types
API_TOKEN = '6690741839:AAGL9qyPmjXWWI9teG4It2dwxWunyrZss1o'
bot = telebot.TeleBot(API_TOKEN)
def weather_info():
    url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
    respons = requests.get(url)
    forecast_info = respons.json()
    return forecast_info
@bot.message_handler(func= lambda message : True)
def send_info(message):
    bot.send_message(message.chat.id, weather_info()['hourly']['time'][0])
bot.infinity_polling()

