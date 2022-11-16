class ViewClothesGraph:

    def __init__(self):
        self.Id = -1
        self.UpperClothesId = ""
        self.UpperPosition = ""
        self.UpperSubCategory = ""
        self.UpperColorId = ""
        self.UpperUserPreferences = ""
        self.UpperFilePosition = ""

        self.LowerClothesId = ""
        self.LowerPosition = ""
        self.LowerSubCategory = ""
        self.LowerColorId = ""
        self.LowerUserPreferences = ""
        self.LowerFilePosition = ""

        self.OtherClothesId = ""
        self.OtherPosition = ""
        self.OtherSubCategory = ""
        self.OtherColorId = ""
        self.OtherUserPreferences = ""
        self.OtherFilePosition = ""

        self.TotalPreferences = 0
        self.ColorScore = 0
        self.UserLike = 0
        self.TotalScore = 0

    def print(self):
        print("ViewClothesGraph: ")

    def updateBySQL(self, data):
        self.Id = data.Id
        self.UpperClothesId = data.UpperClothesId
        self.UpperPosition = data.UpperPosition
        self.UpperSubCategory = data.UpperSubCategory
        self.UpperColorId = data.UpperColorId
        self.UpperUserPreferences = data.UpperUserPreferences
        self.UpperFilePosition = data.UpperFilePosition

        self.LowerClothesId = data.LowerClothesId
        self.LowerPosition = data.LowerPosition
        self.LowerSubCategory = data.LowerSubCategory
        self.LowerColorId = data.LowerColorId
        self.LowerUserPreferences = data.LowerUserPreferences
        self.LowerFilePosition = data.LowerFilePosition

        self.OtherClothesId = data.OtherClothesId
        self.OtherPosition = data.OtherPosition
        self.OtherSubCategory = data.OtherSubCategory
        self.OtherColorId = data.OtherColorId
        self.OtherUserPreferences = data.OtherUserPreferences
        self.OtherFilePosition = data.OtherFilePosition

        self.TotalPreferences = data.TotalPreferences
        self.ColorScore = data.ColorScore
        self.UserLike = data.UserLike
        
        self.TotalScore = data.TotalScore

    def updateByDict(self, data):
        if data.get("Id") != None:
            self.Id = data['Id']

        if data.get("Id") != None:
            self.Id = data.Id
        if data.get("UpperClothesId") != None:
            self.UpperClothesId = data.UpperClothesId
        if data.get("UpperPosition") != None:
            self.UpperPosition = data.UpperPosition
        if data.get("UpperSubCategory") != None:
            self.UpperSubCategory = data.UpperSubCategory
        if data.get("UpperColorId") != None:
            self.UpperColorId = data.UpperColorId
        if data.get("UpperUserPreferences") != None:
            self.UpperUserPreferences = data.UpperUserPreferences
        if data.get("UpperFilePosition") != None:
            self.UpperFilePosition = data.UpperFilePosition

        if data.get("LowerClothesId") != None:
            self.LowerClothesId = data.LowerClothesId
        if data.get("LowerPosition") != None:
            self.LowerPosition = data.LowerPosition
        if data.get("LowerSubCategory") != None:
            self.LowerSubCategory = data.LowerSubCategory
        if data.get("LowerColorId") != None:
            self.LowerColorId = data.LowerColorId
        if data.get("LowerUserPreferences") != None:
            self.LowerUserPreferences = data.LowerUserPreferences
        if data.get("LowerFilePosition") != None:
            self.LowerFilePosition = data.LowerFilePosition

        if data.get("OtherClothesId") != None:
            self.OtherClothesId = data.OtherClothesId
        if data.get("OtherPosition") != None:
            self.OtherPosition = data.OtherPosition
        if data.get("OtherSubCategory") != None:
            self.OtherSubCategory = data.OtherSubCategory
        if data.get("OtherColorId") != None:
            self.OtherColorId = data.OtherColorId
        if data.get("OtherUserPreferences") != None:
            self.OtherUserPreferences = data.OtherUserPreferences
        if data.get("OtherFilePosition") != None:
            self.OtherFilePosition = data.OtherFilePosition

        if data.get("TotalPreferences") != None:
            self.TotalPreferences = data.TotalPreferences
        if data.get("UserLike") != None:
            self.UserLike = data.UserLike

        if data.get("ColorScore") != None:
            self.ColorScore = data.ColorScore
        
        if data.get("TotalScore") != None:
            self.TotalScore = data.TotalScore