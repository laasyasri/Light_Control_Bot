#!pip install adafruit-io
#!pip install python-telegram-bot

import os

from telegram.ext import Updater,CommandHandler
import requests

# 1. Python Code for Adafruit

x = os.getenv('adafruit_io_username') #ADAFRUIT_IO_USERNAME
y = os.getenv('adafruit_io_key') #ADAFRUIT_IO_KEY

from Adafruit_IO import Client, Feed
aio = Client(x,y)
feed = Feed(name = 'bot' ) #Create a feed
result = aio.create_feed(feed)
result

def send_value(indicator):
  #Sending a value to the feed
  from Adafruit_IO import Data
  val = Data(value= indicator)
  val_send = aio.create_data('bot', val)
  
# 2. Bot Coding with Python

def light_on(bot,update):
  url = 'https://p.kindpng.com/picc/s/61-617848_incandescent-light-bulb-lighting-transparency-and-translucency-yellow.png'
  chat_id=update.message.chat_id
  bot.send_message(chat_id,text = 'Turning on the Light')
  bot.send_photo(chat_id,photo=url)
  send_value(1)

def light_off(bot,update):
  url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSHaNDJvg4tlgQPBlhCqRMzpesxagwVtOr-bA&usqp=CAU'
  chat_id=update.message.chat_id
  bot.send_message(chat_id,text = 'Turning off the Light')
  bot.send_photo(chat_id,photo=url)
  send_value(0)

telegram_bot_api = os.getenv('telegram_bot_api')
u = Updater(telegram_bot_api)
dp = u.dispatcher
dp.add_handler(CommandHandler('on',light_on))
dp.add_handler(CommandHandler('off',light_off))
u.start_polling()
u.idle()
