



class ViewClothesNode:
    
    def __init__(self):
        self.Id = -1
        self.Position = ""
        self.ClothesId = ""
        self.Name = ""
        self.ClothesType = ""
        self.ColorId = ""
        self.ColorName = ""
        self.UserPreferences = ""
        self.CategoryId = ""
        self.ClothesStyle = ""
        self.UsageCounter = ""
        self.CreateTime = ""
        self.ModifyTime = ""
        self.FilePosition = ""
        self.Score = ""
        self.Level = ""
        self.IsFavorite = ""

        
    def print(self):
        print("Id: {0}, Position: {1}, ClothesId: {2}".format(self.Id, self.Position, self.ClothesId))
        print("Name: {0}, ClothesType: {1}, ColorId: {2}, ColorName: {3}".format(self.Name, self.ClothesType, self.ColorId, self.ColorName))
        print("UserPreferences:{0}, CategoryId:{1}, ClothesStyle: {2}, UsageCounter:{3}, CreateTime: {4}, ModifyTime: {5}").format(self.UserPreferences,  self.CategoryId,  self.ClothesStyle,  self.UsageCounter,  self.CreateTime,  self.ModifyTime,)
        print("FilePosition: {0},  Score:{1}, Level:{2}".format(self.FilePosition, self.Score, self.Level))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.Position = data.Position
        self.ClothesId = data.ClothesId
        self.Name = data.Name
        self.ClothesType = data.ClothesType
        self.ColorId = data.ColorId
        self.ColorName = data.ColorName
        self.UserPreferences = data.UserPreferences
        self.CategoryId = data.CategoryId
        self.ClothesStyle = data.ClothesStyle
        self.UsageCounter = data.UsageCounter
        self.CreateTime = data.CreateTime
        self.ModifyTime = data.ModifyTime
        self.FilePosition = data.FilePosition
        self.Score = data.Score
        self.Level = data.Level
        self.IsFavorite = data.IsFavorite
        
    def updateByDict(self, data):
        if data.get("Id") != None: 
            self.Id = data['Id']
            
        if data.get("Position") != None: 
            self.Position = data['Position']
            
        if data.get("ClothesId") != None: 
            self.ClothesId = data['ClothesId']     
            
        if data.get("Name") != None: 
            self.Name = data['Name']
            
        if data.get("ClothesType") != None: 
            self.ClothesType = data['ClothesType']        
            
        if data.get("ClothesType") != None: 
            self.ClothesType = data['ClothesType']

        if data.get("ColorName") != None: 
            self.ColorName = data['ColorName']
            
        if data.get("UserPreferences") != None: 
            self.UserPreferences = data['UserPreferences']
            
        if data.get("UserPreferences") != None: 
            self.UserPreferences = data['UserPreferences']
            
        if data.get("ClothesStyle") != None: 
            self.ClothesStyle = data['ClothesStyle']  
        
        if data.get("UsageCounter") != None: 
            self.UsageCounter = data['UsageCounter']
            
        if data.get("CreateTime") != None: 
            self.CreateTime = data['CreateTime']
        
        if data.get("ModifyTime") != None: 
            self.ModifyTime = data['ModifyTime']
            
        if data.get("FilePosition") != None: 
            self.FilePosition = data['FilePosition']
            
        if data.get("Score") != None: 
            self.Score = data['Score']
            
        if data.get("Level") != None: 
            self.Level = data['Level']
            
        if data.get("IsFavorite") != None:
            self.IsFavorite = data['IsFavorite']        
        