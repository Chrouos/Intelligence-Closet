from Model.DAO.colorDAO import ColorDAO

class ColorService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.colorDAO = ColorDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        datas = self.colorDAO.queryAll()
        
        color_dict = []
        for data in datas:
            color_dict.append({'Id': data.Id, 'ColorEngName': data.ColorEngName, 'ColorName': data.ColorName})
        
        return color_dict
    
    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.colorDAO.queryById(id)
        
        color_dict = {'Id': data.Id, 'ColorEngName': data.ColorEngName, 'ColorName': data.ColorName}
        return color_dict
    
    def queryIdByEngName(self, colorName):
        ColorId = self.colorDAO.queryIdByEngName(colorName.upper())
        return ColorId