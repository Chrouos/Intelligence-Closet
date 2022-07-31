from Model.DAO.viewClothesGraphDAO import ViewClothesGraphDAO

class ViewClothesGraphService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.viewClothesGraphDAO = ViewClothesGraphDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        
        viewClothesGraph_dict = []
        datas = self.viewClothesGraphDAO.queryAll()
        
        for data in datas:
            viewClothesGraph_dict.append({  'Id': data.ViewId, 
                                            'Clothes1Id': data.Clothes1Id, 
                                            'Clothes2Id': data.Clothes2Id,
                                            'Clothes1Position': data.Clothes1Position,
                                            'Clothes2Position': data.Clothes2Position,
                                            'Clothes1CategoryId': data.Clothes1CategoryId,
                                            'Clothes2CategoryId': data.Clothes2CategoryId,
                                            'Clothes1ClothesName': data.Clothes1ClothesName,
                                            'Clothes2ClothesName': data.Clothes2ClothesName,
                                            'Clothes1WS': data.Clothes1WS,
                                            'Clothes2WS': data.Clothes2WS,
                                            'ColorScore': data.ColorScore,
                                            'Clothes1Color': data.Clothes1Color,
                                            'Clothes2Color': data.Clothes2Color,
                                            'Clothes1ColorName': data.Clothes1ColorName,
                                            'Clothes2ColorName': data.Clothes2ColorName,
                                            'AdaptationScore': data.AdaptationScore,
                                            'Clothes1UserPreferences': data.Clothes1UserPreferences,
                                            'Clothes2UserPreferences': data.Clothes2UserPreferences,
                                            'TotalPreferences': data.TotalPreferences,
                                        })
        
        return viewClothesGraph_dict
    
    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.viewClothesGraphDAO.queryById(id)
        
        viewClothesGraph_dict = {   'Id': data.ViewId, 
                                    'Clothes1Id': data.Clothes1Id, 
                                    'Clothes2Id': data.Clothes2Id,
                                    'Clothes1Position': data.Clothes1Position,
                                    'Clothes2Position': data.Clothes2Position,
                                    'Clothes1CategoryId': data.Clothes1CategoryId,
                                    'Clothes2CategoryId': data.Clothes2CategoryId,
                                    'Clothes1ClothesName': data.Clothes1ClothesName,
                                    'Clothes2ClothesName': data.Clothes2ClothesName,
                                    'Clothes1WS': data.Clothes1WS,
                                    'Clothes2WS': data.Clothes2WS,
                                    'ColorScore': data.ColorScore,
                                    'Clothes1Color': data.Clothes1Color,
                                    'Clothes2Color': data.Clothes2Color,
                                    'Clothes1ColorName': data.Clothes1ColorName,
                                    'Clothes2ColorName': data.Clothes2ColorName,
                                    'AdaptationScore': data.AdaptationScore,
                                    'Clothes1UserPreferences': data.Clothes1UserPreferences,
                                    'Clothes2UserPreferences': data.Clothes2UserPreferences,
                                    'TotalPreferences': data.TotalPreferences,
                                }
        return viewClothesGraph_dict