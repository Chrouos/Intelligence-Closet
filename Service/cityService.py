from Model.DAO.cityDAO import CityDAO

class CityService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.cityDAO = CityDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        datas = self.cityDAO.queryAll()
        
        city_dict = []
        for data in datas:
            city_dict.append({'Id': data.Id, 'CityName': data.CityName})
        
        return city_dict
    
    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.cityDAO.queryById(id)
        
        city_dict = {'Id': data.Id, 'CityName': data.CityName}
        return city_dict
    
    def queryByName(self, cityName):
        datas = self.cityDAO.queryByName(cityName)
        
        city_dict = []
        for data in datas:
            city_dict.append({'Id': data.Id, 'CityName': data.CityName})
            
        return city_dict
    
    def create(self, cityName):
        return self.cityDAO.create(cityName)
    
    def deleteAllData(self):
        return self.cityDAO.deleteAllData()