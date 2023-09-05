import telebot
from bot_token import tot
from telebot import types


bot = telebot.TeleBot(tot)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет ✌️ ")
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    but1 = telebot.types.KeyboardButton('🛍 Оформить заказ')
    but2 = telebot.types.KeyboardButton('💸 Калькулятор цен')
    but3 = telebot.types.KeyboardButton('🛩 Доставка')
    but4 = telebot.types.KeyboardButton('ℹ️ FAQ')

    keyboard.add(but1, but2, but3, but4)
    
    bot.send_message(message.chat.id, 'Я помошник по формированию заказов.\nПомагу вам сделать заказ', reply_markup=keyboard)
    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == '🛍 Оформить заказ':
        bot.send_message(message.chat.id,'')
    if message.text == '💸 Калькулятор цен':
        bot.send_message(message.chat.id,'')
    if message.text == '🛩 Доставка':
        bot.send_message(message.chat.id,'')
    if message.text == 'ℹ️ FAQ':
        bot.send_message(message.chat.id,'')
    else:
        bot.send_message(message.chat.id,'Команда не распознана.😞\nВыберите вариант придложанный из кнопок.')


bot.infinity_polling()


