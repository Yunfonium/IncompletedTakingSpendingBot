import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Yunfonium930435',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

def create_a_default_table(YearAndMonth):
    sql = "CREATE TABLE "
    tb = YearAndMonth
    col = " (DATE date, COST float, GENRE nvarchar(max))"
    mycursor.execute(sql,tb,col)

def drop_a_table(tablename):
    sql = 'DROP TABLE '
    mycursor.execute(sql,tablename)

def show_all_cost(tablename):
    sql = 'SELECT * FROM ' + tablename
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



