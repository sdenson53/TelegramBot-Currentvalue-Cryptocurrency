import time
import telebot
import requests


TOKEN = "your telegram bot token obtained from BotFather"
bot = telebot.TeleBot(token=TOKEN)

def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i

@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, 'Hi There! \n Enter /btc to get current value'
                          ' \n or @username to get a link to instagram account')

@bot.message_handler(commands=['btc']) # help message handler
def send_welcome(message):
    api = requests.get(url='https://blockchain.info/tobtc?currency=USD&value=1')
    dd = api.json()
    xx = 1/dd
    bot.reply_to(message, xx)

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
# lambda function finds messages with the '@' sign in them
# in case msg.text doesn't exist, the handler doesn't process it
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '@':  # in case it's just the '@', skip
        pass
    else:
        insta_link = "https://instagram.com/{}".format(at_text[1:])
        bot.reply_to(message, insta_link)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception:
        time.sleep(15)
