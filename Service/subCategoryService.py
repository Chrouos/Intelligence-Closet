from Model.DAO.subCategoryDAO import SubCategoryDAO

class SubCategoryService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.subCategoryDAO = SubCategoryDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        datas = self.subCategoryDAO.queryAll()
        
        subCategory_dict = []
        for data in datas:
            subCategory_dict.append(  {'Id': data.Id, 
                                'CategoryId': data.CategoryId, 
                                'ClothesType': data.ClothesType, 
                                'Score': data.Score, 
                                'Name': data.Name})
        
        return subCategory_dict
    
    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.subCategoryDAO.queryById(id)
        
        subCategory_dict = {'Id': data.Id, 
                            'CategoryId': data.CategoryId, 
                            'ClothesType': data.ClothesType, 
                            'Score': data.Score, 
                            'Name': data.Name}
        return subCategory_dict
    
    def queryByCategoryId(self, id):
        datas = self.subCategoryDAO.queryByCategoryId(id)
        
        subCategory_dict = []
        for data in datas:
            subCategory_dict.append({   'Id': data.Id, 
                                        'CategoryId': data.CategoryId, 
                                        'ClothesType': data.ClothesType, 
                                        'Score': data.Score, 
                                        'Name': data.Name})
        
        return subCategory_dict
    
    def queryIdByClothesType(self, clothesType):
        data = self.subCategoryDAO.queryByClothesType(clothesType)
        
        return data.Id
    
    def updateScoreById(self, score, id):
        self.subCategoryDAO.updateScoreById(score, id)
        return True
    
    