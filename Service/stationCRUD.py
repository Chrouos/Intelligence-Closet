import sys, os
sys.path.append(os.getcwd()) # 抓取路徑

import pyodbc
import pandas as pd
from crawler.crawler import station

class stationCRUD:
	
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
  
  
	################## CREATE START ##################
	def insertStation(self, data):
		cityId = self.queryCityByName(data[2])[0][0]
   
   	# 0.站號 1.站名 2.城市 3.地址 4.資料起始日期 5.備註
		execute_str = "INSERT INTO station (StationNumber, StationName, CityId, [Address], CreateTime,  Remark, ModifyTime, Work) VALUES (" \
									+ "'" + data[0] + "'" \
									+ ", '" + data[1] + "'" \
									+ ", " +  str(cityId) \
									+ ", '" + data[3] + "'" \
									+ ", '" + data[4] + "'" \
									+ ", '" + data[5] + "'" \
									+ ", GETDATE(), 1)"

		self.cnxn.cursor().execute(execute_str)
		self.cnxn.commit() # 送出
  
	def insertCity(self, cityName):
    
    # 是否有這個縣市 
		execute_str = "SELECT * FROM city WHERE CityName = '" + cityName + "'" 
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()

		# 若沒有就增加
		if datas == []:
			execute_str = "INSERT INTO city VALUES ('" + cityName + "')"
			self.cnxn.cursor().execute(execute_str)
			self.cnxn.commit()
   
	################## CREATE END ##################
 
	################## SELECT START ##################
	def queryCityByName(self, cityName):
		execute_str = "SELECT * FROM city Where CityName = '" + cityName + "'"
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
		return datas

	def queryStation(self):
		execute_str = "SELECT * FROM station"
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
		return datas

	def queryCity(self):
		execute_str = "SELECT * FROM city "
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
		return datas
 
	def refreshAllData(self):
		st = station()
		st.refreshDataByNet()  # 各站
		allCity = st.getAllCity(); # 各 City名稱
		allInfo = st.getAllInformation()
  
		for c in allCity:
			self.insertCity(c)

		for outIndex in range(len(allInfo)):
			self.insertStation(allInfo[outIndex])
			# print(allInfo[outIndex])