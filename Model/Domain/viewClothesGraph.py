



class ViewClothesGraph:
    
    def __init__(self):
        self.ViewId = -1
        self.Clothes1Id = ""
        self.Clothes2Id = ""
        self.Clothes1Position = ""
        self.Clothes2Position = ""
        self.Clothes1CategoryId = ""
        self.Clothes2CategoryId = ""
        self.Clothes1ClothesName = ""
        self.Clothes2ClothesName = ""
        self.Clothes1WS = ""
        self.Clothes2WS = ""
        self.ColorScore = ""
        self.Clothes1Color = ""
        self.Clothes2Color = ""
        self.Clothes1ColorName = ""
        self.Clothes2ColorName = ""
        self.AdaptationScore = ""
        self.Clothes1UserPreferences = ""
        self.Clothes2UserPreferences = ""
        self.TotalPreferences = ""
        
    def print(self):
        print("Id: {0}, Clothes1Position: {1}, Clothes2Position: {2}".format(self.Id, self.Clothes1Position, self.Clothes2Position))
        print("Clothes1CategoryId: {0}, Clothes2CategoryId: {1}, Clothes1ClothesName: {2}, Clothes2ClothesName: {3}".format(self.Clothes1CategoryId, self.Clothes2CategoryId, self.Clothes1ClothesName, self.Clothes2ClothesName))
        print("Clothes1WS:{0}, Clothes2WS:{1}, ColorScore: {2}, Clothes2Color:{3}, Clothes1ColorName: {4}, Clothes2ColorName: {5}").format(self.Clothes1WS,  self.Clothes2WS,  self.ColorScore,  self.Clothes1Color,  self.Clothes2Color,  self.Clothes1ColorName, self.Clothes2ColorName,)
        print("AdaptationScore: {0}, Clothes1UserPreferences:{1}, Clothes2UserPreferences:{2}, TotalPreferences:{3}".format(self.AdaptationScore, self.Clothes1UserPreferences, self.Clothes2UserPreferences, self.TotalPreferences))
        
    def updateBySQL(self, data):
        self.ViewId = data.ViewId
        self.Clothes1Id = data.Clothes1Id
        self.Clothes2Id = data.Clothes2Id
        self.Clothes1Position = data.Clothes1Position
        self.Clothes2Position = data.Clothes2Position
        self.Clothes1CategoryId = data.Clothes1CategoryId
        self.Clothes2CategoryId = data.Clothes2CategoryId
        self.Clothes1ClothesName = data.Clothes1ClothesName
        self.Clothes2ClothesName = data.Clothes2ClothesName
        self.Clothes1WS = data.Clothes1WS
        self.Clothes2WS = data.Clothes2WS
        self.ColorScore = data.ColorScore
        self.Clothes1Color = data.Clothes1Color
        self.Clothes2Color = data.Clothes2Color
        self.Clothes1ColorName = data.Clothes1ColorName
        self.Clothes2ColorName = data.Clothes2ColorName
        self.AdaptationScore = data.AdaptationScore
        self.Clothes1UserPreferences = data.Clothes1UserPreferences
        self.Clothes2UserPreferences = data.Clothes2UserPreferences
        self.TotalPreferences = data.TotalPreferences
        
    def updateByDict(self, data):
        if data.get("Id") != None: 
            self.Id = data['Id']
            
        if data.get("Clothes1Id") != None: 
            self.Clothes1Id = data['Clothes1Id']
            
        if data.get("Clothes2Id") != None: 
            self.Clothes2Id = data['Clothes2Id']     
            
        if data.get("Clothes1Position") != None: 
            self.Clothes1Position = data['Clothes1Position']
            
        if data.get("Clothes2Position") != None: 
            self.Clothes2Position = data['Clothes2Position']        
            
        if data.get("Clothes1CategoryId") != None: 
            self.Clothes1CategoryId = data['Clothes1CategoryId']

        if data.get("Clothes2CategoryId") != None: 
            self.Clothes2CategoryId = data['Clothes2CategoryId']
            
        if data.get("Clothes1ClothesName") != None: 
            self.Clothes1ClothesName = data['Clothes1ClothesName']
            
        if data.get("Clothes2ClothesName") != None: 
            self.Clothes2ClothesName = data['Clothes2ClothesName']
            
        if data.get("Clothes1WS") != None: 
            self.Clothes1WS = data['Clothes1WS']  
        
        if data.get("Clothes2WS") != None: 
            self.Clothes2WS = data['Clothes2WS']
            
        if data.get("ColorScore") != None: 
            self.ColorScore = data['ColorScore']
        
        if data.get("Clothes1Color") != None: 
            self.Clothes1Color = data['Clothes1Color']
            
        if data.get("Clothes2Color") != None: 
            self.Clothes2Color = data['Clothes2Color']
            
        if data.get("Clothes1ColorName") != None: 
            self.Clothes1ColorName = data['Clothes1ColorName']
            
        if data.get("Clothes2ColorName") != None: 
            self.Clothes2ColorName = data['Clothes2ColorName']
            
        if data.get("AdaptationScore") != None: 
            self.AdaptationScore = data['AdaptationScore']
            
        if data.get("Clothes1UserPreferences") != None: 
            self.Clothes1UserPreferences = data['Clothes1UserPreferences']
            
        if data.get("Clothes2UserPreferences") != None: 
            self.Clothes2UserPreferences = data['Clothes2UserPreferences']
            
        if data.get("TotalPreferences") != None: 
            self.TotalPreferences = data['TotalPreferences']
        
        