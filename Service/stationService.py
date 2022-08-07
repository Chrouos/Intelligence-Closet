import imp


import json

from Model.DAO.stationDAO import StationDAO
from Model.Domain.station import Station

class StationService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.stationDAO = StationDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        datas = self.stationDAO.queryAll()
        
        station_dict = []
        for data in datas:
            station_dict.append(   {'Id': data.Id, 
                                'StationNumber': data.StationNumber, 
                                'StationName':data.StationName, 
                                'CityId':data.CityId, 
                                'Address': data.Address, 
                                'Remark': data.Remark, 
                                'CreateTime': data.CreateTime, 
                                'ModifyTime': data.ModifyTime, 
                                'Work': data.Work}
                            )
        
        return station_dict
    
    # station: 轉換成字典
    def queryByCityId(self, id):
        datas = self.stationDAO.queryByCityId(id)
        
        station_dict = []
        for data in datas:
            station_dict.append(   {'Id': data.Id, 
                                    'StationNumber': data.StationNumber, 
                                    'StationName':data.StationName, 
                                    'CityId':data.CityId, 
                                    'Address': data.Address, 
                                    'Remark': data.Remark, 
                                    'CreateTime': data.CreateTime, 
                                    'ModifyTime': data.ModifyTime, 
                                    'Work': data.Work}
                            )
        
        return station_dict
    
    def create(self, jso):
        if isinstance(jso, str):
            station_dict = json.loads(jso)
        else:
            station_dict = jso
            
        station = Station()
        station.updateByDict(station_dict)
        return self.stationDAO.create(station)
    
    def deleteAllData(self):
        return self.stationDAO.deleteAllData()
    
    def deleteById(self, id):
        return self.stationDAO.deleteById(id)