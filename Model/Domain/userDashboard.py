



class UserDashboard:
    
    def __init__(self):
        self.Id = -1
        self.UserName = ""
        self.WeatherLike = ""
        self.StationName = ""
        self.Clock = ""
        self.ModifyTime = ""
        
    def print(self):
        print("Id: {0}, UserName: {1}, WeatherLike: {2}".format(self.Id, self.UserName, self.WeatherLike))
        print("StationName: {0}, Clock: {1}, ModifyTime: {2}".format(self.StationName, self.Clock, self.ModifyTime))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.UserName = data.UserName
        self.WeatherLike = data.WeatherLike
        self.StationName = data.StationName
        self.Clock = data.Clock.strftime("%H/%M")
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

        if data.get("Clock") != None: 
            self.Clock = data['Clock'].strftime("%H/%M")
            
        if data.get("ModifyTime") != None: 
            self.ModifyTime = data['ModifyTime'].strftime("%m/%d/%Y")
        