import imp
import json

from Model.DAO.viewStationDAO import ViewStationDAO
from Model.Domain.viewStation import ViewStation

class ViewStationService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.viewViewStationDAO = ViewStationDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        datas = self.viewViewStationDAO.queryAll()
        
        viewViewStation_dict = []
        for data in datas:
            viewViewStation_dict.append(   {'Id': data.Id, 
                                            'StationNumber': data.StationNumber, 
                                            'StationName':data.StationName, 
                                            'CityId':data.CityId, 
                                            'CityName': data.CityName,
                                            'Address': data.Address, 
                                            'Remark': data.Remark, 
                                            'CreateTime': data.CreateTime, 
                                            'ModifyTime': data.ModifyTime, 
                                            'Work': data.Work}
                            )
        
        return viewViewStation_dict
    
    # viewViewStation: 轉換成字典
    def queryByCityId(self, id):
        datas = self.viewViewStationDAO.queryByCityId(id)
        
        viewViewStation_dict = []
        for data in datas:
            viewViewStation_dict.append(  { 'Id': data.Id, 
                                            'StationNumber': data.StationNumber, 
                                            'StationName':data.StationName, 
                                            'CityId':data.CityId, 
                                            'CityName': data.CityName,
                                            'Address': data.Address, 
                                            'Remark': data.Remark, 
                                            'CreateTime': data.CreateTime, 
                                            'ModifyTime': data.ModifyTime, 
                                            'Work': data.Work}
                            )
        
        return viewViewStation_dict
    