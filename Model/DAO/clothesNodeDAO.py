
# 個人的帳號密碼 sql server, 請不要更動crudAccount.py (輸入自己的即可)
from pickle import FALSE
from Model.DAO.crudAccount import ExportSQLLink
from Model.Domain.clothesNode import ClothesNode

import pyodbc
import time

class ClothesNodeDAO:
	
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
			print('ClothesNodeDAO 操作成功')

		except:
			print('ClothesNodeDAO 操作錯誤')
   
		self.cnxn = cnxn
		self.cursor = cnxn.cursor()
  
  
	###################### READ ######################
  
	# 搜尋所有資料: tuple
	def queryAll(self):
		execute_str = "SELECT * FROM intelligence_closet.dbo.clothes_node;"
		print("queryAll: ", execute_str)
  
		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()
  
		clothesNodeLists = []
		for data in datas:
			clothesNode = ClothesNode()
			clothesNode.updateBySQL(data)
			clothesNodeLists.append(clothesNode)
  
		return clothesNodeLists
  
	# 透過Id查找一筆資料: tuple
	def queryById(self, id):
		execute_str = "SELECT * FROM intelligence_closet.dbo.clothes_node WHERE Id = {0}".format(id)
		print("queryById: ", execute_str)
  
		self.cursor.execute(execute_str)
		data = self.cursor.fetchone()
  
		clothesNode = ClothesNode()
		clothesNode.updateBySQL(data)
  
		return clothesNode
    
	def queryByPosition(self, position):
		execute_str = "SELECT * FROM intelligence_closet.dbo.clothes_node WHERE [Position]  = {0}".format(position)
		print("queryByPosition: ", execute_str)
  
		self.cursor.execute(execute_str)
		data = self.cursor.fetchone()
  
		clothesNode = ClothesNode()
		clothesNode.updateBySQL(data)
  
		return clothesNode

     
	# 空缺的位置資訊(範圍 0~9 )
	def vacancyPosition(self):
		for i in range(10):
			# print("self.queryDataByPosition({0}): {1}".format(i, self.queryDataByPosition(i)))
			if self.queryDataByPosition(i) == None:
				return i

		return -1

    # 透過位置找尋資料
	def queryDataByPosition(self, position):
		execute_str = "SELECT * FROM intelligence_closet.dbo.clothes_node WHERE Position = '{0}' ".format(position)
		self.cursor.execute(execute_str)
		data = self.cursor.fetchone()
		return data

	# 最後一個位置
	def lastPosition(self):
		return self.sortNameDESC('Position')[1]

	# 大到小分類: name 想找尋的分類
	def sortNameDESC(self, name):
		execute_str = "SELECT * FROM intelligence_closet.dbo.clothes_node ORDER BY '{0}' DESC".format(name)

		self.cursor.execute(execute_str)
		data = self.cursor.fetchone()
		return data

	# 大到小分類: name 想找尋的分類
	def sortNameDESC(self, name):
		execute_str = "SELECT * FROM intelligence_closet.dbo.clothes_node ORDER BY '{0}' ASC".format(name)

		self.cursor.execute(execute_str)
		data = self.cursor.fetchone()
		return data

	###################### CREATE ######################
	
	def create(self, clothesNode_dict):
		position = self.vacancyPosition()
		if position == -1:
			print("位置已滿")
			return False


		execute_str = "INSERT INTO clothes_node (Position, ColorId, SubCategoryId, UsageCounter, CreateTime, ModifyTime , FilePosition) " \
                    + "VALUES ({0}, {1}, {2}, 0, GETDATE(), GETDATE(), '{3}' )".format(position, clothesNode_dict['ColorId'], clothesNode_dict['SubCategoryId'], clothesNode_dict['FilePosition'])
        
		print("create", execute_str)
		self.cnxn.cursor().execute(execute_str)
		self.cnxn.commit()
  
		return position
        
   	###################### UPDATE ######################
	def updatePositionToNull(self, position):
    
		if self.queryDataByPosition(position) == None:
			print('沒有此衣物')
			return False

		execute_str = "UPDATE clothes_node SET Position = NULL WHERE Position = {0}".format(position)
		print(execute_str)
  
		self.cursor.execute(execute_str)
		self.cnxn.commit()
  
		return True

   	###################### DELETE ######################
	def deleteByPosition(self, position):
    
		if self.queryDataByPosition(position) == None:
			print('沒有此衣物')
			return False

		execute_str = "DELETE FROM clothes_node WHERE Position = {0}".format(position)
		print(execute_str)
  
		self.cursor.execute(execute_str)
		self.cnxn.commit()
  
		return True