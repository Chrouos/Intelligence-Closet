from datetime import datetime

now = datetime.now()  # current date and time


class ViewClothesNode:

    def __init__(self):
        self.Id = -1
        self.Position = ""
        self.SubCategoryId = ""
        self.SubCategoryName = ""
        self.CategoryId = ""
        self.Score = ""
        self.CategoryName = ""
        self.ColorId = ""
        self.ColorEngName = ""
        self.ColorName = ""
        self.UserPreference = ""
        self.WarmLevel = ""
        self.ClothesStyle = ""
        self.UsageCounter = ""
        self.CreateTime = ""
        self.ModifyTime = ""
        self.FilePosition = ""
        self.IsFavorite = ""

    # def print(self):
    #     print(
    #         "Id: {0}, Position: {1}, SubCategoryId: {2}, ColorId: {3}, IsFavorite: {4}"
    #         .format(self.Id, self.Position, self.SubCategoryId, self.ColorId,
    #                 self.IsFavorite))
    #     print(
    #         "UserPreference: {0}, UsageCounter: {1}, CreateTime: {2}, ModifyTime: {3}, FilePosition:{4}"
    #         .format(self.UserPreference, self.UsageCounter, self.CreateTime,
    #                 self.ModifyTime, self.FilePosition))

    def updateBySQL(self, data):
        self.Id = data.Id
        self.Position = data.Position
        self.SubCategoryId = data.SubCategoryId
        self.SubCategoryName = data.SubCategoryName
        self.CategoryId = data.CategoryId
        self.CategoryName = data.CategoryName
        self.Score = data.Score
        self.ColorId = data.ColorId
        self.ColorEngName = data.ColorEngName
        self.ColorName = data.ColorName
        self.UserPreferences = data.UserPreferences
        self.WarmLevel = data.WarmLevel
        self.ClothesStyle = data.ClothesStyle
        self.UsageCounter = data.UsageCounter
        self.FilePosition = data.FilePosition
        self.IsFavorite = data.IsFavorite
        
        if data.CreateTime != None:
            self.CreateTime = data.CreateTime.strftime("%m/%d/%Y")
        if data.ModifyTime != None:
            self.ModifyTime = data.ModifyTime.strftime("%m/%d/%Y")

    def updateByDict(self, data):
        if data.get("Id") != None:
            self.Id = data['Id']
        if data.get("Position") != None:
            self.Position = data['Position']

        if data.get("SubCategoryId") != None:
            self.SubCategoryId = data['SubCategoryId']
        if data.get("SubCategoryName") != None:
            self.SubCategoryName = data['SubCategoryName']

        if data.get("CategoryId") != None:
            self.CategoryId = data['CategoryId']
        if data.get("CategoryName") != None:
            self.CategoryName = data['CategoryName']

        if data.get("ColorId") != None:
            self.ColorId = data['ColorId']
        if data.get("ColorEngName") != None:
            self.ColorEngName = data['ColorEngName']
        if data.get("ColorName") != None:
            self.ColorName = data['ColorName']

        if data.get("Score") != None:
            self.Score = data['Score']
        if data.get("UserPreference") != None:
            self.UserPreference = data['UserPreference']
        if data.get("WarmLevel") != None:
            self.WarmLevel = data['WarmLevel']
        if data.get("ClothesStyle") != None:
            self.ClothesStyle = data['ClothesStyle']
        if data.get("UsageCounter") != None:
            self.UsageCounter = data['UsageCounter']
            
        try:
            if data.get("CreateTime") != None:
                self.CreateTime = data['CreateTime'].strftime("%m/%d/%Y")
            if data.get("ModifyTime") != None: 
                self.ModifyTime = data['ModifyTime'].strftime("%m/%d/%Y")
        except:
            if data.get("CreateTime") != None:
                self.ModifyTime = datetime.strptime(data['CreateTime'], "%m/%d/%Y")
            if data.get("ModifyTime") != None: 
                self.ModifyTime = datetime.strptime(data['ModifyTime'], "%m/%d/%Y")
            

        if data.get("FilePosition") != None:
            self.FilePosition = data['FilePosition']
        if data.get("IsFavorite") != None:
            self.IsFavorite = data['IsFavorite']
