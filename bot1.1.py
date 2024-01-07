import random
from telebot import types, TeleBot
from weather import weather_info
user_questions = [
    {'question': "What is the capital of France", 'answer': "Paris"},
    {'question': "What is the best car in the world", 'answer': "BMW"},
    {'question': "Do you like yourself", 'answer': "yes"}
]

API_TOKEN = '6690741839:AAGL9qyPmjXWWI9teG4It2dwxWunyrZss1o'
bot = TeleBot(API_TOKEN)

answer = ""  # Declare answer outside the function

@bot.message_handler(commands=['start'])
def start(message):
    # Create a keyboard with two buttons
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Button 1")
    button2 = types.KeyboardButton("Button 2")
    
    # Add buttons to the keyboard
    keyboard.add(button1, button2)
    
    # Send a message with the keyboard
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    global answer 
    
    # Handle other messages
    if message.text == 'Button 1':
        # Ask a random question
        random_question = random.choice(user_questions)
        answer = random_question["answer"]

        bot.send_message(message.chat.id, random_question["question"])
    elif message.text == "Button 2":
        print(weather_info())
    elif message.text.lower() == answer.lower():
        # User's answer is correct

        bot.send_message(message.chat.id, "You're correct!")
    else:
        # User's answer is incorrect
        bot.send_message(message.chat.id, "Sorry, that's not the correct answer. Try again!")

# Start the bot
bot.infinity_polling()
