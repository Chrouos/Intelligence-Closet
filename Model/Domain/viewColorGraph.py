



class ViewColorGraph:
    
    def __init__(self):
        self.UpperColorId = -1
        self.LowerColorId = ""
        self.UpperEngName = ""
        self.LowerEngName = ""
        self.UpperColor = ""
        self.LowerColor = ""

        
    def print(self):
        print("UpperColorId: {0}, LowerColorId: {1}, UpperEngName: {2}".format(self.UpperColorId, self.LowerColorId, self.UpperEngName ))
        print("LowerEngName: {0}, UpperColor: {1}, LowerColor: {2}".format(self.LowerEngName, self.UpperColor, self.LowerColor))
        
        
    def updateBySQL(self, data):
        self.UpperColorId = data.UpperColorId
        self.LowerColorId = data.LowerColorId
        self.UpperEngName  = data.UpperEngName 
        self.LowerEngName = data.LowerEngName
        self.UpperColor = data.UpperColor
        self.LowerColor = data.LowerColor
        
    def updateByDict(self, data):
        if data.get("UpperColorId") != None: 
            self.UpperColorId = data['UpperColorId']
            
        if data.get("LowerColorId") != None: 
            self.LowerColorId = data['LowerColorId']
            
        if data.get("UpperEngName") != None: 
            self.UpperEngName  = data['UpperEngName']     
            
        if data.get("LowerEngName") != None: 
            self.LowerEngName = data['LowerEngName']
            
        if data.get("UpperColor") != None: 
            self.UpperColor = data['UpperColor']        
            
        if data.get("LowerColor") != None: 
            self.LowerColor = data['LowerColor']