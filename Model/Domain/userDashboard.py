

from asyncio.windows_events import NULL
from datetime import datetime

class UserDashboard:
    
    def __init__(self):
        self.Id = -1
        self.UserName = ""
        self.WeatherLike = ""
        self.StationName = ""
        self.Clock = ""
        self.ModifyTime = ""
        self.CityId = ""
        
    def print(self):
        print("Id: {0}, UserName: {1}, WeatherLike: {2}".format(self.Id, self.UserName, self.WeatherLike))
        print("StationName: {0}, Clock: {1}, ModifyTime: {2}".format(self.StationName, self.Clock, self.ModifyTime))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.UserName = data.UserName
        self.WeatherLike = data.WeatherLike
        self.StationName = data.StationName
        self.CityId = data.CityId
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
            
        if data.get("StationName") != None: 
            self.StationName = data['StationName']
            
        if data.get("CityId") != None: 
            self.CityId = data['CityId']

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
            if data.get("Clock") != None: 
                self.ModifyTime = datetime.strptime(data['ModifyTime'], "%m/%d/%Y")
            
        