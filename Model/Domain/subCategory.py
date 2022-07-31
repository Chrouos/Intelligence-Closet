



class SubCategory:
    
    def __init__(self):
        self.Id = -1
        self.CategoryId = ""
        self.ClothesType = ""
        self.Score = ""
        self.Name = ""
        
    def print(self):
        print("Id: {0}, CategoryId: {1}, ClothesType: {2}".format(self.Id, self.CategoryId, self.ClothesType))
        print("Score: {0}, Name: {1}".format(self.Score, self.Name))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.CategoryId = data.CategoryId
        self.ClothesType = data.ClothesType
        self.Score = data.Score
        self.Name = data.Name
        
    def updateByDict(self, data):
        if data.get("Id") != None: 
            self.Id = data['Id']
            
        if data.get("CategoryId") != None: 
            self.CategoryId = data['CategoryId']
            
        if data.get("ClothesType") != None: 
            self.ClothesType = data['ClothesType']        
            
        if data.get("Score") != None: 
            self.Score = data['Score']

        if data.get("Name") != None: 
            self.Name = data['Name']
        