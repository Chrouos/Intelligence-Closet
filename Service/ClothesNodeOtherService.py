from Model.DAO.clothesNodeOtherDAO import ClothesNodeOtherDAO
import json


class ClothesNodeOtherService:

    # 建構子: 呼叫SQL
    def __init__(self):
        self.clothesNodeOtherDAO = ClothesNodeOtherDAO()


###################### READ ######################

# 搜尋全部資料: 轉換成字典

    def queryAll(self):
        datas = self.clothesNodeOtherDAO.queryAll()

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
        data = self.clothesNodeOtherDAO.queryById(id)

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
        data = self.clothesNodeOtherDAO.queryNodeByPosition(position)

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
    #     return self.clothesNodeOtherDAO.lastId()

    ###################### CREATE ######################

    def create(self, jso):

        clothesNode_dict = json.loads(jso)
        result = self.clothesNodeOtherDAO.create(clothesNode_dict)  # 新增

        return result

    ###################### UPDATE ######################
    def updatePositionToNull(self, position):
        self.clothesNodeOtherDAO.updatePositionToNull(position)
        return True

    ###################### DELETE ######################
    def deleteByPosition(self, position):
        self.clothesNodeOtherDAO.deleteByPosition(position)
        return True