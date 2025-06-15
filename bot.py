import telebot
from telebot import types

# Твой токен
TOKEN = '8074984580:AAG45LhOCjxRbynmksTqez8HV8BQkX8279w'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    standoff_button = types.InlineKeyboardButton(text="📥 Скачать чит на Standoff 2", url="https://liget.ru/cheatsgames")
    markup.add(standoff_button)
    bot.send_message(message.chat.id, "Добро пожаловать!\n\nВыберите, что хотите сделать 👇", reply_markup=markup)

# Запускаем бота
bot.polling()
