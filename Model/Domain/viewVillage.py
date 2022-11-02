

class ViewVillage:
    
    def __init__(self):
        self.Id = -1
        self.CityId = ""
        self.CityName = ""
        self.VillageName = ""
        
    def print(self):
        print("Id: {0}, CityId: {1}, CityName: {2}, VillageName: {3}".format(self.Id, self.CityId, self.CityName, self.VillageName))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.CityId = data.CityId
        self.CityName = data.CityName
        self.VillageName = data.VillageName
        
    def updateByDict(self, data):
        if data.get("Id") != None: 
            self.Id = data['Id']
            
        if data.get("CityId") != None:    
            self.CityId = data['CityId']
            
        if data.get("CityName") != None:    
            self.CityName = data['CityName']
            
        if data.get("VillageName") != None:    
            self.VillageName = data['VillageName']
        