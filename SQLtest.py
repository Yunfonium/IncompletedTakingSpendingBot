import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Yunfonium930435',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

def create_a_default_table():
    sql = "CREATE TABLE "
    tb = 'default '
    col = "(DATE date, GENRE nvarchar(max),COST float)"
    mycursor.execute(sql,tb,col)

def drop_a_table(tablename):
    sql = 'DROP TABLE '
    mycursor.execute(sql,tablename)

def edit_table_name(oldname,newname):
    sql = 'RENAME TABLE ' + oldname + 'TO ' + newname
    mycursor.execute(sql)

def show_tables(tablename):
    sql = 'SELECT * FROM ' + tablename
    mycursor.execute(sql)

def insert_new_spending():
    pass

def set_date(now = date.datetime.now):
    SELECT



