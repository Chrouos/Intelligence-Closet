

class Village:
    
    def __init__(self):
        self.Id = -1
        self.CityId = ""
        self.VillageName = ""
        
    def print(self):
        print("Id: {0}, CityId: {1}, VillageName: {2}".format(self.Id, self.CityId, self.VillageName))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.CityId = data.CityId
        self.VillageName = data.VillageName
        
    def updateByDict(self, data):
        if data.get("Id") != None: 
            self.Id = data['Id']
            
        if data.get("CityId") != None:    
            self.CityId = data['CityId']
            
        if data.get("VillageName") != None:    
            self.VillageName = data['VillageName']