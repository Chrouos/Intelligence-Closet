
# 個人的帳號密碼 sql server, 請不要更動crudAccount.py (輸入自己的即可)
from Model.DAO.crudAccount import ExportSQLLink
from Model.Domain.station import Station

import pyodbc

class StationDAO:
	
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
			print('StationDAO 操作成功')

		except:
			print('StationDAO 操作錯誤')
	
		self.cnxn = cnxn
		self.cursor = cnxn.cursor()
	
	# 搜尋所有資料: tuple
	def queryAll(self):
		execute_str = "SELECT * FROM intelligence_closet.dbo.station;"
		print("queryAll: ", execute_str)
	
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
	
		stationLists = []
		for data in datas:
			station = Station()
			station.updateBySQL(data)
			stationLists.append(station)
	
		return stationLists
	
	# 透過Id查找一筆資料: tuple
	def queryById(self, id):
		execute_str = "SELECT * FROM intelligence_closet.dbo.station WHERE Id = {0}".format(id)
		print("queryById: ", execute_str)
	
		self.cursor.execute(execute_str)
		data = self.cursor.fetchone()
	
		station = Station()
		station.updateBySQL(data)
	
		return station
		
	def queryByCityId(self, cityId):
		execute_str = "SELECT * FROM intelligence_closet.dbo.station WHERE CityId = '{0}'".format(cityId)
		print("queryByCityId: ", execute_str)
	
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
	
		stationLists = []
		for data in datas:
			station = Station()
			station.updateBySQL(data)
			stationLists.append(station)
	

		return stationLists

	def create(self, station):
		print(station)
		execute_str = "INSERT INTO station (StationNumber, StationName, CityId, [Address], CreateTime,  Remark, ModifyTime, Work) VALUES (" \
					+ "'{0}', '{1}', {2}, '{3}', GETDATE(), '{4}', GETDATE(), '{5}')".format(	station.StationNumber, 
																								station.StationName, 
																								station.CityId, 
																								station.Address,
																								station.Remark, 
																								station.Work)
		print("create: ", execute_str)
		self.cnxn.cursor().execute(execute_str)
		self.cnxn.commit()

		return True

	def deleteAllData(self):
		execute_str = "TRUNCATE TABLE intelligence_closet.dbo.station "
		print("deleteAllData: ", execute_str)
		self.cnxn.cursor().execute(execute_str)
		self.cnxn.commit()
	
		return True  

	def deleteById(self, id):
		execute_str = "DELETE FROM intelligence_closet.dbo.station WHERE Id = {0};".format(id)
		print("deleteById: ", execute_str)
		self.cnxn.cursor().execute(execute_str)
		self.cnxn.commit()
	
		return True  