from Model.DAO.cityDAO import CityDAO

class CityService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.cityDAO = CityDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        datas = self.cityDAO.queryAll()
        
        category_dict = []
        for data in datas:
            category_dict.append({'Id': data.Id, 'CityName': data.CityName})
        
        return category_dict
    
    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.cityDAO.queryById(id)
        
        category_dict = {'Id': data.Id, 'CityName': data.CityName}
        return category_dict
    
    def queryByName(self, cityName):
        datas = self.cityDAO.queryByName(cityName)
        
        category_dict = []
        for data in datas:
            category_dict.append({'Id': data.Id, 'CityName': data.CityName})
            
        return category_dict