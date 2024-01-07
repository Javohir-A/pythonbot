# import telebot
# from telebot import types
# API_TOKEN = '6690741839:AAGL9qyPmjXWWI9teG4It2dwxWunyrZss1o'
# bot = telebot.TeleBot(API_TOKEN)

# @bot.message_handler(commands=['userinfo'])
# def user_info(message):
#     user_id = message.from_user.id
#     username = message.from_user.username

#     if username is None:
#         # If user doesn't have a username, prompt for a name
#         bot.send_message(chat_id=user_id, text="Please enter your name")
        
#         @bot.message_handler(func=lambda message: True)
#         def user_name(message):
#             nonlocal username
#             username = message.text
#             bot.send_message(chat_id=user_id, text=f"Thank you, {username}! Your information has been recorded.")
            
#             # Write user info to a file
#     with open('userinfo.txt', 'a') as user_info:
#         check_info = f'{user_id}, {username}'
#         with open('userinfo.txt', 'r') as user_info_read:
#             user_info_data = user_info_read.read()
#         if check_info not in user_info_data:
#             user_info.write(f'{user_id}, {username}\n')
# def start(message):
#     # Create a keyboard with two buttons
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = types.KeyboardButton("Button 1")
#     button2 = types.KeyboardButton("Button 2")
#     # Add buttons to the keyboard
#     keyboard.add(button1, button2)
    
#     # Send a message with the keyboard
#     bot.send_message(message.chat.id, "Choose an option:", reply_markup=keyboard, parse_mode=None)

# @bot.message_handler(func=lambda message: True)
# def handle_all_messages(message):
#     # Handle other messages
#     bot.reply_to(message, f"You said: {message.text}")
# bot.infinity_polling()