from Model.DAO.clothesNodeUpperDAO import ClothesNodeUpperDAO
import json


class ClothesNodeUpperService:

    # 建構子: 呼叫SQL
    def __init__(self):
        self.clothesNodeUpperDAO = ClothesNodeUpperDAO()

    ###################### READ ######################

    # 搜尋全部資料: 轉換成字典

    def queryAll(self):
        datas = self.clothesNodeUpperDAO.queryAll()

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
        data = self.clothesNodeUpperDAO.queryById(id)

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
        data = self.clothesNodeUpperDAO.queryNodeByPosition(position)

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

    # def lastId(self):
    #     return self.clothesNodeUpperDAO.lastId()

    ###################### CREATE ######################

    def create(self, jso):

        clothesNode_dict = json.loads(jso)
        result = self.clothesNodeUpperDAO.create(clothesNode_dict)  # 新增

        return result

    ###################### UPDATE ######################
    def updatePositionToNull(self, position):
        self.clothesNodeUpperDAO.updatePositionToNull(position)
        return True

    ###################### DELETE ######################
    def deleteByPosition(self, position):
        self.clothesNodeUpperDAO.deleteByPosition(position)
        return True