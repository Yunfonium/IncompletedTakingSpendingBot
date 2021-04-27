import telebot
import datetime 
import SQLtest as SQL
from telebot import types 


TOKEN = '1432156287:AAEEdp6rVT9JHjy0Eh6pO9PCGEmuAFyc7jU'
bot = telebot.TeleBot(TOKEN)
    

@bot.message_handler(commands=['start'])
def create_new_database(message):
    bot.reply_to(message,"Hi! For starting my serice. I need to make your first cost")

@bot.message_handler(commands=['s'])
def select(message):
    chat_id = message.chat.id
    # or add KeyboardButton one row at a time:
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('新開銷')
    itembtn2 = types.KeyboardButton('刪除紀錄')
    itembtn3 = types.KeyboardButton('修改紀錄')
    itembtn4 = types.KeyboardButton('查看紀錄')
    markup.row(itembtn1,itembtn2)
    markup.row(itembtn3,itembtn4)
    bot.send_message(chat_id, "你需要什麼呢？", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.find('\c') != -1)
def check_the_month(message):
    month = message.text.replace('\c','')
    try:
        record = SQL.show_the_month(month)
        bot.send_message(chat_id= message.chat.id,text=record)
    except:
        bot.send_message(chat_id= message.chat.id,text='好像沒有這一個月的紀錄。')

'''bot.send_message(chat_id= message.chat.id,text='你打錯囉')'''



'''
@bot.message_handler(func=lambda message: message.text == '查看紀錄')
def show_all_table(message):
    bot.send_message(chat_id= message.chat.id,text='你想要看哪一天的紀錄？\n請打YYYYMMDD的格式。')
    alltables = 'Here are your tables! : \n'
    for x in SQL.show_all_month():
        alltables = alltables + str(x) + '\n'
    bot.send_message(chat_id= message.chat.id,text=alltables)

@bot.message_handler(func=lambda message: message.text == '新開銷')
def insert_makemoney(message):
    while True:
        bot.send_message(chat_id= message.chat.id,text='請輸入金額：')
'''


@bot.message_handler(func=lambda message: True)
def parse(message):
            bot.reply_to(message,'Sorry,I can\'t solve this matter')

bot.polling()

