from Model.DAO.viewColorGraphDAO import ViewColorGraphDAO

class ViewColorGraphService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.viewColorGraphDAO = ViewColorGraphDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        
        viewColorGraph_dict = []
        datas = self.viewColorGraphDAO.queryAll()
        
        for data in datas:
            viewColorGraph_dict.append({    'UpperColorId': data.UpperColorId, 
                                            'LowerColorId': data.LowerColorId, 
                                            'UpperEngName': data.UpperEngName,
                                            'LowerEngName': data.LowerEngName,
                                            'UpperColor': data.UpperColor,
                                            'LowerColor': data.LowerColor,
                                        })
        
        return viewColorGraph_dict
    
    # 透過Id查找一筆資料: 轉換成字典
    def queryByUpperColorId(self, id):
        data = self.viewColorGraphDAO.queryByUpperColorId(id)
        
        viewColorGraph_dict ={  'UpperColorId': data.UpperColorId, 
                                'LowerColorId': data.LowerColorId, 
                                'UpperEngName': data.UpperEngName,
                                'LowerEngName': data.LowerEngName,
                                'UpperColor': data.UpperColor,
                                'LowerColor': data.LowerColor,
                                }
        return viewColorGraph_dict
    
    def queryByLowerColorId(self, id):
        data = self.viewColorGraphDAO.queryByLowerColorId(id)
        
        viewColorGraph_dict ={  'UpperColorId': data.UpperColorId, 
                                'LowerColorId': data.LowerColorId, 
                                'UpperEngName': data.UpperEngName,
                                'LowerEngName': data.LowerEngName,
                                'UpperColor': data.UpperColor,
                                'LowerColor': data.LowerColor,
                                }
        return viewColorGraph_dict