from Model.DAO.viewUserDashboardDAO import ViewUserDashboardDAO
from Model.Domain.viewUserDashboard import ViewUserDashboard

import json

class ViewUserDashboardService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.viewUserDashboardDAO = ViewUserDashboardDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        datas = self.viewUserDashboardDAO.queryAll()
        
        viewUserDashboard_dict = []
        for data in datas:
            viewUserDashboard_dict.append({ 'Id': data.Id, 
                                        'UserName': data.UserName, 
                                        'WeatherLike': data.WeatherLike, 
                                        'Clock': data.Clock,
                                        'ModifyTime': data.ModifyTime,
                                        'VillageId': data.VillageId,
                                        'VillageName': data.VillageName,
                                        'CityId': data.CityId,
                                        'CityName': data.CityName})
        
        return viewUserDashboard_dict
    
    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.viewUserDashboardDAO.queryById(id)
        
        viewUserDashboard_dict = {  'Id': data.Id, 
                                'UserName': data.UserName, 
                                'WeatherLike': data.WeatherLike, 
                                'Clock': data.Clock,
                                'ModifyTime': data.ModifyTime,
                                'VillageId': data.VillageId,
                                'VillageName': data.VillageName,
                                'CityId': data.CityId,
                                'CityName': data.CityName}
        return viewUserDashboard_dict

    def updateById(self, request, id):
        # try:
            viewUserDashboard = ViewUserDashboard()
            if type(request) is dict:
                viewUserDashboard.updateByDict(request)
            
            if type(request) is str:
                viewUserDashboard_dic = json.loads(request)
                viewUserDashboard = ViewUserDashboard()
                viewUserDashboard.updateByDict(viewUserDashboard_dic)
            
            self.viewUserDashboardDAO.updateById(viewUserDashboard, id)
            return True
        # except Exception as e:
        #     print(e)
        #     return False
    
    
    def create(self, jso):
        viewUserDashboard_dic = json.loads(jso)
        viewUserDashboard = ViewUserDashboard()
        viewUserDashboard.updateByDict(viewUserDashboard_dic)
        return self.stationDAO.create(viewUserDashboard)