from Model.DAO.viewClothesNodeDAO import ViewClothesNodeDAO
from Model.DAO.viewClothesNodeDAO import ViewClothesNode

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

    # 用類別搜尋最愛資料: 轉換成字典
    def queryIsFavoriteByCategory(self, category):

        viewClothesNode_dict = []
        datas = self.viewClothesNodeDAO.queryIsFavoriteByCategory(category)

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

    # 搜尋存放最多種類的衣服
    def queryMostSubCategory(self):

        mostSubCategory = {}
        data = self.viewClothesNodeDAO.queryMostSubCategory()

        mostSubCategory['SubCategoryName'] = data.SubCategoryName
        mostSubCategory['SubCategoryCount'] = data.SubCategoryCount

        return mostSubCategory

    # 搜尋存放最多顏色的衣服
    def queryMostColor(self):

        mostColor = {}
        data = self.viewClothesNodeDAO.queryMostColor()

        mostColor['ColorName'] = data.ColorName
        mostColor['ColorCount'] = data.ColorCount

        return mostColor

    # 搜尋最常拿出來的衣服
    def queryMostCounter(self):

        mostCounter = {}
        data = self.viewClothesNodeDAO.queryMostCounter()

        mostCounter['FilePosition'] = data.FilePosition
        mostCounter['UsageCounter'] = data.UsageCounter

        return mostCounter