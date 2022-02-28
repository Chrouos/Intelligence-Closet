
from pickle import NONE


class nodeCRUD:

    def __init__(self, cnxn):
        self.cnxn = cnxn
        self.cursor = cnxn.cursor()

    #!# CREATE
    def createtData(self, category, color, weatherScore, type, style):

        if(self.vacancyPosition() == False):
            print("位置已滿")
            return

        self.cnxn.cursor().execute("INSERT	INTO clothes_infomation values(" + str(self.vacancyPosition()) +
                                   ", '" + category + "', '" + color + "', " + weatherScore + ", '" + type + "', " + style + ")")
        self.cnxn.commit()

    #!# READ
    # 搜尋全部的資料
    def queryData(self):
        self.cursor.execute("SELECT * FROM clothes_infomation")
        datas = self.cursor.fetchall()
        return datas

    # 透過位置找尋資料
    def queryDataByPosition(self, position):
        self.cursor.execute("SELECT * FROM clothes_infomation WHERE position='" + str(position) + "'")
        datas = self.cursor.fetchall()
        return datas

    # 透過分類找尋資料
    def queryDataByCategory(self, category):
        self.cursor.execute("SELECT * FROM clothes_infomation WHERE category='" + str(category) + "'")
        datas = self.cursor.fetchall()
        return datas

    # 大到小分類
    def sortNameDESC(self, name):
        self.cursor.execute("SELECT * FROM clothes_infomation ORDER BY " + str(name) + " DESC")
        datas = self.cursor.fetchall()
        return datas

    # 小到大分類
    def sortNameASC(self, name):
        self.cursor.execute("SELECT * FROM clothes_infomation ORDER BY " + name + " ASC")
        datas = self.cursor.fetchall()
        return datas

    # 空缺的位置資訊(範圍1~10)
    def vacancyPosition(self):
        for i in range(10):
            if self.queryDataByPosition(i) == []:
                return i

        return False

     # 最後一個位置
    def lastPosition(self):
        return self.sortNameDESC('position')[0][0]

    #!# Update
    # 輸入位置更改天氣分數
    def updateWeatherScoreByPosition(self, position, weather_score):

        if self.queryDataByPosition(position) == []:
            print('沒有此衣物')
            return

        # ex. UPDATE clothes_infomation SET weather_score = 100 WHERE position = 0
        self.cursor.execute("UPDATE clothes_infomation SET weather_score = " +
                            str(weather_score) + " WHERE position = " + str(position))
        self.cnxn.commit()
        print('successfully updated!')

    #!# DELETE
    def deleteByPosition(self, position):

        if self.queryDataByPosition(position) == []:
            print('沒有此衣物')
            return

        # ex. DELETE FROM clothes_infomation WHERE position=0
        self.cursor.execute("DELETE FROM clothes_infomation WHERE position=" + str(position))
        self.cnxn.commit()
        print('successfully deleted!')
