import telebot
from telebot import types
import random

# তোর টোকেন এখানে অলরেডি বসানো আছে
API_TOKEN = '8534898185:AAFjRbFB8Z3wJ7IMPEtkOr_ONh-veoCSHmQ'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add("📜 কবিতা", "🎵 গান")
    bot.send_message(message.chat.id, f"💖 হ্যালো কিউট {name}! আপনার জন্য স্পেশাল বট রেডি। 🎀", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def handle(m):
    name = m.from_user.first_name
    if m.text == "📜 কবিতা": 
        bot.send_message(m.chat.id, f"ওগো প্রিয় {name},\nতুমি আমার সুখের ঠিকানা।\nসব সময় পাশে থেকো,\nহারিয়ে যেও না। 💖")
    elif m.text == "🎵 গান": 
        bot.send_message(m.chat.id, f"🎶 {name} তোমার জন্য আমি গান গাই...\nতুমি আমার জানের জান, তোমায় ভালোবাসি তাই। ❤️")

bot.infinity_polling()
