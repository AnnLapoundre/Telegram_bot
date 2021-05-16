import telebot
import config
import tempfile
import pyttsx3
from telebot import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


bot = telebot.TeleBot(config.TOKEN)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

@bot.message_handler(commands=['voice'])
def process_start_command(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_zero = types.InlineKeyboardButton(text = 'Russian', callback_data = '0')
    item_one = types.InlineKeyboardButton(text = 'American English Female', callback_data = '1')
    item_two = types.InlineKeyboardButton(text = 'American English Male', callback_data = '2')
    item_three = types.InlineKeyboardButton(text = 'English', callback_data = '3')
    item_four = types.InlineKeyboardButton(text = 'French', callback_data = '4')
    item_five = types.InlineKeyboardButton(text = 'Italian', callback_data = '5')
    item_six = types.InlineKeyboardButton(text = 'Japanese', callback_data = '6')
    item_seven = types.InlineKeyboardButton(text = 'Korean', callback_data = '7')
    item_eight = types.InlineKeyboardButton(text = 'Polish', callback_data = '8')
    item_nine = types.InlineKeyboardButton(text = 'German', callback_data = '9')

    markup_inline.add(item_zero, item_one, item_two, item_three, item_four, item_five, item_six, item_seven, item_eight, item_nine)
    bot.send_message(message.chat.id, 'Choose preferred voice', 
        reply_markup = markup_inline
    )

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == '2':
        bot.send_message(call.message.chat.id, 'Has been installed: American English Male')
        n = int(call.data)
        engine.setProperty('voice', voices[n].id)
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_voice = types.KeyboardButton('OK')
        item_error = types.KeyboardButton('no')
    elif call.data == '1':
        bot.send_message(call.message.chat.id, 'Has been installed: American English Female')
        n = int(call.data)
        engine.setProperty('voice', voices[n].id)
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_voice = types.KeyboardButton('OK')
        item_error = types.KeyboardButton('no')
    elif call.data == '0':
        bot.send_message(call.message.chat.id, 'Has been installed: Russian')
        n = int(call.data)
        engine.setProperty('voice', voices[n].id)
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_voice = types.KeyboardButton('OK')
        item_error = types.KeyboardButton('no')
    elif call.data == '3':
        bot.send_message(call.message.chat.id, 'Has been installed: English')
        n = int(call.data)
        engine.setProperty('voice', voices[n].id)
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_voice = types.KeyboardButton('OK')
        item_error = types.KeyboardButton('no')
    elif call.data == '4':
        bot.send_message(call.message.chat.id, 'Has been installed: French')
        n = int(call.data)
        engine.setProperty('voice', voices[n].id)
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_voice = types.KeyboardButton('OK')
        item_error = types.KeyboardButton('no')
    elif call.data == '5':
        bot.send_message(call.message.chat.id, 'Has been installed: Italian')
        n = int(call.data)
        engine.setProperty('voice', voices[n].id)
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_voice = types.KeyboardButton('OK')
        item_error = types.KeyboardButton('no')
    elif call.data == '6':
        bot.send_message(call.message.chat.id, 'Has been installed: Japanese')
        n = int(call.data)
        engine.setProperty('voice', voices[n].id)
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_voice = types.KeyboardButton('OK')
        item_error = types.KeyboardButton('no')
    elif call.data == '7':
        bot.send_message(call.message.chat.id, 'Has been installed: Korean')
        n = int(call.data)
        engine.setProperty('voice', voices[n].id)
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_voice = types.KeyboardButton('OK')
        item_error = types.KeyboardButton('no')
    elif call.data == '8':
        bot.send_message(call.message.chat.id, 'Has been installed: Polish')
        n = int(call.data)
        engine.setProperty('voice', voices[n].id)
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_voice = types.KeyboardButton('OK')
        item_error = types.KeyboardButton('no')
    elif call.data == '9':
        bot.send_message(call.message.chat.id, 'Has been installed: German')
        n = int(call.data)
        engine.setProperty('voice', voices[n].id)
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_voice = types.KeyboardButton('OK')
        item_error = types.KeyboardButton('no')


@bot.message_handler(content_types=['text'])
def lalala(message):
    #bot.send_message(message.chat.id, message.text)
    with tempfile.NamedTemporaryFile() as f:
        engine.save_to_file(message.text, f.name + '.mp3')
        engine.runAndWait()
        ff = open(f.name + '.mp3', 'rb')
        bot.send_voice(message.chat.id, ff)
        

#RUN
bot.polling(none_stop = True)
