

from asyncio.windows_events import NULL
from datetime import datetime

class ViewUserDashboard:
    
    def __init__(self):
        self.Id = -1
        self.UserName = ""
        self.WeatherLike = ""
        self.ModifyTime = ""
        self.Clock = ""
        self.VillageId = ""
        self.VillageName = ""
        self.CityId = ""
        self.CityName = ""
        
    def print(self):
        print("Id: {0}, UserName: {1}, WeatherLike: {2}".format(self.Id, self.UserName, self.WeatherLike))
        print("ModifyTime: {0}, Clock: {1}, VillageId: {2}".format(self.ModifyTime, self.Clock, self.VillageId))
        print("VillageName: {0}, CityId: {1}, CityName: {2}".format(self.VillageName, self.CityId, self.CityName))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.UserName = data.UserName
        self.WeatherLike = data.WeatherLike
        self.VillageId = data.VillageId
        self.VillageName = data.VillageName
        self.CityId = data.CityId
        self.CityName = data.CityName
        print("CLOCK: ", data.Clock)
        if data.Clock != None:
            self.Clock = data.Clock.strftime("%H/%M")
        if data.ModifyTime != None:
            self.ModifyTime = data.ModifyTime.strftime("%m/%d/%Y")
        
    def updateByDict(self, data):
        if data.get("Id") != None: 
            self.Id = data['Id']
            
        if data.get("UserName") != None: 
            self.UserName = data['UserName']
            
        if data.get("WeatherLike") != None: 
            self.WeatherLike = data['WeatherLike']        
            
        if data.get("VillageId") != None: 
            self.VillageId = data['VillageId']

        if data.get("VillageName") != None: 
            self.VillageName = data['VillageName']

        if data.get("CityId") != None: 
            self.CityId = data['CityId']

        if data.get("CityName") != None: 
            self.CityName = data['CityName']

        try:
            if data.get("Clock") != None: 
                self.Clock = data['Clock'].strftime("%H/%M")
        except:
            if data.get("Clock") != None: 
                self.Clock = datetime.strptime(data['Clock'], "%H/%M")
                
        try:
            if data.get("ModifyTime") != None: 
                self.ModifyTime = data['ModifyTime'].strftime("%m/%d/%Y")
        except:
            if data.get("ModifyTime") != None: 
                self.ModifyTime = datetime.strptime(data['ModifyTime'], "%m/%d/%Y")
            
        