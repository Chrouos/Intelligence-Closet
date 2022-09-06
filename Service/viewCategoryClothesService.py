from Model.DAO.viewCategoryClothesDAO import ViewCategoryClothesDAO

class ViewCategoryClothesService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.viewCategoryClothesDAO = ViewCategoryClothesDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        
        viewCategoryClothes_dict = []
        datas = self.viewCategoryClothesDAO.queryAll()
        
        for data in datas:
            viewCategoryClothes_dict.append({   'Id': data.Id, 
                                                'CategoryId': data.CategoryId, 
                                                'CategoryName': data.CategoryName,
                                                'ClothesType': data.ClothesType,
                                                'Score': data.Score,
                                                'Name': data.Name,
                                                'Level': data.Level,
                                            })
        
        return viewCategoryClothes_dict
    
    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.viewCategoryClothesDAO.queryById(id)
        
        viewCategoryClothes_dict = {   'Id': data.Id, 
                                        'CategoryId': data.CategoryId, 
                                        'CategoryName': data.CategoryName,
                                        'ClothesType': data.ClothesType,
                                        'Score': data.Score,
                                        'Name': data.Name,
                                        'Level': data.Level,
                                    }
        return viewCategoryClothes_dict
    
        # 透過Id查找一筆資料: 轉換成字典
    def queryByCategoryId(self, categoryId):
        datas = self.viewCategoryClothesDAO.queryByCategoryId(categoryId)
        
        viewCategoryClothes_dict = []
        for data in datas:
            viewCategoryClothes_dict.append({   'Id': data.Id, 
                                                'CategoryId': data.CategoryId, 
                                                'CategoryName': data.CategoryName,
                                                'ClothesType': data.ClothesType,
                                                'Score': data.Score,
                                                'Name': data.Name,
                                                'Level': data.Level,
                                            })
        
        return viewCategoryClothes_dict