import os
import telebot
from dotenv import load_dotenv
from telebot import types

# loading bot data
load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


# --------------------BOT COMMANDS -------------------
@bot.message_handler(commands=['selfie'])
def get_char(message):
    markup = types.InlineKeyboardMarkup()
    key_old = types.InlineKeyboardButton(text='старое селфи', callback_data='old')
    key_new = types.InlineKeyboardButton(text='новое селфи', callback_data='new')
    markup.add(key_old, key_new)
    bot.send_message(message.chat.id, text='Какое?', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_list(message):
    bot.send_message(message.chat.id,
                     '<i> You can type time of the day, say hello, ask me about my friend, my troubles, what I think about us and just type chat to talk \nWe can talk about Ascension too, if you want </>',
                     parse_mode='html')


@bot.message_handler(commands=['lang'])
def set_lang(message):
    keyboard = types.InlineKeyboardMarkup()
    key_jp = types.InlineKeyboardButton(text='🇯🇵 japanese', callback_data='jp')
    keyboard.add(key_jp)
    key_en = types.InlineKeyboardButton(text='🇬🇧 english', callback_data='en')
    keyboard.add(key_en)
    bot.send_message(message.chat.id, text='💬 please choose language', reply_markup=keyboard)


# -------------------BOT CHATTING----------------
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     # getting phrases from voice data
#     if message.text:
#         bot.send_message(message.chat.id, '<i>' + msg + '</>', parse_mode='html')
#         bot.send_audio(message.chat.id, audio=(result[1]))


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'old':
        bot.send_message(call.message.chat.id, 'Вот моё старое селфи')
        bot.send_photo(call.message.chat.id,
                       'https://meowpassion.com/wp-content/uploads/2019/07/back-to-school-white-cat.jpg')
    elif call.data == 'new':
        bot.send_message(call.message.chat.id, 'Вот моё новое селфи')
        bot.send_photo(call.message.chat.id,
                       'https://www.learningliftoff.com/wp-content/uploads/2015/04/Gaming-cat-computer-cats.jpg')


if __name__ == '__main__':
    bot.infinity_polling()
