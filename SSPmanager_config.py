#Configure Windows system to work with SSP Manager program
from time import sleep
import os
import webbrowser as web
from random import randint

#mysql database username and password
user_name = 'root'
passwd = 'password'
model_list = ['achiver','splendor','mastro','bullet','thunderbird','rx100','fazer','ray']
model_items = [8, 10, 7, 8, 9, 8, 8, 6]
#Funtion to install required modules for the main program using pip install
def install_modules(modules):
    print('Installing modules!\nThis may take some time....')
    for module in modules:
        module = 'python -m pip install {}'.format(module)
        os.system(module)
    print('Modules import Completed!')
#Create the required database
def create_DB():
    import mysql.connector as sql
    print('Connecting to MySQL Server...')
    try:
        server = sql.connect(
        host='localhost',
        user=user_name,
        password=passwd,
        port=3306,
        auth_plugin='mysql_native_password',
        )
    except:
        print('Missing MySQL Server\nConfiguration processes cancled!')
        print('Check User name and Password')
        web.open_new_tab('https://dev.mysql.com/downloads/installer/')
        sleep(5)
    print('Server Connected!')
    sleep(1)
    my_cursor = server.cursor()
    print(my_cursor)
    try:
        my_cursor.execute('drop database SparePartsManager;')
    except:
        print('Creating Database for SSP Manager.....\n')
    my_cursor.execute('create database SparePartsManager;')
    print('\nDatabase Created!')
    sleep(0.5)
    my_cursor.close()
#Create required tables update sample data and clear table data
def create_table():
    import mysql.connector as sql
    print('Connecting to SparePartsManager Database')
    server = sql.connect(
        host='localhost',
        user=user_name,
        password=passwd,
        port=3306,
        auth_plugin='mysql_native_password',
        database='SparePartsManager'
        )
    print(server)
    my_cursor=server.cursor()
    print('Creating Sales Data Table!')
    my_cursor.execute("CREATE TABLE salesdata(Date varchar(50), Item varchar(40), Price int, Count int, Brand varchar(25), VechileType varchar(2),primary key(Date));")
    print('Sales Data Table created...')
    sleep(2)
    my_cursor.execute("insert into salesdata values('0000-00-00','abcdefg', 000, 0, 'abcd', 'Wx');")
    print('Sample data uploaded to database\n\nPrinting Sample data')
    print('Creating Stock tables for each brand')
    for i in range(len(model_list)):
        cmd = 'CREATE TABLE {}(Stock smallint)'.format(model_list[i])
        my_cursor.execute(cmd)
    server.commit()
    print('Updating Stock......')
    for i in range(len(model_items)):
        for j in range(model_items[i]):
            cmd = 'INSERT INTO {} values({})'.format(model_list[i],randint(20,50))
            #print(cmd)
            my_cursor.execute(cmd)
    sleep(0.5)
    print('Sample Stock List Created....')
    my_cursor.execute('select * from salesData;')
    for data in my_cursor:
        print(data)   
    sleep(2)
    my_cursor.execute("delete from salesdata;")
    server.commit()
    my_cursor.close()
def create_pdf_folder():
    try:
        os.mkdir('C:/SparePartsManagementSystem/SSP_Bills')
    except:
        print('Folder alredy existes')
#Main Program 
if __name__=='__main__':
    modules = ['tk', 'mysql-connector-python','pillow', 'numpy', 'matplotlib']
    install_modules(modules)
    create_DB()
    create_pdf_folder()
    sleep(1)
    create_table()
    print('Configuration Completed!')
    sleep(2)
