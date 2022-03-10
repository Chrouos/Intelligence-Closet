import pyodbc
import pandas as pd


class nodeCRUD:

    def __init__(self):

        try:
            server = 'LAPTOP-BGP802KH\SQLEXPRESS'
            database = 'intelligence_closet'
            username = 'sa'
            password = 'asd464017'
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server
                                  + ';DATABASE=' + database
                                  + ';UID=' + username
                                  + ';PWD=' + password)
            cursor = cnxn.cursor()
            print('操作成功')

        except:
            print('操作錯誤')

        self.cnxn = cnxn
        self.cursor = cnxn.cursor()

    def reconnect(self):
        self.cursor = self.cnxn.cursor()

     #!# CREATE
    def createtData(self, category, color, weatherScore, type, style):

        if(self.vacancyPosition() == False):
            print("位置已滿")
            return

        self.cnxn.cursor().execute("INSERT  INTO clothes_information values(" + str(self.vacancyPosition())
                                   + ", '" + category + "', '" + color + "', " + weatherScore
                                   + ", '" + type + "', " + style + ", 0, GETDATE())")
        self.cnxn.commit()

    #!# READ
    # 搜尋全部的資料
    def queryData(self):
        self.cursor.execute("SELECT * FROM clothes_information")
        datas = self.cursor.fetchall()
        return datas

    # 透過位置找尋資料
    def queryDataByPosition(self, position):
        self.cursor.execute("SELECT * FROM clothes_information WHERE position='"
                            + str(position) + "'")
        datas = self.cursor.fetchall()
        return datas

    def queryDataInNode(self):
        self.cursor.execute(
            "SELECT position,category, color, clothes_type, usageCounter, createTime, filePosition, weather_score FROM clothes_information")
        datas = self.cursor.fetchall()
        return datas

    # 透過分類找尋資料
    def queryDataByCategory(self, category):
        self.cursor.execute("SELECT * FROM clothes_information WHERE category='"
                            + str(category) + "'")
        datas = self.cursor.fetchall()
        return datas

    # 大到小分類
    def sortNameDESC(self, name):
        self.cursor.execute("SELECT * FROM clothes_information ORDER BY "
                            + str(name) + " DESC")
        datas = self.cursor.fetchall()
        return datas

    # 小到大分類
    def sortNameASC(self, name):
        self.cursor.execute("SELECT * FROM clothes_information ORDER BY "
                            + name + " ASC")
        datas = self.cursor.fetchall()
        return datas

    # 空缺的位置資訊(範圍1~10)
    def vacancyPosition(self):
        for i in range(1, 11):
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

        # ex. UPDATE clothes_information SET weather_score = 100 WHERE position = 0
        self.cursor.execute("UPDATE clothes_information SET weather_score = "
                            + str(weather_score) + " WHERE position = " + str(position))
        self.cnxn.commit()
        print('successfully updated!')

    def updatePositionToNull(self, position):

        if self.queryDataByPosition(position) == []:
            print('沒有此衣物')
            return

        # ex. UPDATE clothes_information SET weather_score = 100 WHERE position = 0
        self.cursor.execute("UPDATE clothes_information SET position = NULL  WHERE position = " + str(position))
        self.cnxn.commit()
        print('successfully updated!')

    #!# DELETE
    def deleteByPosition(self, position):

        if self.queryDataByPosition(position) == []:
            print('沒有此衣物')
            return

        # ex. DELETE FROM clothes_information WHERE position=0
        self.cursor.execute("DELETE FROM clothes_information WHERE position="
                            + str(position))
        self.cnxn.commit()
        print('successfully deleted!')
