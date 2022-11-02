import imp
import json

from Model.DAO.viewVillageDAO import ViewVillageDAO
from Model.Domain.viewVillage import ViewVillage

class ViewVillageService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.viewViewVillageDAO = ViewVillageDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        datas = self.viewViewVillageDAO.queryAll()
        
        viewViewVillage_dict = []
        for data in datas:
            viewViewVillage_dict.append(   {'Id': data.Id, 
                                            'CityId':data.CityId, 
                                            'CityName': data.CityName,
                                            'VillageName': data.VillageName}
                            )
        
        return viewViewVillage_dict
    
    # viewViewVillage: 轉換成字典
    def queryByCityId(self, id):
        datas = self.viewViewVillageDAO.queryByCityId(id)
        
        viewViewVillage_dict = []
        for data in datas:
            viewViewVillage_dict.append(  { 'Id': data.Id, 
                                            'CityId':data.CityId, 
                                            'CityName': data.CityName,
                                            'VillageName': data.VillageName}
                            )
        
        return viewViewVillage_dict
    