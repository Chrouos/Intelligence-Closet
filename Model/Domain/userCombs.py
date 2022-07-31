



class UserCombs:
    
    def __init__(self):
        self.Id = -1
        self.Clothes1Id = ""
        self.Clothes2Id = ""
        self.CombLike = ""
        self.CreateTime = ""
        self.ModifyTime = ""
        
    def print(self):
        print("Id: {0}, Clothes1Id: {1}, Clothes2Id: {2}".format(self.Id, self.Clothes1Id, self.Clothes2Id))
        print("CombLike: {0}, CreateTime: {1}, ModifyTime: {2}".format(self.CombLike, self.CreateTime, self.ModifyTime))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.Clothes1Id = data.Clothes1Id
        self.Clothes2Id = data.Clothes2Id
        self.CombLike = data.CombLike
        self.CreateTime = data.CreateTime.strftime("%m/%d/%Y")
        self.ModifyTime = data.ModifyTime.strftime("%m/%d/%Y")
        
    def updateByDict(self, data):
        if data.get("Id") != None: 
            self.Id = data['Id']
            
        if data.get("Clothes1Id") != None: 
            self.Clothes1Id = data['Clothes1Id']
            
        if data.get("Clothes2Id") != None: 
            self.Clothes2Id = data['Clothes2Id']        
            
        if data.get("CombLike") != None: 
            self.CombLike = data['CombLike']

        if data.get("CreateTime") != None: 
            self.CreateTime = data['CreateTime'].strftime("%m/%d/%Y")
            
        if data.get("ModifyTime") != None: 
            self.ModifyTime = data['ModifyTime'].strftime("%m/%d/%Y")
        