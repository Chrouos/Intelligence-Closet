
# 個人的帳號密碼 sql server, 請不要更動crudAccount.py (輸入自己的即可)
from Model.DAO.crudAccount import ExportSQLLink
from Model.Domain.userCombs import UserCombs

import pyodbc
import pandas as pd

class UserCombsDAO:
	
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
			print('UserCombsDAO 操作成功')

		except:
			print('UserCombsDAO 操作錯誤')

		self.cnxn = cnxn
		self.cursor = cnxn.cursor()

	# 搜尋所有資料: tuple
	def queryAll(self):
		execute_str = "SELECT * FROM intelligence_closet.dbo.user_combs;"
		print("queryAll: ", execute_str)

		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()

		userCombsLists = []
		for data in datas:
			userCombs = UserCombs()
			userCombs.updateBySQL(data)
			userCombsLists.append(userCombs)
		return userCombsLists
	
	# 透過Id查找一筆資料: tuple
	def queryById(self, id):
		execute_str = "SELECT * FROM intelligence_closet.dbo.user_combs WHERE Id = {0}".format(id)
		print("queryById: ", execute_str)

		self.cursor.execute(execute_str)
		data = self.cursor.fetchone()

		userCombs = UserCombs()
		if data != None:
			userCombs.updateBySQL(data)

		return userCombs

	def queryByClothes1Id(self, id):
		execute_str = "SELECT * FROM intelligence_closet.dbo.user_combs where Clothes1Id = {0};".format(id)
		print("queryByClothes1Id: ", execute_str)

		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()

		userCombsLists = []
		for data in datas:
			userCombs = UserCombs()
			userCombs.updateBySQL(data)
			userCombsLists.append(userCombs)
		return userCombsLists

	def queryByClothes2Id(self, id):
		execute_str = "SELECT * FROM intelligence_closet.dbo.user_combs where Clothes2Id = {0};".format(id)
		print("queryByClothes2Id: ", execute_str)

		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()

		userCombsLists = []
		for data in datas:
			userCombs = UserCombs()
			userCombs.updateBySQL(data)
			userCombsLists.append(userCombs)
		return userCombsLists

	def updateCombLikeById(self, score, id):
		execute_str = "UPDATE intelligence_closet.dbo.user_combs SET CombLike = {0}, ModifyTime = GETDATE() WHERE Id = {1}".format(score, id)
		print("updateCombLikeById: ", execute_str)

		self.cursor.execute(execute_str)
		self.cnxn.commit()

		return True

	def create(self, combs):
		execute_str = "INSERT INTO intelligence_closet.dbo.user_combs (Clothes1Id, Clothes2Id, CombLike, CreateTime, ModifyTime) VALUES (" \
					+ "{0}, {1}, {2}, GETDATE(), GETDATE() )".format(combs.Clothes1Id, combs.Clothes2Id, combs.CombLike)
		print("create: ", execute_str)

		self.cursor.execute(execute_str)
		self.cnxn.commit()

		return True