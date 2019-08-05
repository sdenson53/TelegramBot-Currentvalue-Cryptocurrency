import time
import telebot
import requests
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()
TOKEN = "648843546:AAE_-WfnWrFqjSeSiiCeMgHK1YY2AvDn07M"
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])  # welcome message handler
def send_welcome(message):
    bot.reply_to(message, 'Hi There!...Enter: \n /btc : current Bitcoin value \n /eth : current Ethereum value\n'
                          ' /ltc : current Litecoin value \n /xrp : current ripple value')


@bot.message_handler(commands=['btc'])  # bitcoin
def send_welcome(message):
    api = requests.get(url='https://blockchain.info/tobtc?currency=USD&value=1')
    dd = api.json()
    xx = 1 / dd
    b = '$' + str(xx)
    bot.reply_to(message, b)


@bot.message_handler(commands=['eth'])  # ethereum
def send_welcome(message):
    a = str(cg.get_price(ids='ethereum', vs_currencies='usd'))
    b = '$' + a[21:27]
    bot.reply_to(message, b)


@bot.message_handler(commands=['ltc'])  # litecoin
def send_welcome(message):
    a = str(cg.get_price(ids='litecoin', vs_currencies='usd'))
    b = '$' + a[21:27]
    bot.reply_to(message, b)


@bot.message_handler(commands=['xrp'])  # ripple
def send_welcome(message):
    a = str(cg.get_price(ids='ripple', vs_currencies='usd'))
    b = '$' + a[19:26]
    bot.reply_to(message, b)


while True:
    try:
        bot.polling(none_stop=True)
    except Exception:
        time.sleep(15)
