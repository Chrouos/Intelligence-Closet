from datetime import datetime

now = datetime.now()  # current date and time


class ClothesNode:

    def __init__(self):
        self.Id = -1
        self.Position = ""
        self.SubCategoryId = ""
        self.ColorId = ""
        self.UserPreferences = ""
        self.UsageCounter = ""
        self.CreateTime = ""
        self.ModifyTime = ""
        self.FilePosition = ""
        self.IsFavorite = ""
        self.WarmLevel = ""

    def print(self):
        print(
            "Id: {0}, Position: {1}, SubCategoryId: {2}, ColorId: {3}, IsFavorite: {4}"
            .format(self.Id, self.Position, self.SubCategoryId, self.ColorId,
                    self.IsFavorite))
        print(
            "UserPreferences: {0}, UsageCounter: {1}, CreateTime: {2}, ModifyTime: {3}, FilePosition:{4}"
            .format(self.UserPreferences, self.UsageCounter, self.CreateTime,
                    self.ModifyTime, self.FilePosition))

    def updateBySQL(self, data):
        self.Id = data.Id
        self.Position = data.Position
        self.SubCategoryId = data.SubCategoryId
        self.ColorId = data.ColorId
        self.UserPreferences = data.UserPreferences
        self.ClothesStyle = data.ClothesStyle
        self.UsageCounter = data.UsageCounter
        self.IsFavorite = data.IsFavorite
        self.WarmLevel = data.WarmLevel

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
        if data.get("ColorId") != None:
            self.ColorId = data['ColorId']
        if data.get("UserPreferences") != None:
            self.UserPreferences = data['UserPreferences']
        if data.get("ClothesStyle") != None:
            self.ClothesStyle = data['ClothesStyle']
        if data.get("UsageCounter") != None:
            self.UsageCounter = data['UsageCounter']
        if data.get("FilePosition") != None:
            self.FilePosition = data['FilePosition']
        if data.get("WarmLevel") != None:
            self.WarmLevel = data['WarmLevel']
        if data.get("IsFavorite") != None:
            self.IsFavorite = data['IsFavorite']

        try:
            if data.get("ModifyTime") != None: 
                self.ModifyTime = data['ModifyTime'].strftime("%m/%d/%Y")
        except:
            if data.get("ModifyTime") != None: 
                self.ModifyTime = datetime.strptime(data['ModifyTime'], "%m/%d/%Y")
