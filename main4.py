import telebot
import random
import time
import os
TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def scan(message):
  text = message.text.lower()
  
  if text == 'На дабл'.lower():
    bot.send_message(message.chat.id, random.randint(0, 99))
  elif text == 'На трипл'.lower():
    bot.send_message(message.chat.id, random.randint(100, 999))
  elif text == 'На квадрипл'.lower():
  	bot.send_message(message.chat.id, random.randint(1000, 9999))

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        time.sleep(15)