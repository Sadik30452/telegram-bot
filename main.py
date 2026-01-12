import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Auto approve join requests
@bot.chat_join_request_handler()
def approve_request(request):
    try:
        bot.approve_chat_join_request(request.chat.id, request.from_user.id)
        print("Approved:", request.from_user.username)
    except:
        pass

bot.infinity_polling()
