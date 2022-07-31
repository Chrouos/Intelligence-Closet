

class Station:
    
    def __init__(self):
        self.Id = -1
        self.StationNumber = ""
        self.StationName = ""
        self.CityId = ""
        self.Address = ""
        self.Remark = ""
        self.CreateTime = ""
        self.ModifyTime = ""
        self.Work = ""
        
    def print(self):
        print("Id: {0}, StationNumber: {1}, StationName: {2}, CityId: {3}".format(self.Id, self.StationNumber, self.StationName, self.CityId))
        print("Address: {0}, Remark: {1}, CreateTime: {2}, ModifyTime: {3}, Work:{4}".format(self.Address, self.Remark, self.CreateTime, self.ModifyTime, self.Work))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.StationNumber = data.StationNumber
        self.StationName = data.StationName
        self.CityId = data.CityId
        self.Address = data.Address
        self.Remark = data.Remark
        self.CreateTime = data.CreateTime.strftime("%m/%d/%Y")
        self.ModifyTime = data.ModifyTime.strftime("%m/%d/%Y")
        self.Work = data.Work
        
    def updateByDict(self, data):
        if data.get("Id") != None: 
            self.Id = data['Id']
            
        if data.get("StationNumber") != None:     
            self.StationNumber = data['StationNumber']
            
        if data.get("StationName") != None:        
            self.StationName = data['StationName']
            
        if data.get("CityId") != None:    
            self.CityId = data['CityId']
            
        if data.get("Address") != None:    
            self.Address = data['Address']
            
        if data.get("Remark") != None:    
            self.Remark = data['Remark']
            
        if data.get("CreateTime") != None:    
            self.CreateTime = data['CreateTime'].strftime("%m/%d/%Y")
            
        if data.get("ModifyTime") != None:    
            self.ModifyTime = data['ModifyTime'].strftime("%m/%d/%Y")
            
        if data.get("Work") != None:    
            self.Work = data['Work']
        