

from asyncio.windows_events import NULL
from datetime import datetime

class UserDashboard:
    
    def __init__(self):
        self.Id = -1
        self.UserName = ""
        self.WeatherLike = ""
        self.VillageId = ""
        self.Clock = ""
        self.ModifyTime = ""
        self.LastPosition = ""
        
    def print(self):
        print("Id: {0}, UserName: {1}, WeatherLike: {2}".format(self.Id, self.UserName, self.WeatherLike))
        print("VillageId: {0}, Clock: {1}, ModifyTime: {2}".format(self.VillageId, self.Clock, self.ModifyTime))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.UserName = data.UserName
        self.WeatherLike = data.WeatherLike
        self.VillageId = data.VillageId
        self.LastPosition = data.LastPosition
        # print("CLOCK: ", data.Clock)
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
            
        if data.get("LastPosition") != None: 
            self.LastPosition = data['LastPosition']

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
            
        