import telebot
import config
import tempfile
import pyttsx3

bot = telebot.TeleBot(config.TOKEN)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

@bot.message_handler(commands=['voice'])
def command_voice(message):
    #bot.send_message(message.chat.id, message.text)
    reply='OK'
    try:
        n=int(message.text[7:])
        engine.setProperty('voice', voices[n].id)
    except:
        reply="wrong voice number ("+message.text[7:]+")"
    bot.send_message(message.chat.id, reply)

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
