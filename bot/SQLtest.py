import mysql.connector
import os
from dotenv import load_dotenv

#先存取我自己的.env
load_dotenv(dotenv_path='/Users/liyun/program/telegrambot/.env')

mydb = mysql.connector.connect(
    host = 'db',
    user = os.getenv('MYSQL_USER'),
    password = os.getenv('MYSQL_PASSWORD'),
    database = os.getenv('MYSQL_DATABASE')
)

mycursor = mydb.cursor(prepared=True)
def set_user_data(telegram_id)->str:
    try:
        sql1 = 'INSERT INTO users (user_telegram_id) VALUES (%s);'
        id = str(telegram_id)
        mycursor.execute(sql1,(id,))
        mydb.commit()
        return 'Setting OK!'
    except mysql.connector.Error as error:
        return 'You are already set up or there\'s something wrong!\nYou can try typing \'/id\' to check if you have an ID.'
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close() 

def get_user_id(telegramId):
    try:
        sql1 = 'SELECT id from users WHERE user_telegram_id = %s;'
        id = str(telegramId)
        mycursor.execute(sql1,(id,))
        mydb.commit() 
        User_id = mycursor.fetchall()
        return User_id
    except mysql.connector.Error as error:
        '''return 'Maybe you haven\'t set up! Please type \'/start\'.' '''
        return str(error)
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
    

def insert_records(records,User_id) -> str:
    try:
        sql1 = 'INSERT INTO records (User_id,Year,Month,Day,Cost,description) VALUE(%s,%s,%s,%s,%s,%s)'
        '''(Year,Month,Day,Cost,Description)'''
        tuple1 = (User_id,records[0],records[1],records[2],records[3],records[4])
        mycursor.execute(sql1,tuple1)
        mydb.commit()
        return 'Insert Success!'
    except mysql.connector.Error as error:
        return 'Format Error!' 
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()

def show_all_records(User_id):
    try:
        sql2 = 'SELECT * FROM records WHERE User_id = %S' 
        tuple1 = (User_id)
        mycursor.execute(sql2,tuple1)
        mydb.commit()
        record = mycursor.fetchall()
        return record
    except mysql.connector.Error as error:
        return 'Format Error!' 
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()

def show_month_records(User_id,Year,Month)->str:
    sql = 'SELECT * FROM records WHERE User_id = %S, Year = %S , Month = %S;'
    tuple1 = (User_id,Year,Month)
    mycursor.execute(sql)
    mydb.commit()
    myrecord = mycursor.fetchall()
    return myrecord
