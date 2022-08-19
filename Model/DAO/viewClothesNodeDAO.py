
# 個人的帳號密碼 sql server, 請不要更動crudAccount.py (輸入自己的即可)
from Model.DAO.crudAccount import ExportSQLLink
from Model.Domain.viewClothesNode import ViewClothesNode

import pyodbc

class ViewClothesNodeDAO:
	
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
			print('ViewClothesNodeDAO 操作成功')

		except:
			print('ViewClothesNodeDAO 操作錯誤')
	
		self.cnxn = cnxn
		self.cursor = cnxn.cursor()
	
	# 搜尋所有資料: tuple
	def queryAll(self):
		execute_str = "SELECT * FROM intelligence_closet.dbo.v_clothes_node;"
		print("queryAll: ", execute_str)
	
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
	
		viewClothesNodeLists = []
		for data in datas:
			viewClothesNode = ViewClothesNode()
			viewClothesNode.updateBySQL(data)
			viewClothesNodeLists.append(viewClothesNode)
	
		return viewClothesNodeLists
	
	# 透過Id查找一筆資料: tuple
	def queryById(self, id):
		execute_str = "SELECT * FROM intelligence_closet.dbo.v_clothes_node WHERE Id = {0}".format(id)
		print("queryById: ", execute_str)
	
		self.cursor.execute(execute_str)
		data = self.cursor.fetchone()
	
		viewClothesNode = ViewClothesNode()
		viewClothesNode.updateBySQL(data)
	
		return viewClothesNode

	def queryPositionExitNode(self):
		execute_str = "SELECT * FROM intelligence_closet.dbo.v_clothes_node WHERE [Position] IS NOT NULL;"
		print("queryPositionExitNode: ", execute_str)
	
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
	
		viewClothesNodeLists = []
		for data in datas:
			viewClothesNode = ViewClothesNode()
			viewClothesNode.updateBySQL(data)
			viewClothesNodeLists.append(viewClothesNode)
	
		return viewClothesNodeLists

	# 搜尋所有資料: tuple
	def queryUpperAll(self):
		execute_str = "SELECT * FROM v_clothes_node vcn WHERE CategoryId = 1;"
		print("queryUpperAll: ", execute_str)
	
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
	
		viewClothesNodeLists = []
		for data in datas:
			viewClothesNode = ViewClothesNode()
			viewClothesNode.updateBySQL(data)
			viewClothesNodeLists.append(viewClothesNode)
	
		return viewClothesNodeLists

	# 搜尋所有資料: tuple
	def queryLowerAll(self):
		execute_str = "SELECT * FROM v_clothes_node vcn WHERE CategoryId = 2;"
		print("queryLowerAll: ", execute_str)
	
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
	
		viewClothesNodeLists = []
		for data in datas:
			viewClothesNode = ViewClothesNode()
			viewClothesNode.updateBySQL(data)
			viewClothesNodeLists.append(viewClothesNode)
	
		return viewClothesNodeLists

	# 搜尋所有資料: tuple
	def queryOtherAll(self):
		execute_str = "SELECT * FROM v_clothes_node vcn WHERE CategoryId != 1 AND CategoryId != 2;"
		print("queryOtherAll: ", execute_str)
	
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
	
		viewClothesNodeLists = []
		for data in datas:
			viewClothesNode = ViewClothesNode()
			viewClothesNode.updateBySQL(data)
			viewClothesNodeLists.append(viewClothesNode)
	
		return viewClothesNodeLists