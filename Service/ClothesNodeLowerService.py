from Model.DAO.clothesNodeLowerDAO import ClothesNodeLowerDAO
import json


class ClothesNodeLowerService:

    # 建構子: 呼叫SQL
    def __init__(self):
        self.clothesNodeLowerDAO = ClothesNodeLowerDAO()

    ###################### READ ######################

    # 搜尋全部資料: 轉換成字典

    def queryAll(self):
        datas = self.clothesNodeLowerDAO.queryAll()

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
        data = self.clothesNodeLowerDAO.queryById(id)

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
        data = self.clothesNodeLowerDAO.queryNodeByPosition(position)

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
    #     return self.clothesNodeLowerDAO.lastId()

    ###################### CREATE ######################

    def create(self, jso):

        clothesNode_dict = json.loads(jso)
        result = self.clothesNodeLowerDAO.create(clothesNode_dict)  # 新增

        return result

    ###################### UPDATE ######################
    def updatePositionToNull(self, position):
        self.clothesNodeLowerDAO.updatePositionToNull(position)
        return True

    ###################### DELETE ######################
    def deleteByPosition(self, position):
        self.clothesNodeLowerDAO.deleteByPosition(position)
        return True