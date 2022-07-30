

class City:
    
    def __init__(self):
        self.Id = -1
        self.CityName = ""
        
    def print(self):
        print("Id: {0}, CityName: {1}".format(self.Id, self.CityName))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.CityName = data.CityName
        
        
    def updateByDict(self, data):
        self.Id = data['Id']
        self.CityName = data['CityName']
        