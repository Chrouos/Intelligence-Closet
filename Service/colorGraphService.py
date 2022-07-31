from Model.DAO.colorGraphDAO import ColorGraphDAO

class ColorGraphService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.colorGraphDAO = ColorGraphDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        datas = self.colorGraphDAO.queryAll()
        
        colorGraph_dict = []
        for data in datas:
            colorGraph_dict.append({'Id': data.Id, 'ColorId1': data.ColorId1, 'ColorId2': data.ColorId2, 'ColorScore': data.ColorScore})
        
        return colorGraph_dict
    
    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.colorGraphDAO.queryById(id)
        
        colorGraph_dict = {'Id': data.Id, 'ColorId1': data.ColorId1, 'ColorId2': data.ColorId2, 'ColorScore': data.ColorScore}
        return colorGraph_dict
    
    def queryUpperByColorId(self, id):
        datas = self.colorGraphDAO.queryUpperByColorId(id)
        
        colorGraph_dict = []
        for data in datas:
            colorGraph_dict.append({'Id': data.Id, 'ColorId1': data.ColorId1, 'ColorId2': data.ColorId2, 'ColorScore': data.ColorScore})
        
        return colorGraph_dict
    
    def queryLowerByColorId(self, id):
        datas = self.colorGraphDAO.queryLowerByColorId(id)
        
        colorGraph_dict = []
        for data in datas:
            colorGraph_dict.append({'Id': data.Id, 'ColorId1': data.ColorId1, 'ColorId2': data.ColorId2, 'ColorScore': data.ColorScore})
        
        return colorGraph_dict
    
    def updateColorScoreById(self, colorScore, id):
        self.colorGraphDAO.updateColorScoreById(colorScore, id)
        return True