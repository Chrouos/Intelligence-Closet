class NodeGraph:

    def __init__(self):
        self.Id = -1
        self.UpperId = ""
        self.LowerId = ""
        self.OtherId = ""
        self.CombLike = ""
        self.CreateTime = ""
        self.ModifyTime = ""
        self.Position = ""

    def print(self):
        print("Id: {0}, UpperId: {1}, LowerId: {2}".format(
            self.Id, self.UpperId, self.LowerId))
        print("CombLike: {0}, CreateTime: {1}, ModifyTime: {2}".format(
            self.CombLike, self.CreateTime, self.ModifyTime))

    def updateBySQL(self, data):
        self.Id = data.Id
        self.UpperId = data.UpperId
        self.LowerId = data.LowerId
        self.OtherId = data.OtherId
        self.UserLike = data.UserLike
        self.Position = data.Position
        self.CreateTime = data.CreateTime.strftime("%m/%d/%Y")
        self.ModifyTime = data.ModifyTime.strftime("%m/%d/%Y")

    def updateByDict(self, data):
        if data.get("Id") != None:
            self.Id = data['Id']

        if data.get("UpperId") != None:
            self.UpperId = data['UpperId']

        if data.get("LowerId") != None:
            self.LowerId = data['LowerId']

        if data.get("OtherId") != None:
            self.OtherId = data['OtherId']

        if data.get("UserLike") != None:
            self.CombLike = data['CombLike']

        if data.get("Position") != None:
            self.CombLike = data['Position']

        if data.get("CreateTime") != None:
            self.CreateTime = data['CreateTime'].strftime("%m/%d/%Y")

        if data.get("ModifyTime") != None:
            self.ModifyTime = data['ModifyTime'].strftime("%m/%d/%Y")
