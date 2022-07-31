from Model.DAO.userCombsDAO import UserCombsDAO
from Model.Domain.userCombs import UserCombs

import json

class UserCombsService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.userCombsDAO = UserCombsDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        datas = self.userCombsDAO.queryAll()
        
        userCombs_dict = []
        for data in datas:
            userCombs_dict.append({ 'Id': data.Id, 
                                    'Clothes1Id': data.Clothes1Id, 
                                    'Clothes2Id': data.Clothes2Id, 
                                    'CombLike': data.CombLike, 
                                    'CreateTime': data.CreateTime,
                                    'ModifyTime': data.ModifyTime})
        
        return userCombs_dict
    
    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.userCombsDAO.queryById(id)
        
        userCombs_dict = {  'Id': data.Id, 
                            'Clothes1Id': data.Clothes1Id, 
                            'Clothes2Id': data.Clothes2Id, 
                            'CombLike': data.CombLike, 
                            'CreateTime': data.CreateTime,
                            'ModifyTime': data.ModifyTime}
        return userCombs_dict
    
    def queryByClothes1Id(self, id):
        datas = self.userCombsDAO.queryByClothes1Id(id)
        
        userCombs_dict = []
        for data in datas:
            userCombs_dict.append({ 'Id': data.Id, 
                                    'Clothes1Id': data.Clothes1Id, 
                                    'Clothes2Id': data.Clothes2Id, 
                                    'CombLike': data.CombLike, 
                                    'CreateTime': data.CreateTime,
                                    'ModifyTime': data.ModifyTime})
        return userCombs_dict
    
    def queryByClothes2Id(self, id):
        datas = self.userCombsDAO.queryByClothes2Id(id)
        
        userCombs_dict = []
        for data in datas:
            userCombs_dict.append({ 'Id': data.Id, 
                                    'Clothes1Id': data.Clothes1Id, 
                                    'Clothes2Id': data.Clothes2Id, 
                                    'CombLike': data.CombLike, 
                                    'CreateTime': data.CreateTime,
                                    'ModifyTime': data.ModifyTime})
        return userCombs_dict
    
    
    def updateCombLikeById(self, combLike, id):
        self.userCombsDAO.updateCombLikeById(combLike, id)
        return True
    
    
    def create(self, jso):
        userCombs_dic = json.loads(jso)
        userCombs = UserCombs()
        userCombs.updateByDict(userCombs_dic)
        return self.stationDAO.create(userCombs)