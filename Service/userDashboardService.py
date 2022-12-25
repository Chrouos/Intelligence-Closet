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
                                        'Clock': data.Clock,
                                        'ModifyTime': data.ModifyTime,
                                        'VillageId': data.VillageId,
                                        'LastPosition': data.LastPosition})
        
        return userDashboard_dict
    
    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.userDashboardDAO.queryById(id)
        
        userDashboard_dict = {  'Id': data.Id, 
                                'UserName': data.UserName, 
                                'WeatherLike': data.WeatherLike,  
                                'Clock': data.Clock,
                                'ModifyTime': data.ModifyTime,
                                'VillageId': data.VillageId,
                                'LastPosition': data.LastPosition}
        return userDashboard_dict

    def updateById(self, request, id):
        # try:
            userDashboard = UserDashboard()
            if type(request) is dict:
                userDashboard.updateByDict(request)
            
            if type(request) is str:
                userDashboard_dic = json.loads(request)
                userDashboard.updateByDict(userDashboard_dic)
            
            self.userDashboardDAO.updateById(userDashboard, id)
            return True
        # except Exception as e:
        #     print(e)
        #     return False
    
    
    def create(self, jso):
        userDashboard_dic = json.loads(jso)
        userDashboard = UserDashboard()
        userDashboard.updateByDict(userDashboard_dic)
        return self.stationDAO.create(userDashboard)