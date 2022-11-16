

class ViewVillage:
    
    def __init__(self):
        self.Id = -1
        self.CityId = ""
        self.CityName = ""
        self.VillageName = ""
        self.DayAPIId = ""
        self.WeekAPIId = ""
        
    def print(self):
        print("Id: {0}, CityId: {1}, CityName: {2}, VillageName: {3}".format(self.Id, self.CityId, self.CityName, self.VillageName))
        print("DayAPIId: {0}, WeekAPIId: {1}".format(self.DayAPIId, self.WeekAPIId))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.CityId = data.CityId
        self.CityName = data.CityName
        self.VillageName = data.VillageName
        self.DayAPIId = data.DayAPIId
        self.WeekAPIId = data.WeekAPIId
        
    def updateByDict(self, data):
        if data.get("Id") != None: 
            self.Id = data['Id']
            
        if data.get("CityId") != None:    
            self.CityId = data['CityId']
            
        if data.get("CityName") != None:    
            self.CityName = data['CityName']
            
        if data.get("VillageName") != None:    
            self.VillageName = data['VillageName']
        
        if data.get("DayAPIId") != None:    
            self.DayAPIId = data['DayAPIId']
            
        if data.get("WeekAPIId") != None:    
            self.WeekAPIId = data['WeekAPIId']