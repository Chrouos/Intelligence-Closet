from Model.DAO.userDashboardDAO import UserDashboardDAO
from Model.Domain.userDashboard import UserDashboard

import json

class UserDashboardService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.userDashboardDAO = UserDashboardDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        datas = self.userDashboardDAO.queryAll()
        
        userDashboard_dict = []
        for data in datas:
            userDashboard_dict.append({ 'Id': data.Id, 
                                        'UserName': data.UserName, 
                                        'WeatherLike': data.WeatherLike, 
                                        'StationName': data.StationName, 
                                        'Clock': data.Clock,
                                        'ModifyTime': data.ModifyTime})
        
        return userDashboard_dict
    
    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.userDashboardDAO.queryById(id)
        
        userDashboard_dict = {  'Id': data.Id, 
                                'UserName': data.UserName, 
                                'WeatherLike': data.WeatherLike, 
                                'StationName': data.StationName, 
                                'Clock': data.Clock,
                                'ModifyTime': data.ModifyTime}
        return userDashboard_dict

    def updateById(self, jso, id):
        userDashboard_dic = json.loads(jso)
        userDashboard = UserDashboard()
        userDashboard.updateByDict(userDashboard_dic)
        
        self.userDashboardDAO.updateStationNameById(userDashboard, id)
        return True
    
    
    def create(self, jso):
        userDashboard_dic = json.loads(jso)
        userDashboard = UserDashboard()
        userDashboard.updateByDict(userDashboard_dic)
        return self.stationDAO.create(userDashboard)