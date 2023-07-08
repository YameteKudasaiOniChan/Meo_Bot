from time import sleep
from telebot import TeleBot

bot_token = ''
bot = TeleBot(bot_token)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    text = message.text
    text = text.split()
    for t in text:
        if t == "معو" or t == "ماعو" or t == "meo" or t == "Meo" or t == "MEO":
            bot.reply_to(message, t)


bot.infinity_polling()
