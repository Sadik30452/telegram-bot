import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Bot is running 🚀")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "You said: " + message.text)

bot.infinity_polling()
