import telebot
import fuction
from telebot import types

TOKEN = '1432156287:AAEEdp6rVT9JHjy0Eh6pO9PCGEmuAFyc7jU'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message,"Howdy, how are you doing?")

@bot.message_handler(commands=['s'])
def select(message):
    chat_id = message.chat.id
    # or add KeyboardButton one row at a time:
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('新開銷')
    itembtn2 = types.KeyboardButton('查看紀錄')
    itembtn3 = types.KeyboardButton('修改紀錄')
    markup.row(itembtn1)
    markup.row(itembtn2, itembtn3)
    bot.send_message(chat_id, "你需要什麼呢？", reply_markup=markup)

@bot.message_handler(commands=['新開銷','查看紀錄','修改紀錄'])
def newrow(message) :
    if message.text == '新開銷' :
        fuction.TakeSpending.NewTaking()



@bot.message_handler(func=lambda message: True)
def no_for_service(message):
    bot.reply_to(message,'Sorry,I can\'t solve this matter')





bot.polling()

