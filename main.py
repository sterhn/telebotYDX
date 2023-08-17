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


@bot.message_handler(commands=['hobby'])
def hobby(message):
    bot.send_message(message.chat.id, text='Мне очень нравится вязать. Обычно я вижу разные маленькие игрушки. Их '
                                           'иногда называют амигуруми. Мне нравится вязать потому что я могу это '
                                           'делать одновременно с просмотром любимых сериалов')


@bot.message_handler(commands=['source'])
def source(message):
    bot.send_message(message.chat.id, text='https://github.com/sterhn/telebotYDX')


@bot.message_handler(commands=['voice'])
def voice(message):
    markup = types.InlineKeyboardMarkup()
    key_love = types.InlineKeyboardButton(text='о любви', callback_data='love')
    key_chat = types.InlineKeyboardButton(text='о ChatGPT', callback_data='chatgpt')
    key_sql = types.InlineKeyboardButton(text='SQL и NoSQL', callback_data='sql')
    markup.add(key_love)
    markup.add(key_chat)
    markup.add(key_sql)
    bot.send_message(message.chat.id, text='О чём ты хочешь послушать?', reply_markup=markup)


# ----------BUTTONS---------------------------------
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
    elif call.data == 'chatgpt':
        bot.send_message(call.message.chat.id, 'Вот что такое ChatGPT')
        bot.send_voice(call.message.chat.id, 'AwACAgIAAxkBAAMsZN3EmbDf20KdydeuRzpf9c9bmIcAAuYwAAKjCeBKpcsruOl5g4owBA')

    elif call.data == 'love':
        bot.send_message(call.message.chat.id, 'Предлагаю послушать песню о любви')
        bot.send_message(call.message.chat.id, 'https://www.youtube.com/watch?v=HEXWRTEbj1I')
    elif call.data == 'sql':
        bot.send_message(call.message.chat.id, 'Вот разница между SQL и NoSQL')
        bot.send_voice(call.message.chat.id, 'AwACAgIAAxkBAAMyZN3E - o0jNAYXHcDfLgut6UFTtecAAuowAAKjCeBKUDEmVoq69qgwBA')


if __name__ == '__main__':
    bot.infinity_polling()
