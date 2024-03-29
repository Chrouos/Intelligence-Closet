
# 個人的帳號密碼 sql server, 請不要更動crudAccount.py (輸入自己的即可)
from Model.DAO.crudAccount import ExportSQLLink
from Model.Domain.viewStation import ViewStation

import pyodbc

class ViewStationDAO:
	
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
			# print('ViewStationDAO 操作成功')

		except:
			print('ViewStationDAO 操作錯誤')
	
		self.cnxn = cnxn
		self.cursor = cnxn.cursor()
	
	# 搜尋所有資料: tuple
	def queryAll(self):
		execute_str = "SELECT * FROM intelligence_closet.dbo.v_station;"
		# print("queryAll: ", execute_str)
	
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
	
		viewStationLists = []
		for data in datas:
			viewStation = ViewStation()
			viewStation.updateBySQL(data)
			viewStationLists.append(viewStation)
	
		return viewStationLists
	
	# 透過Id查找一筆資料: tuple
	def queryById(self, id):
		execute_str = "SELECT * FROM intelligence_closet.dbo.v_station WHERE Id = {0}".format(id)
		# print("queryById: ", execute_str)
	
		self.cursor.execute(execute_str)
		data = self.cursor.fetchone()
	
		viewStation = ViewStation()
		viewStation.updateBySQL(data)
	
		return viewStation
		
	def queryByCityId(self, cityId):
		execute_str = "SELECT * FROM intelligence_closet.dbo.v_station WHERE CityId = '{0}'".format(cityId)
		# print("queryByCityId: ", execute_str)
	
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
	
		viewStationLists = []
		for data in datas:
			viewStation = ViewStation()
			viewStation.updateBySQL(data)
			viewStationLists.append(viewStation)
	

		return viewStationLists

	