

class ColorGraph:
    
    def __init__(self):
        self.Id = -1
        self.ColorId1 = ""
        self.ColorId2 = ""
        self.ColorScore = ""
        
    def print(self):
        print("Id: {0}, ColorId1: {1}, ColorId2: {2}, ColorScore: {3}".format(self.Id, self.ColorId1, self.ColorId2, self.ColorScore))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.ColorId1 = data.ColorId1
        self.ColorId2 = data.ColorId2
        self.ColorScore = data.ColorScore
        
        
    def updateByDict(self, data):
        self.Id = data['Id']
        self.ColorId1 = data['ColorId1']
        self.ColorId2 = data['ColorId2']
        self.ColorScore = data['ColorScore']