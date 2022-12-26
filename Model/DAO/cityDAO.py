
# 個人的帳號密碼 sql server, 請不要更動crudAccount.py (輸入自己的即可)
from Model.DAO.crudAccount import ExportSQLLink
from Model.Domain.city import City

import pyodbc
import pandas as pd

class CityDAO:
	
	# 建構子: 建立資料庫連線
	def __init__(self):	

		try:
		
			global_dict = ExportSQLLink() # 呼叫帳號密碼
		
			database = 'intelligence_closet'
			server = global_dict['server']
			username = global_dict['username']
			password = global_dict['password']
			cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server
									+ ';DATABASE=' + database
									+ ';UID=' + username
									+ ';PWD=' + password)
			self.cursor = cnxn.cursor()
			# print('CityDAO 操作成功')

		except:
			print('CityDAO 操作錯誤')
	
		self.cnxn = cnxn
		self.cursor = cnxn.cursor()
	
	# 搜尋所有資料: tuple
	def queryAll(self):
		execute_str = "SELECT * FROM intelligence_closet.dbo.city;"
		# print("queryAll: ", execute_str)
	
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
	
		cityLists = []
		for data in datas:
			city = City()
			city.updateBySQL(data)
			cityLists.append(city)
	
		return cityLists
	
	# 透過Id查找一筆資料: tuple
	def queryById(self, id):
		execute_str = "SELECT * FROM intelligence_closet.dbo.city WHERE Id = {0}".format(id)
		# print("queryById: ", execute_str)
	
		self.cursor.execute(execute_str)
		data = self.cursor.fetchone()
	
		city = City()
		city.updateBySQL(data)
	
		return city
    
	def queryByName(self, cityName):
		execute_str = "SELECT * FROM intelligence_closet.dbo.city WHERE CityName = '{0}'".format(cityName)
		# print("queryByName: ", execute_str)
	
		self.cursor.execute(execute_str)
		data = self.cursor.fetchone()
	
		city = City()
		city.updateBySQL(data)
	
		return city

	def create(self, cityName):
		
		city = self.queryIdByName(cityName)
		
		if city != None:
			print("CityName 已存在 ", city.Id, cityName)
			return False
		
		execute_str = "INSERT INTO city VALUES ('{0}')".format(cityName)
		# print("create: ", execute_str)
		self.cnxn.cursor().execute(execute_str)
		self.cnxn.commit()

		return True     

	def queryIdByName(self, cityName):
		execute_str = "SELECT * FROM intelligence_closet.dbo.city WHERE CityName = '{0}'".format(cityName)
		# print("queryByName: ", execute_str)
	
		self.cursor.execute(execute_str)
		data = self.cursor.fetchone()
		
	
		return data

	def deleteAllData(self):
		execute_str = "TRUNCATE TABLE intelligence_closet.dbo.city "
		# print("deleteAllData: ", execute_str)
		self.cnxn.cursor().execute(execute_str)
		self.cnxn.commit()
	
		return True     


