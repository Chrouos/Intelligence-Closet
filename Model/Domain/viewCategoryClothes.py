



class ViewCategoryClothes:
    
    def __init__(self):
        self.Id = -1
        self.CategoryId = ""
        self.CategoryName = ""
        self.ClothesType = ""
        self.Score = ""
        self.Name = ""
        self.Level = ""
        
    def print(self):
        print("Id: {0}, CategoryId: {1}, CategoryName: {2}".format(self.Id, self.CategoryId, self.CategoryName))
        print("ClothesType: {0}, Score: {1}, Name: {2}, Level: {3}".format(self.ClothesType, self.Score, self.Name, self.Level))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.CategoryId = data.CategoryId
        self.CategoryName = data.CategoryName
        self.ClothesType = data.ClothesType
        self.Score = data.Score
        self.Name = data.Name
        self.Level = data.Level
        
    def updateByDict(self, data):
        if data.get("Id") != None: 
            self.Id = data['Id']
            
        if data.get("CategoryId") != None: 
            self.CategoryId = data['CategoryId']
            
        if data.get("CategoryName") != None: 
            self.CategoryName = data['CategoryName']        
            
        if data.get("ClothesType") != None: 
            self.ClothesType = data['ClothesType']

        if data.get("Score") != None: 
            self.Score = data['Score']
            
        if data.get("Name") != None: 
            self.Name = data['Name']
            
        if data.get("Level") != None: 
            self.Level = data['Level']
        