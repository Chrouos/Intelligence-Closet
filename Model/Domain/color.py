

class Color:
    
    def __init__(self):
        self.Id = -1
        self.ColorEngName = ""
        self.ColorName = ""
        
        
        
    def print(self):
        print("Id: {0}, ColorEngName: {1}, ColorName: {2}".format(self.Id, self.ColorEngName, self.ColorName))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.ColorEngName = data.ColorEngName
        self.ColorName = data.ColorName
        
        
    def updateByDict(self, data):
        self.Id = data['Id']
        self.ColorEngName = data['ColorEngName']
        self.ColorName = data['ColorName']