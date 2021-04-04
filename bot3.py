import telebot
import config
import tempfile
import pyttsx3

bot = telebot.TeleBot(config.TOKEN)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #[0] russian female, [2] English male, [3] English female 

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

