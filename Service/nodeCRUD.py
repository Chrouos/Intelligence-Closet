import pyodbc
import pandas as pd

# 個人的帳號密碼 sql server, 請不要更動crudAccount.py (輸入自己的即可)
from Service.crudAccount import exportSQLLink
import sys, os
sys.path.append(os.getcwd()) # 抓取路徑

global_dict = exportSQLLink()


class nodeCRUD:

    def __init__(self):
        try:
            database = 'intelligence_closet'
            server = global_dict['server']
            username = global_dict['username']
            password = global_dict['password']
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server
                                  + ';DATABASE=' + database
                                  + ';UID=' + username
                                  + ';PWD=' + password)
            self.cursor = cnxn.cursor()
            print('操作成功')
        except:
            print('操作錯誤')

        self.cnxn = cnxn
        self.cursor = cnxn.cursor()

    def reconnect(self):
        self.cursor = self.cnxn.cursor()

    ######################################## CREATE START ########################################

    # insert 必要的
    ### 此為 目前 未有的資料: 使用次數為0
    def insertData(self, colorId, weatherScoreId, filePostion):

        position = self.vacancyPosition()
        print("空缺位置為:", position)
        if position == -1:
            print("位置已滿")
            return
        
        execute_str = "INSERT  INTO clothes_information (Position, ColorId, WeatherScoreId, UsageCounter, CreateTime, ModifyTime , FilePosition) " \
                    + "VALUES ({0}, {1}, {2}, 0, GETDATE(), GETDATE(), '{3}' )".format(position, colorId, weatherScoreId, filePostion)

        print(execute_str)

        self.cnxn.cursor().execute(execute_str)
        self.cnxn.commit()

        return position

    ######################################## CREATE END ########################################

    # !# READ
    # 搜尋 全部的資料
    def queryData(self):
        execute_str = "SELECT * FROM clothes_information"
        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()
        return datas

    # 搜尋 全部的資料
    def queryIdCount(self):
        execute_str = "select count(*) from v_clothes_information"
        self.cursor.execute(execute_str)
        datas = self.cursor.fetchone()[0]
        return datas

    # 搜尋 View全部的資料
    def queryViewData(self):
        execute_str = "SELECT * FROM v_clothes_information"
        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()
        return datas

    # 透過位置找尋資料
    def queryDataByPosition(self, position):
        execute_str = "SELECT * FROM v_clothes_information WHERE Position='" + str(position) + "'"
        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()
        return datas

    # 透過分類找尋資料
    def queryDataByCategory(self, category):
        execute_str = "SELECT * FROM v_clothes_information WHERE CategoryId = '" + str(category) + "'"
        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()
        return datas

    # 大到小分類: name 想找尋的分類
    def sortNameDESC(self, name):
        self.cursor.execute("SELECT * FROM v_clothes_information ORDER BY "
                            + str(name) + " DESC")
        datas = self.cursor.fetchall()
        return datas

    # 小到大分類: name 想找尋的分類
    def sortNameASC(self, name):
        self.cursor.execute("SELECT * FROM v_clothes_information ORDER BY "
                            + name + " ASC")
        datas = self.cursor.fetchall()
        return datas

    # 空缺的位置資訊(範圍 0~9 )
    def vacancyPosition(self):
        for i in range(10):
            if self.queryDataByPosition(i) == []:
                return i

        return -1

    # 最後一個位置
    def lastPosition(self):
        return self.sortNameDESC('Position')[0][1]

    # 查詢存在的Position
    def exitPosition(self):
        execute_str = "SELECT * FROM v_clothes_information"
        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()
        # reData = [row[1] for row in datas]
        reData = []
        for row in datas:
            if row[1] != None:
                reData.append(row[1])

        return reData

    # !# Update

    def updatePositionToNull(self, position):

        if self.queryDataByPosition(position) == []:
            print('沒有此衣物')
            return

        execute_str = "UPDATE clothes_information SET Position = NULL WHERE Position = " + str(position)
        print(execute_str)
        self.cursor.execute(execute_str)
        self.cnxn.commit()

    # !# DELETE
    def deleteByPosition(self, position):

        if self.queryDataByPosition(position) == []:
            print('沒有此衣物')
            return

        execute_str = "DELETE FROM clothes_information WHERE position = " + str(position)
        self.cursor.execute(execute_str)
        self.cnxn.commit()
