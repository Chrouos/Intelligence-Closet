
# 個人的帳號密碼 sql server, 請不要更動crudAccount.py (輸入自己的即可)
from Model.DAO.crudAccount import ExportSQLLink
from Model.Domain.colorGraph import ColorGraph

import pyodbc
import pandas as pd

class ColorGraphDAO:
	
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
			# print('ColorGraphDAO 操作成功')

		except:
			print('ColorGraphDAO 操作錯誤')

		self.cnxn = cnxn
		self.cursor = cnxn.cursor()

	# 搜尋所有資料: tuple
	def queryAll(self):
		execute_str = "SELECT * FROM intelligence_closet.dbo.color_graph;"
		# print("queryAll: ", execute_str)

		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()

		colorGraphLists = []
		for data in datas:
			colorGraph = ColorGraph()
			colorGraph.updateBySQL(data)
			colorGraphLists.append(colorGraph)
		return colorGraphLists
	
	
	
	# 透過Id查找一筆資料: tuple
	def queryById(self, id):
		execute_str = "SELECT * FROM intelligence_closet.dbo.color_graph WHERE Id = {0}".format(id)
		# print("queryById: ", execute_str)

		self.cursor.execute(execute_str)
		data = self.cursor.fetchone()

		colorGraph = ColorGraph()
		colorGraph.updateBySQL(data)

		return colorGraph

	def queryUpperByColorId(self, id):
		execute_str = "SELECT * FROM intelligence_closet.dbo.color_graph where ColorId1 = {0};".format(id)
		# print("queryUpperByColorId: ", execute_str)

		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()

		colorGraphLists = []
		for data in datas:
			colorGraph = ColorGraph()
			colorGraph.updateBySQL(data)
			colorGraphLists.append(colorGraph)
		return colorGraphLists

	def queryLowerByColorId(self, id):
		execute_str = "SELECT * FROM intelligence_closet.dbo.color_graph where ColorId2 = {0};".format(id)
		# print("queryUpperByColorId: ", execute_str)

		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()

		colorGraphLists = []
		for data in datas:
			colorGraph = ColorGraph()
			colorGraph.updateBySQL(data)
			colorGraphLists.append(colorGraph)
		return colorGraphLists

	def updateColorScoreById(self, colorScore, id):
		execute_str = "UPDATE intelligence_closet.dbo.color_graph SET ColorScore = {0} WHERE Id = {1}".format(colorScore, id)
		# print("updateColorScoreById: ", execute_str)

		self.cursor.execute(execute_str)
		self.cnxn.commit()

		return True