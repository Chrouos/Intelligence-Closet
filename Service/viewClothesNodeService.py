from Model.DAO.viewClothesNodeDAO import ViewClothesNodeDAO

class ViewClothesNodeService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.viewClothesNodeDAO = ViewClothesNodeDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        
        viewClothesNode_dict = []
        datas = self.viewClothesNodeDAO.queryAll()
        
        for data in datas:
            viewClothesNode_dict.append({  'Id': data.Id, 
                                            'Position': data.Position, 
                                            'ClothesId': data.ClothesId,
                                            'Name': data.Name,
                                            'ClothesType': data.ClothesType,
                                            'ColorId': data.ColorId,
                                            'ColorName': data.ColorName,
                                            'UserPreferences': data.UserPreferences,
                                            'CategoryId': data.CategoryId,
                                            'ClothesStyle': data.ClothesStyle,
                                            'UsageCounter': data.UsageCounter,
                                            'CreateTime': data.CreateTime,
                                            'ModifyTime': data.ModifyTime,
                                            'FilePosition': data.FilePosition,
                                            'Score': data.Score,
                                            'Level': data.Level
                                        })
        
        return viewClothesNode_dict
    
    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.viewClothesNodeDAO.queryById(id)
        
        viewClothesNode_dict ={ 'Id': data.Id, 
                                'Position': data.Position, 
                                'ClothesId': data.ClothesId,
                                'Name': data.Name,
                                'ClothesType': data.ClothesType,
                                'ColorId': data.ColorId,
                                'ColorName': data.ColorName,
                                'UserPreferences': data.UserPreferences,
                                'CategoryId': data.CategoryId,
                                'ClothesStyle': data.ClothesStyle,
                                'UsageCounter': data.UsageCounter,
                                'CreateTime': data.CreateTime,
                                'ModifyTime': data.ModifyTime,
                                'FilePosition': data.FilePosition,
                                'Score': data.Score,
                                'Level': data.Level
                            }
        return viewClothesNode_dict
    
    def queryPositionExitNode(self):
        datas = self.viewClothesNodeDAO.queryPositionExitNode()
        
        viewClothesNode_dict = []
        for data in datas:
            viewClothesNode_dict.append({  'Id': data.Id, 
                                            'Position': data.Position, 
                                            'ClothesId': data.ClothesId,
                                            'Name': data.Name,
                                            'ClothesType': data.ClothesType,
                                            'ColorId': data.ColorId,
                                            'ColorName': data.ColorName,
                                            'UserPreferences': data.UserPreferences,
                                            'CategoryId': data.CategoryId,
                                            'ClothesStyle': data.ClothesStyle,
                                            'UsageCounter': data.UsageCounter,
                                            'CreateTime': data.CreateTime,
                                            'ModifyTime': data.ModifyTime,
                                            'FilePosition': data.FilePosition,
                                            'Score': data.Score,
                                            'Level': data.Level
                                        })
        
        return viewClothesNode_dict