

class City:
    
    def __init__(self):
        self.Id = -1
        self.CityName = ""
        
    def print(self):
        print("Id: {0}, CityName: {1}".format(self.Id, self.CityName))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        if data.CityName != None:
            self.CityName = data.CityName
        
        
    def updateByDict(self, data):
        if data.get("Id") != None: 
            self.Id = data['Id']
        if data.get("CityName") != None: 
            self.CityName = data['CityName']
        