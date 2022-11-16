import imp
import json

from Model.DAO.viewVillageDAO import ViewVillageDAO
from Model.Domain.viewVillage import ViewVillage

class ViewVillageService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.viewVillageDAO = ViewVillageDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        datas = self.viewVillageDAO.queryAll()
        
        viewVillage_dict = []
        for data in datas:
            viewVillage_dict.append(   {'Id': data.Id, 
                                            'CityId':data.CityId, 
                                            'CityName': data.CityName,
                                            'VillageName': data.VillageName,
                                            'DayAPIId': data.DayAPIId,
                                            'WeekAPIId': data.WeekAPIId}
                            )
        
        return viewVillage_dict
    
    # viewViewVillage: 轉換成字典
    def queryByCityId(self, id):
        datas = self.viewVillageDAO.queryByCityId(id)
        
        viewVillage_dict = []
        for data in datas:
            viewVillage_dict.append(  { 'Id': data.Id, 
                                            'CityId':data.CityId, 
                                            'CityName': data.CityName,
                                            'VillageName': data.VillageName,
                                            'DayAPIId': data.DayAPIId,
                                            'WeekAPIId': data.WeekAPIId}
                            )
        
        return viewVillage_dict

    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.viewVillageDAO.queryById(id)
        

        viewVillage_dict = { 'Id': data.Id, 
                            'CityId':data.CityId, 
                            'CityName': data.CityName,
                            'VillageName': data.VillageName,
                            'DayAPIId': data.DayAPIId,
                            'WeekAPIId': data.WeekAPIId
                            }
        
        return viewVillage_dict
    