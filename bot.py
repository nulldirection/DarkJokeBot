import os
import random

import telebot
from telebot.types import Audio

TOKEN = "1977316434:AAGO0ceLtAHF25ZwMEEwem2-wvtjBC3gYmM"
bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('/start','Отправь шутку')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, 'Привет, чтобы получить шутку, напиши "Отправь шутку"', reply_markup=keyboard)
"""
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
"""

@bot.message_handler(content_types = ['text'])
def send_message(message):
	text = message.text.lower()
	if text == 'отправь шутку':
		bot.send_voice(message.chat.id, open(getRandomFile('jokes/'), 'rb'))

def getRandomFile(path):
  """
  Returns a random filename, chosen among the files of the given path.
  """
  files = os.listdir(path)
  index = random.randrange(0, len(files))
  print(files[index])
  return 'jokes/' + files[index]



bot.polling()