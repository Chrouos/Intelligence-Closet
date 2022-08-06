import sys, os
sys.path.append(os.getcwd()) # 抓取路徑

import pyodbc
import pandas as pd

# 個人的帳號密碼 sql server, 請不要更動crudAccount.py (輸入自己的即可)
from Service.crudAccount import exportSQLLink

global_dict = exportSQLLink()

class graphCRUD:
	
	def __init__(self):	

		try:
			database = 'intelligence_closet'
			server = global_dict['server']
			username = global_dict['username']
			password = global_dict['password']
			cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server
									+ ';DATABASE=' + database
									+ ';UID=' + username
									+ ';PWD=' + password)
			self.cursor = cnxn.cursor()
			print('操作成功')

		except:
			print('操作錯誤')
   
		self.cnxn = cnxn
		self.cursor = cnxn.cursor()
				
	def reconnect(self):
		self.cursor = self.cnxn.cursor()
  

	# 1. 搜尋全部徒圖型相關
	def queryAll(self):
		execute_str = "SELECT * FROM v_clothes_graph_edge WHERE Clothes1Position != ''  or Clothes1Position = 0"
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
  	
		return list(datas)

	# 2. 透過No回傳
	def queryById(self, id):
		execute_str = "SELECT * FROM v_clothes_graph_edge WHERE ViewId = " + str(id) 
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
  	
		return datas