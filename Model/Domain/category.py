
from asyncio.windows_events import NULL
from pickle import NONE


class Category:
    
    def __init__(self):
        self.Id = -1
        self.CategoryName = ""
        self.Level = ""
        
    def print(self):
        print("Id: {0}, CategoryName: {1}, Level: {2}".format(self.Id, self.CategoryName, self.Level))
        
    def updateBySQL(self, data):
        self.Id = data.Id
        self.CategoryName = data.CategoryName
        self.Level = data.Level
        
    def updateByDict(self, data):
        if data.get("Id") != None: 
            self.Id = data['Id']
        if data.get("CategoryName") != None: 
            self.CategoryName = data['CategoryName']
        if data.get("Level") != None: 
            self.Level = data['Level']
        