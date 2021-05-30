import telebot
import datetime 
import os
import SQLtest as SQL
from telebot import types 


TOKEN = os.getenv('TB_TOKEN')
bot = telebot.TeleBot(TOKEN)
    

@bot.message_handler(commands=['start'])
def set_or_check_user(message):
        id = message.from_user.id
        status = SQL.set_user_data(id)
        bot.send_message(chat_id= message.chat.id,text = str(status))


@bot.message_handler(commands=['id'])
def my_id(message):
        id = message.from_user.id
        res = SQL.get_user_id(id)
        bot.send_message(chat_id= message.chat.id,text = res)


@bot.message_handler(func=lambda message: message.text.find('\i') != -1)
def insert_records(message):
        User_id = SQL.get_user_id(message.from_user.id)
        records = message.text.replace('\i','')
        records = records.split(';')
        return SQL.insert_records(records,User_id)


@bot.message_handler(func=lambda message: message.text.find('\c') != -1)
def check_the_month(message):
    month = message.text.replace('\c','')
    try:
        record = SQL.show_the_month(month)
        bot.send_message(chat_id= message.chat.id,text=record)
    except:
        bot.send_message(chat_id= message.chat.id,text='好像沒有這一個月的紀錄。')

@bot.message_handler(func=lambda message: True)
def parse(message):
            bot.reply_to(message,'Sorry,I can\'t solve this matter')

bot.polling()

