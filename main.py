import telebot as tb
from telebot import types
import requests as rq
from bs4 import BeautifulSoup as BS
from dotenv import load_dotenv
import os


load_dotenv()

token = os.getenv('TOKEN')
bot = tb.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    bot.send_message(message.chat.id, f'Hello {name}.')

@bot.message_handler(commands=['search'])
def search(message):
    bot.send_message(message.chat.id, 'What would you like for me to search on wikipedia?')
    bot.register_next_step_handler(message, procces)

def procces(message):
    url = f'https://ru.wikipedia.org/wiki/{message.text}'
    res = rq.get(url)
    soup = BS(res.text, 'html.parser')
    res = soup.find('p')
    bot.send_message(message.chat.id, res.text)    

bot.polling(non_stop=True)