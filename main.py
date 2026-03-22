import telebot
from flask import Flask
from threading import Thread
import os
import requests

# Render mate mini server
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

# Tamaro Bot Token
TOKEN = '8683148346:AAEOfvR6fD7i9Wvmz0vvX_yd7JtJCFS3ASc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Priyam! Bot have Render par 24/7 chalu chhe! ✅\n\nCommands:\n/ip [address]")

@bot.message_handler(commands=['ip'])
def ip(message):
    try:
        addr = message.text.split()[1]
        data = requests.get(f"http://ip-api.com/json/{addr}").json()
        bot.reply_to(message, f"City: {data['city']}\nISP: {data['isp']}")
    except:
        bot.reply_to(message, "IP nakho.")

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    bot.polling(none_stop=True)
  
