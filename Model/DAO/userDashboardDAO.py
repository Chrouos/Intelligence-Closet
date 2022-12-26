
# 個人的帳號密碼 sql server, 請不要更動crudAccount.py (輸入自己的即可)
from Model.DAO.crudAccount import ExportSQLLink
from Model.Domain.userDashboard import UserDashboard

import pyodbc

class UserDashboardDAO:
	
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
			# print('UserDashboardDAO 操作成功')

		except:
			print('UserDashboardDAO 操作錯誤')

		self.cnxn = cnxn
		self.cursor = cnxn.cursor()

	# 搜尋所有資料: tuple
	def queryAll(self):
		execute_str = "SELECT * FROM intelligence_closet.dbo.user_dashboard;"
		# print("queryAll: ", execute_str)

		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()

		userDashBoardLists = []
		for data in datas:
			userDashBoard = UserDashboard()
			userDashBoard.updateBySQL(data)
			userDashBoardLists.append(userDashBoard)
		return userDashBoardLists
	
	# 透過Id查找一筆資料: tuple
	def queryById(self, id):
		execute_str = "SELECT * FROM intelligence_closet.dbo.user_dashboard WHERE Id = {0}".format(id)
		# print("queryById: ", execute_str)

		self.cursor.execute(execute_str)
		data = self.cursor.fetchone()

		userDashBoard = UserDashboard()
		if data != None:
			userDashBoard.updateBySQL(data)

		return userDashBoard

	def updateById(self, userDashboard, id):
		execute_str = "UPDATE intelligence_closet.dbo.user_dashboard SET " \
					+ "UserName='{0}', WeatherLike={1}, ModifyTime = GETDATE(), ".format(userDashboard.UserName, userDashboard.WeatherLike)\
					+ "VillageId={2}, Clock='{0}' WHERE Id = {1};".format(userDashboard.Clock, id, userDashboard.VillageId)
		# print("updateById: ", execute_str)

		self.cursor.execute(execute_str)
		self.cnxn.commit()

		return True

	def create(self, userDashboard):
		execute_str = "INSERT INTO intelligence_closet.dbo.user_dashboard " \
					+ "(UserName, WeatherLike, ModifyTime, VillageId, Clock) " \
					+ "VALUES('{0}', {1}, GETDATE(), '{2}', '{3}');".format(userDashboard.UserName, userDashboard.WeatherLike, userDashboard.StationName, userDashboard.Clock, userDashboard.CityId)
		# print("create: ", execute_str)

		self.cursor.execute(execute_str)
		self.cnxn.commit()

		return True


	def updateLastPosition(self, id, lastPosition):
		
		execute_str = "UPDATE intelligence_closet.dbo.user_dashboard SET LastPosition = {} WHERE Id = {};".format(lastPosition, id)
		# print("updateLastPosition: ", execute_str)

		self.cursor.execute(execute_str)
		self.cnxn.commit()

		return True