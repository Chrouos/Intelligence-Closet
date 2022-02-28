import pyodbc
import pandas as pd

from nodeCRUD import nodeCRUD

try:
    server = 'LAPTOP-BGP802KH\SQLEXPRESS'
    database = 'intelligence_closet'
    username = 'sa'
    password = 'asd464017'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server +
                          ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    print('操作成功')
except:
    print('操作錯誤')

crud = nodeCRUD(cnxn)
