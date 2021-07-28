import telebot
import datetime 
import os
import pickle

from telebot import types 
from dotenv import load_dotenv

class User:
    def __init__(self,user_name = "default"):
        self.user_name = user_name
        self.records = []   #[Date,"cost type","product",dollars]
        self.file_path = "save/"

    def set_user_name(self,user_name):
        self.user_name = user_name
        return True

    def create_record(self,cost : list)->str:
        self.records.append(cost)
        return str(self.records[-1])

    def delete_record(self,indexs : list):
        targets = ""
        for index in indexs:
            if index.isdecimal():
                targets = targets + str(self.records[int(index)]) + "\n"
                self.records.pop(int(index))
        return targets

    def show_records(self,indexs : list)->str:
        if not self.records:
            return "No records!"
        else:
            result = ""
            if indexs:
                for index in indexs:
                    result = result + str(self.records[int(index)]) + "\n"
            else:
                for record in self.records:
                    result = result + str(record) + "\n"
            return result

    def save_records(self)->str:
        if not os.path.isdir(self.file_path):
            os.mkdir(self.file_path)
        with open(self.file_path+ self.user_name,"wb") as f:
            pickle.dump(self.records,f)
            f.close()
        return "Save complete!"

    def load_records(self)->str:
        try:
            with open(self.file_path+ self.user_name,"rb") as f:
                self.records = pickle.load(f)
                f.close()
            return "Load complete!"
        except:
            return "Your user_name does not have any saved file!"
        
load_dotenv(dotenv_path='/Users/liyun/program/telegrambot/.env')


TOKEN = os.getenv('TB_TOKEN')
bot = telebot.TeleBot(TOKEN)
user = User()

@bot.message_handler(func=lambda message: True)
def parse(message):
    print(message.text)
    m = message.text.split(" ")
    print(m)
    if m[0] in ["set","Set"]:
        user.user_name = m[1] 
        bot.send_message(chat_id= message.chat.id,text = "You set your user name as:\n" + user.user_name)   
    elif m[0] in ["c","C","Create","create"]:
        if len(m) != 4:
            return "Format error! Please type again!"
        cost = m[1::]
        bot.send_message(chat_id= message.chat.id,text = "You create a new record:\n" + user.create_record(cost))   
    elif m[0] in ["d","D","Delete","delete"]:
        targets = m[1::]
        bot.send_message(chat_id= message.chat.id,text = "You delete :\n" + user.delete_record(targets))   
    elif m[0] in ["show","Show"]:
        m.pop(0)
        bot.send_message(chat_id= message.chat.id,text = user.show_records(m))#怎麼輸入多個arguments?
    elif m[0] in ['Save','save']:
        bot.send_message(chat_id= message.chat.id,text = user.save_records()) #存入跟取出的檔案內容一樣嗎？
    elif m[0] in ['Load','load']:
        bot.send_message(chat_id= message.chat.id,text = user.load_records())
    else:
        bot.send_message(chat_id= message.chat.id,text = "Sorry, The format may be wrong.")

# @bot.message_handler(commands=['start'])
# def set_or_check_user(message):
#         userid = message.from_user.id
#         id = SQL.set_user_data(userid)
#         bot.send_message(chat_id= message.chat.id,text = str(id))


# @bot.message_handler(commands=['id'])
# def my_id(message):
#         id = message.from_user.id
#         res = SQL.get_user_id(id)
#         bot.send_message(chat_id= message.chat.id,text = res)

# @bot.message_handler(func=lambda message: message.text.find('\i') != -1)
# def insert_records(message):
#         User_id = SQL.get_user_id(message.from_user.id)
#         records = message.text.replace('\i','')
#         records = records.split(';')
#         return SQL.insert_records(records,User_id)

# @bot.message_handler(func=lambda message: message.text.find('\c') != -1)
# def check_the_month(message):
#     month = message.text.replace('\c','')
#     try:
#         record = SQL.show_the_month(month)
#         bot.send_message(chat_id= message.chat.id,text=record)
#     except:
#         bot.send_message(chat_id= message.chat.id,text='好像沒有這一個月的紀錄。')

# @bot.message_handler(func=lambda message: True)
# def parse(message):
#             bot.reply_to(message,'Sorry,I can\'t solve this matter')

bot.polling()

