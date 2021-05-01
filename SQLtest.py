import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'telegrambot',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

def show_all_cost(user_id):
    sql = 'SELECT * FROM records WHERE User_id = ?' + user_id
    mycursor.execute(sql)
    record = mycursor.fetchall()
    return record

def show_all_month():
    sql = 'SELECT * FROM ALLTABLES'
    mycursor.execute(sql)
    myrecord = mycursor.fetchall()
    return myrecord
def show_the_month(month):
    sql = 'SELECT * FROM ' + month
    mycursor.execute(sql)
    record = mycursor.fetchall()
    return str(record)

def insert_new_spending(Date = datetime.datetime.now , Genre = '' , Cost = 0):
    sql = 'INSERT INTO default '
    val = 'VALUE (' + Date + ',' + Genre + ',' + Cost + ')'
    mycursor.execute(sql,val)



