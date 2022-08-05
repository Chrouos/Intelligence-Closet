from Model.DAO.clothesNodeDAO import ClothesNodeDAO
import json


class ClothesNodeService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.clothesNodeDAO = ClothesNodeDAO()
        
	###################### READ ######################
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        datas = self.clothesNodeDAO.queryAll()
        
        category_dict = []
        for data in datas:
            category_dict.append({  'Id': data.Id, 
                                    'Position': data.Position,
                                    'SubCategoryId': data.SubCategoryId,
                                    'ColorId': data.ColorId,
                                    'UserPreferences': data.UserPreferences,
                                    'UsageCounter': data.UsageCounter,
                                    'CreateTime': data.CreateTime,
                                    'ModifyTime': data.ModifyTime,
                                    'FilePosition': data.FilePosition,
                                    })
        
        return category_dict
    
    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.clothesNodeDAO.queryById(id)
        
        category_dict =     {'Id': data.Id, 
                            'Position': data.Position,
                            'SubCategoryId': data.SubCategoryId,
                            'ColorId': data.ColorId,
                            'UserPreferences': data.UserPreferences,
                            'UsageCounter': data.UsageCounter,
                            'CreateTime': data.CreateTime,
                            'ModifyTime': data.ModifyTime,
                            'FilePosition': data.FilePosition,
                            }
        
        return category_dict
    
    def queryByPosition(self, position):
        data = self.clothesNodeDAO.queryByPosition(position)
        
        category_dict =     {'Id': data.Id, 
                            'Position': data.Position,
                            'SubCategoryId': data.SubCategoryId,
                            'ColorId': data.ColorId,
                            'UserPreferences': data.UserPreferences,
                            'UsageCounter': data.UsageCounter,
                            'CreateTime': data.CreateTime,
                            'ModifyTime': data.ModifyTime,
                            'FilePosition': data.FilePosition,
                            }
        
        return category_dict
    
    def lastId(self):
        return self.clothesNodeDAO.lastId()
    
            
	###################### CREATE ######################
            
    def create(self, jso):
        
        clothesNode_dict = json.loads(jso)
        result = self.clothesNodeDAO.create(clothesNode_dict) # 新增
        
        return result
        
    ###################### UPDATE ######################
    def updatePositionToNull(self, position):
        self.clothesNodeDAO.updatePositionToNull(position)
        return True
    
    ###################### DELETE ######################
    def deleteByPosition(self, position):
        self.clothesNodeDAO.deleteByPosition(position)
        return True