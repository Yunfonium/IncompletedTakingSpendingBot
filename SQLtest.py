import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Yunfonium930435',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

def create_a_new_table(tablename,column):
    sql = "CREATE TABLE "
    tb = tablename
    col = "(" + column +")"
    mycursor.execute(sql,tb,col)

def drop_a_table(tablename):
    sql = 'DROP TABLE '
    mycursor.execute(sql,tablename)

def edit_table_name(oldname,newname):
    sql = 'RENAME TABLE ' + oldname + 'TO ' + newname
    mycursor.execute(sql)

def show_tables(tablename):
    sql = 'SELECT' + tablename
    mycursor.execute(sql)

def insert_new_spending():
    pass



