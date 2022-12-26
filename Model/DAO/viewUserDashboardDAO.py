
# 個人的帳號密碼 sql server, 請不要更動crudAccount.py (輸入自己的即可)
from Model.DAO.crudAccount import ExportSQLLink
from Model.Domain.viewUserDashboard import ViewUserDashboard

import pyodbc

class ViewUserDashboardDAO:
	
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
			# print('ViewUserDashboardDAO 操作成功')

		except:
			print('ViewUserDashboardDAO 操作錯誤')

		self.cnxn = cnxn
		self.cursor = cnxn.cursor()

	# 搜尋所有資料: tuple
	def queryAll(self):
		execute_str = "SELECT * FROM intelligence_closet.dbo.v_user_dashboard;"
		# print("queryAll: ", execute_str)

		self.cursor.execute(execute_str)
		datas = self.cursor.fetchall()

		userDashBoardLists = []
		for data in datas:
			userDashBoard = ViewUserDashboard()
			userDashBoard.updateBySQL(data)
			userDashBoardLists.append(userDashBoard)
		return userDashBoardLists
	
	# 透過Id查找一筆資料: tuple
	def queryById(self, id):
		execute_str = "SELECT * FROM intelligence_closet.dbo.v_user_dashboard WHERE Id = {0}".format(id)
		# print("queryById: ", execute_str)

		self.cursor.execute(execute_str)
		data = self.cursor.fetchone()

		userDashBoard = ViewUserDashboard()
		if data != None:
			userDashBoard.updateBySQL(data)

		return userDashBoard

	def updateById(self, viewUserDashboard, id):
		execute_str = "UPDATE intelligence_closet.dbo.v_user_dashboard SET " \
					+ "UserName='{0}', WeatherLike={1}, ModifyTime = GETDATE(), ".format(viewUserDashboard.UserName, viewUserDashboard.WeatherLike)\
					+ "Clock='{0}', VillageId={1}, VillageName = {2}, ".format(viewUserDashboard.Clock, viewUserDashboard.VillageId, viewUserDashboard.VillageName)\
					+ "CityId={0}, CityName='{1}' WHERE Id = {2};".format(viewUserDashboard.CityId, viewUserDashboard.CityName, id)
		# print("updateById: ", execute_str)

		self.cursor.execute(execute_str)
		self.cnxn.commit()

		return True
