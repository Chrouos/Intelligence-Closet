import sys, os
sys.path.append(os.getcwd()) # 抓取路徑

import pyodbc
import pandas as pd

class colorCRUD:
	
	def __init__(self):	

		try:
			server = 'LAPTOP-BGP802KH\SQLEXPRESS'
			database = 'intelligence_closet'
			username = 'sa'
			password = 'asd464017'
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
		execute_str = "select * from color"
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
  	
		return list(datas)

  # 2. 搜尋從顏色中 ENG
	def queryIdByEngName(self, colorEngName):
		execute_str = "select Id from color where ColorEngName = '" + str(colorEngName) + "'"
		self.cursor.execute(execute_str)
		colorId = self.cursor.fetchone()
    
		return colorId[0]


# 