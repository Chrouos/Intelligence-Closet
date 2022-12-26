from Model.DAO.clothesNodeDAO import ClothesNodeDAO
from Model.DAO.viewClothesNodeDAO import ViewClothesNodeDAO
from Model.Domain.clothesNode import ClothesNode
import json

from Model.Domain.viewClothesNode import ViewClothesNode
from Service.nodeGraphService import NodeGraphService


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
            category_dict.append({
                'Id': data.Id,
                'Position': data.Position,
                'SubCategoryId': data.SubCategoryId,
                'ColorId': data.ColorId,
                'UserPreferences': data.UserPreferences,
                'WarmLevel': data.WarmLevel,
                'UsageCounter': data.UsageCounter,
                'CreateTime': data.CreateTime,
                'ModifyTime': data.ModifyTime,
                'FilePosition': data.FilePosition,
                'IsFavorite': data.IsFavorite,
            })

        return category_dict

    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.clothesNodeDAO.queryById(id)

        category_dict = {
            'Id': data.Id,
            'Position': data.Position,
            'SubCategoryId': data.SubCategoryId,
            'ColorId': data.ColorId,
            'UserPreferences': data.UserPreferences,
            'WarmLevel': data.WarmLevel,
            'UsageCounter': data.UsageCounter,
            'CreateTime': data.CreateTime,
            'ModifyTime': data.ModifyTime,
            'FilePosition': data.FilePosition,
            'IsFavorite': data.IsFavorite,
        }

        return category_dict

    def queryByPosition(self, position):
        data = self.clothesNodeDAO.queryNodeByPosition(position)

        try:
            category_dict = {
                'Id': data.Id,
                'Position': data.Position,
                'SubCategoryId': data.SubCategoryId,
                'ColorId': data.ColorId,
                'UserPreferences': data.UserPreferences,
                'WarmLevel': data.WarmLevel,
                'UsageCounter': data.UsageCounter,
                'CreateTime': data.CreateTime,
                'ModifyTime': data.ModifyTime,
                'FilePosition': data.FilePosition,
                'IsFavorite': data.IsFavorite,
            }

            return category_dict
        except:
            return None

    # def lastId(self):
    #     return self.clothesNodeDAO.lastId()

    def vacancyPosition(self):
        return self.clothesNodeDAO.vacancyPosition()

    ###################### CREATE ######################

    def create(self, jso):

        clothesNode_dict = json.loads(jso)
        result = self.clothesNodeDAO.create(clothesNode_dict)  # 新增

        return result

    ###################### UPDATE ######################

    def updatePositionToNull(self, position):
        try:
            self.clothesNodeDAO.updatePositionToNull(position)
            return True
        except Exception as e:
            print("updatePositionToNull Fail Beacuse: ", e)
            return False
        
    def updateIdInPosition(self, position, request):
        try:
            clothesNode = ClothesNode()
            if type(request) is dict:
                clothesNode.updateByDict(request)
            
            if type(request) is str:
                clothesNode_dic = json.loads(request)
                clothesNode.updateByDict(clothesNode_dic)
                
            self.clothesNodeDAO.updateIdInPosition(position, clothesNode.Id)
            return True
        except Exception as e:
            print("updateIdInPosition Fail Beacuse: ", e)
            return False

    def updateById(self, request):
        # try:
        clothesNode = ClothesNode()
        if type(request) is dict:
            clothesNode.updateByDict(request)
        
        if type(request) is str:
            clothesNode_dic = json.loads(request)
            clothesNode.updateByDict(clothesNode_dic)
        
        self.clothesNodeDAO.updateById(clothesNode)
        return True
    
    # 修改衣物時若修改了類別
    def ChangeCategory_UpdateTheGraph(self, request):
        viewClothesNode = ViewClothesNode()
        viewClothesNodeDAO = ViewClothesNodeDAO()
        
        if type(request) is dict:
            viewClothesNode.updateByDict(request)
        
        if type(request) is str:
            viewClothesNode_dic = json.loads(request)
            viewClothesNode.updateByDict(viewClothesNode_dic)
        
        
        clothesNode_aft = viewClothesNodeDAO.queryById(viewClothesNode.Id)
        print(clothesNode_aft.CategoryId, viewClothesNode.CategoryId)
        # 如果分類不一樣才要update graph
        if clothesNode_aft.CategoryId != viewClothesNode.CategoryId:     
            self.clothesNodeDAO.ChangeCategory_UpdateTheGraph(clothesNode_aft)
            clothesGraph_create = '{{"ClothesNodeLastId": {0}, "CategoryId": {1}}}'.format(
            clothesNode_aft.Id, clothesNode_aft.CategoryId)
            print("saveClothesGraph_Data:", clothesGraph_create)
            
            nodeGraphService = NodeGraphService()
            nodeGraphService.create(clothesGraph_create)
            
        return True

    # Clothes Node 歸零
    def returnZeroClothesNode(self, clothesNodeId):            
            self.clothesNodeDAO.returnZeroClothesNode(clothesNodeId)
            return True

    ###################### DELETE ######################

    def deleteByPosition(self, position):
        self.clothesNodeDAO.deleteByPosition(position)
        return True

    def deleteById(self, id):
        self.clothesNodeDAO.deleteById(id)
        return True