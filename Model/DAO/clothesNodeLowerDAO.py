# 個人的帳號密碼 sql server, 請不要更動crudAccount.py (輸入自己的即可)
from Model.DAO.crudAccount import ExportSQLLink
from Model.Domain.clothesNodeLower import ClothesNodeLower

import pyodbc
import time


class ClothesNodeLowerDAO:

    # 建構子: 建立資料庫連線
    def __init__(self):

        try:

            global_dict = ExportSQLLink()  # 呼叫帳號密碼

            database = 'intelligence_closet'
            server = global_dict['server']
            username = global_dict['username']
            password = global_dict['password']
            cnxn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server +
                ';DATABASE=' + database + ';UID=' + username + ';PWD=' +
                password)
            self.cursor = cnxn.cursor()
            print('ClothesNodeDAO 操作成功')

        except:
            print('ClothesNodeDAO 操作錯誤')

        self.cnxn = cnxn
        self.cursor = cnxn.cursor()

    ###################### READ ######################

    # 搜尋所有資料: tuple
    def queryAll(self):
        execute_str = "SELECT * FROM intelligence_closet.dbo.clothes_node_lower;"
        print("queryAll: ", execute_str)

        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()

        clothesNodeLowerLists = []
        for data in datas:
            clothesNodeLower = ClothesNodeLower()
            clothesNodeLower.updateBySQL(data)
            clothesNodeLowerLists.append(clothesNodeLower)

        return clothesNodeLowerLists

    # 透過Id查找一筆資料: tuple
    def queryById(self, id):
        execute_str = "SELECT * FROM intelligence_closet.dbo.clothes_node_lower WHERE Id = {0}".format(
            id)
        print("queryById: ", execute_str)

        self.cursor.execute(execute_str)
        data = self.cursor.fetchone()

        clothesNodeLower = ClothesNodeLower()
        clothesNodeLower.updateBySQL(data)

        return clothesNodeLower

    def queryNodeByPosition(self, position):
        execute_str = "SELECT * FROM intelligence_closet.dbo.clothes_node_lower WHERE [Position]  = {0}".format(
            position)
        print("queryNodeByPosition: ", execute_str)

        self.cursor.execute(execute_str)
        data = self.cursor.fetchone()

        if data != None:
            clothesNodeLower = ClothesNodeLower()
            clothesNodeLower.updateBySQL(data)

            return clothesNodeLower

        else:
            return None

    # 空缺的位置資訊(範圍 0~9 )
    def vacancyPosition(self):
        for i in range(10):
            if self.queryDataByPosition(i) == None:
                return i

        return -1

    # 透過位置找尋資料
    def queryDataByPosition(self, position):
        execute_str = "SELECT * FROM intelligence_closet.dbo.v_clothes_node WHERE Position = '{0}' ".format(
            position)
        self.cursor.execute(execute_str)
        data = self.cursor.fetchone()
        return data

    # 大到小分類: name 想找尋的分類
    def sortNameDESC(self, name):
        execute_str = "SELECT * FROM intelligence_closet.dbo.clothes_node_lower ORDER BY '{0}' DESC".format(
            name)
        print("sortNameDESC", execute_str)

        self.cursor.execute(execute_str)
        data = self.cursor.fetchone()
        return data

    # 大到小分類: name 想找尋的分類
    def sortNameASC(self, name):
        execute_str = "SELECT * FROM intelligence_closet.dbo.clothes_node_lower ORDER BY '{0}' ASC".format(
            name)

        self.cursor.execute(execute_str)
        data = self.cursor.fetchone()
        return data

    #     # 最後一個位置
    # def lastId(self):
    #     data = self.sortNameDESC('Id')

    #     print("data: ", data)
    #     if data == None:
    #         return 0

    #     clothesNodeLower = ClothesNodeLower()
    #     clothesNodeLower.updateBySQL(data)

    #     return clothesNodeLower.Id

    ###################### CREATE ######################

    def create(self, clothesNodeLower_dict):
        position = self.vacancyPosition()
        if position == -1:
            print("位置已滿")
            return False

        execute_str = "INSERT INTO clothes_node_lower (Position, ColorId, SubCategoryId, UsageCounter, CreateTime, ModifyTime , FilePosition, IsFavorite) " \
        + "VALUES ({0}, {1}, {2}, 0, GETDATE(), GETDATE(), '{3}', {4} )".format(
            position, clothesNodeLower_dict['ColorId'],
            clothesNodeLower_dict['SubCategoryId'],
            clothesNodeLower_dict['FilePosition'],
            clothesNodeLower_dict['IsFavorite'])

        print("create", execute_str)
        self.cnxn.cursor().execute(execute_str)
        self.cnxn.commit()

        return position

    ###################### UPDATE ######################
    def updatePositionToNull(self, position):

        if self.queryDataByPosition(position) == None:
            print('沒有此衣物')
            return False

        execute_str = "UPDATE clothes_node_lower SET Position = NULL WHERE Position = {0}".format(
            position)
        print(execute_str)

        self.cursor.execute(execute_str)
        self.cnxn.commit()

        return True

    ###################### DELETE ######################
    def deleteByPosition(self, position):

        if self.queryDataByPosition(position) == None:
            print('沒有此衣物')
            return False

        execute_str = "DELETE FROM clothes_node_lower WHERE Position = {0}".format(
            position)
        print(execute_str)

        self.cursor.execute(execute_str)
        self.cnxn.commit()

        return True
