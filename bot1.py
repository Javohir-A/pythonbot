import telebot
from bot1 import weather_info
API_TOKEN = '6690741839:AAGL9qyPmjXWWI9teG4It2dwxWunyrZss1o'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!
""")
    
# @bot.message_handler(regexp='Hello')
# def se2nd_message(message):
#     bot.reply_to(message, f'Hello {message.from_user.first_name}')

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print(message)
    if message.from_user.first_name == 'Dilshod':

        bot.send_message(chat_id=1068678414, text= message.text)
        bot.send_message(chat_id=1056424021, text= message.text)
    elif message.from_user.first_name == 'Жавохир':
        
        bot.send_message(chat_id=6306793827, text= message.text)
        bot.send_message(chat_id=1056424021, text= message.text)
    elif message.from_user.first_name == 'Abdulloh':

        bot.send_message(chat_id=6306793827, text= message.text)
        bot.send_message(chat_id=1068678414, text= message.text)
bot.infinity_polling()

