from Model.DAO.viewClothesNodeDAO import ViewClothesNodeDAO
import json


class ViewClothesNodeService:

    # 建構子: 呼叫SQL
    def __init__(self):
        self.viewClothesNodeDAO = ViewClothesNodeDAO()


###################### READ ######################

# 搜尋全部資料: 轉換成字典

    def queryAll(self):
        datas = self.viewClothesNodeDAO.queryAll()

        category_dict = []
        for data in datas:
            category_dict.append({
                'Id': data.Id,
                'Position': data.Position,
                'SubCategoryId': data.SubCategoryId,
                'SubCategoryName': data.SubCategoryName,
                'CategoryId': data.CategoryId,
                'Score': data.Score,
                'CategoryName': data.CategoryName,
                'ColorId': data.ColorId,
                'ColorEngName': data.ColorEngName,
                'ColorName': data.ColorName,
                'UserPreferences': data.UserPreferences,
                'WarmLevel': data.WarmLevel,
                'ClothesStyle': data.ClothesStyle,
                'UsageCounter': data.UsageCounter,
                'CreateTime': data.CreateTime,
                'ModifyTime': data.ModifyTime,
                'FilePosition': data.FilePosition,
                'IsFavorite': data.IsFavorite,
            })

        return category_dict

    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.viewClothesNodeDAO.queryById(id)

        category_dict = {
            'Id': data.Id,
            'Position': data.Position,
            'SubCategoryId': data.SubCategoryId,
            'SubCategoryName': data.SubCategoryName,
            'CategoryId': data.CategoryId,
            'Score': data.Score,
            'CategoryName': data.CategoryName,
            'ColorId': data.ColorId,
            'ColorEngName': data.ColorEngName,
            'ColorName': data.ColorName,
            'UserPreferences': data.UserPreferences,
            'WarmLevel': data.WarmLevel,
            'ClothesStyle': data.ClothesStyle,
            'UsageCounter': data.UsageCounter,
            'CreateTime': data.CreateTime,
            'ModifyTime': data.ModifyTime,
            'FilePosition': data.FilePosition,
            'IsFavorite': data.IsFavorite,
        }

        return category_dict

    def queryByPosition(self, position):
        data = self.viewClothesNodeDAO.queryNodeByPosition(position)

        category_dict = {
            'Id': data.Id,
            'Position': data.Position,
            'SubCategoryId': data.SubCategoryId,
            'SubCategoryName': data.SubCategoryName,
            'CategoryId': data.CategoryId,
            'Score': data.Score,
            'CategoryName': data.CategoryName,
            'ColorId': data.ColorId,
            'ColorEngName': data.ColorEngName,
            'ColorName': data.ColorName,
            'UserPreferences': data.UserPreferences,
            'WarmLevel': data.WarmLevel,
            'ClothesStyle': data.ClothesStyle,
            'UsageCounter': data.UsageCounter,
            'CreateTime': data.CreateTime,
            'ModifyTime': data.ModifyTime,
            'FilePosition': data.FilePosition,
            'IsFavorite': data.IsFavorite,
        }

        return category_dict

    def lastId(self):
        return self.viewClothesNodeDAO.lastId()

    # 搜尋全部資料: 轉換成字典
    def queryBySubCategoryId(self, subCategoryId):

        viewClothesNode_dict = []
        datas = self.viewClothesNodeDAO.queryBySubCategoryId(subCategoryId)

        for data in datas:
            viewClothesNode_dict.append({
                'Id': data.Id,
                'Position': data.Position,
                'SubCategoryId': data.SubCategoryId,
                'SubCategoryName': data.SubCategoryName,
                'CategoryId': data.CategoryId,
                'Score': data.Score,
                'CategoryName': data.CategoryName,
                'ColorId': data.ColorId,
                'ColorEngName': data.ColorEngName,
                'ColorName': data.ColorName,
                'UserPreferences': data.UserPreferences,
                'WarmLevel': data.WarmLevel,
                'ClothesStyle': data.ClothesStyle,
                'UsageCounter': data.UsageCounter,
                'CreateTime': data.CreateTime,
                'ModifyTime': data.ModifyTime,
                'FilePosition': data.FilePosition,
                'IsFavorite': data.IsFavorite,
            })

        return viewClothesNode_dict

        # 搜尋全部資料: 轉換成字典
    def queryUpperAll(self):

        viewClothesNode_dict = []
        datas = self.viewClothesNodeDAO.queryUpperAll()

        for data in datas:
            viewClothesNode_dict.append({
                'Id': data.Id,
                'Position': data.Position,
                'SubCategoryId': data.SubCategoryId,
                'SubCategoryName': data.SubCategoryName,
                'CategoryId': data.CategoryId,
                'Score': data.Score,
                'CategoryName': data.CategoryName,
                'ColorId': data.ColorId,
                'ColorEngName': data.ColorEngName,
                'ColorName': data.ColorName,
                'UserPreferences': data.UserPreferences,
                'WarmLevel': data.WarmLevel,
                'ClothesStyle': data.ClothesStyle,
                'UsageCounter': data.UsageCounter,
                'CreateTime': data.CreateTime,
                'ModifyTime': data.ModifyTime,
                'FilePosition': data.FilePosition,
                'IsFavorite': data.IsFavorite,
            })

        return viewClothesNode_dict

    # 搜尋全部資料: 轉換成字典
    def queryLowerAll(self):

        viewClothesNode_dict = []
        datas = self.viewClothesNodeDAO.queryLowerAll()

        for data in datas:
            viewClothesNode_dict.append({
                'Id': data.Id,
                'Position': data.Position,
                'SubCategoryId': data.SubCategoryId,
                'SubCategoryName': data.SubCategoryName,
                'CategoryId': data.CategoryId,
                'Score': data.Score,
                'CategoryName': data.CategoryName,
                'ColorId': data.ColorId,
                'ColorEngName': data.ColorEngName,
                'ColorName': data.ColorName,
                'UserPreferences': data.UserPreferences,
                'WarmLevel': data.WarmLevel,
                'ClothesStyle': data.ClothesStyle,
                'UsageCounter': data.UsageCounter,
                'CreateTime': data.CreateTime,
                'ModifyTime': data.ModifyTime,
                'FilePosition': data.FilePosition,
                'IsFavorite': data.IsFavorite,
            })

        return viewClothesNode_dict

    # 搜尋全部資料: 轉換成字典
    def queryOtherAll(self):

        viewClothesNode_dict = []
        datas = self.viewClothesNodeDAO.queryOtherAll()

        for data in datas:
            viewClothesNode_dict.append({
                'Id': data.Id,
                'Position': data.Position,
                'SubCategoryId': data.SubCategoryId,
                'SubCategoryName': data.SubCategoryName,
                'CategoryId': data.CategoryId,
                'Score': data.Score,
                'CategoryName': data.CategoryName,
                'ColorId': data.ColorId,
                'ColorEngName': data.ColorEngName,
                'ColorName': data.ColorName,
                'UserPreferences': data.UserPreferences,
                'WarmLevel': data.WarmLevel,
                'ClothesStyle': data.ClothesStyle,
                'UsageCounter': data.UsageCounter,
                'CreateTime': data.CreateTime,
                'ModifyTime': data.ModifyTime,
                'FilePosition': data.FilePosition,
                'IsFavorite': data.IsFavorite,
            })

        return viewClothesNode_dict
    
    # 搜尋全部資料: 轉換成字典
    def queryPositionExitNode(self):

        viewClothesNode_dict = []
        datas = self.viewClothesNodeDAO.queryPositionExitNode()

        for data in datas:
            viewClothesNode_dict.append({
                'Id': data.Id,
                'Position': data.Position,
                'SubCategoryId': data.SubCategoryId,
                'SubCategoryName': data.SubCategoryName,
                'CategoryId': data.CategoryId,
                'Score': data.Score,
                'CategoryName': data.CategoryName,
                'ColorId': data.ColorId,
                'ColorEngName': data.ColorEngName,
                'ColorName': data.ColorName,
                'UserPreferences': data.UserPreferences,
                'WarmLevel': data.WarmLevel,
                'ClothesStyle': data.ClothesStyle,
                'UsageCounter': data.UsageCounter,
                'CreateTime': data.CreateTime,
                'ModifyTime': data.ModifyTime,
                'FilePosition': data.FilePosition,
                'IsFavorite': data.IsFavorite,
            })

        return viewClothesNode_dict

    # 搜尋全部資料: 轉換成字典
    def queryPositionIsNull(self):

        viewClothesNode_dict = []
        datas = self.viewClothesNodeDAO.queryPositionIsNull()

        for data in datas:
            viewClothesNode_dict.append({
                'Id': data.Id,
                'Position': data.Position,
                'SubCategoryId': data.SubCategoryId,
                'SubCategoryName': data.SubCategoryName,
                'CategoryId': data.CategoryId,
                'Score': data.Score,
                'CategoryName': data.CategoryName,
                'ColorId': data.ColorId,
                'ColorEngName': data.ColorEngName,
                'ColorName': data.ColorName,
                'UserPreferences': data.UserPreferences,
                'WarmLevel': data.WarmLevel,
                'ClothesStyle': data.ClothesStyle,
                'UsageCounter': data.UsageCounter,
                'CreateTime': data.CreateTime,
                'ModifyTime': data.ModifyTime,
                'FilePosition': data.FilePosition,
                'IsFavorite': data.IsFavorite,
            })

        return viewClothesNode_dict
