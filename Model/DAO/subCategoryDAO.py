
# 個人的帳號密碼 sql server, 請不要更動crudAccount.py (輸入自己的即可)
from Model.DAO.crudAccount import ExportSQLLink
from Model.Domain.subCategory import SubCategory

import pyodbc
import pandas as pd

class SubCategoryDAO:
	
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
			print('SubCategoryDAO 操作成功')

		except:
			print('SubCategoryDAO 操作錯誤')

		self.cnxn = cnxn
		self.cursor = cnxn.cursor()

	# 搜尋所有資料: tuple
	def queryAll(self):
		execute_str = "SELECT * FROM intelligence_closet.dbo.sub_category;"
		print("queryAll: ", execute_str)

		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()

		subCategoryLists = []
		for data in datas:
			subCategory = SubCategory()
			subCategory.updateBySQL(data)
			subCategoryLists.append(subCategory)
		return subCategoryLists
	
	# 透過Id查找一筆資料: tuple
	def queryById(self, id):
		execute_str = "SELECT * FROM intelligence_closet.dbo.sub_category WHERE Id = {0}".format(id)
		print("queryById: ", execute_str)

		self.cursor.execute(execute_str)
		data = self.cursor.fetchone()

		subCategory = SubCategory()
		subCategory.updateBySQL(data)

		return subCategory

	def queryByCategoryId(self, id):
		execute_str = "SELECT * FROM intelligence_closet.dbo.sub_category where CategoryId = {0};".format(id)
		print("queryByCategoryId: ", execute_str)

		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()

		subCategoryLists = []
		for data in datas:
			subCategory = SubCategory()
			subCategory.updateBySQL(data)
			subCategoryLists.append(subCategory)
		return subCategoryLists


	def updateScoreById(self, score, id):
		execute_str = "UPDATE intelligence_closet.dbo.sub_category SET Score = {0} WHERE Id = {1}".format(score, id)
		print("updateScoreById: ", execute_str)

		self.cursor.execute(execute_str)
		self.cnxn.commit()

		return True