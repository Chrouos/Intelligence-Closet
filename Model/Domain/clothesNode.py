from datetime import datetime

now = datetime.now() # current date and time

class ClothesNode:
    
    def __init__(self):
        self.Id = -1 
        self.Position = ""
        self.SubCategoryId = -1
        self.ColorId = -1
        self.UserPreference = -1
        self.UsageCounter = -1 
        self.CreateTime = ""
        self.ModifyTime = ""
        self.FilePosition = ""
        
    def print(self):
        print("Id: {0}, Position: {1}, SubCategoryId: {2}, ColorId: {3}".format(self.Id, self.Position, self.SubCategoryId, self.ColorId))
        print("UserPreference: {0}, UsageCounter: {1}, CreateTime: {2}, ModifyTime: {3}, FilePosition:{4}".format(self.UserPreference, self.UsageCounter, self.CreateTime, self.ModifyTime, self.FilePosition))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.Position = data.Position
        self.SubCategoryId = data.SubCategoryId
        self.ColorId = data.ColorId
        self.UserPreferences = data.UserPreferences
        self.ClothesStyle = data.ClothesStyle
        self.UsageCounter = data.UsageCounter
        self.CreateTime = data.CreateTime.strftime("%m/%d/%Y")
        self.ModifyTime = data.ModifyTime.strftime("%m/%d/%Y")
        self.FilePosition = data.FilePosition
        
    def updateByDict(self, data):
        self.Id = data['Id']
        self.Position = data['Position']
        self.SubCategoryId = data['SubCategoryId']
        self.ColorId = data['ColorId']
        self.UserPreference = data['UserPreference']
        self.ClothesStyle = data['ClothesStyle']
        self.UsageCounter = data['UsageCounter']
        self.CreateTime = data['CreateTime'].strftime("%m/%d/%Y")
        self.ModifyTime = data['ModifyTime'].strftime("%m/%d/%Y")
        self.FilePosition = data['FilePosition']
        