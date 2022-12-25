# 個人的帳號密碼 sql server, 請不要更動crudAccount.py (輸入自己的即可)
from pickle import FALSE
from Model.DAO.crudAccount import ExportSQLLink
from Model.Domain.viewClothesNode import ViewClothesNode

import pyodbc
import time


class ViewClothesNodeDAO:

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
        execute_str = "SELECT * FROM intelligence_closet.dbo.v_clothes_node;"
        print("queryAll: ", execute_str)

        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()

        clothesNodeLists = []
        for data in datas:
            viewClothesNode = ViewClothesNode()
            viewClothesNode.updateBySQL(data)
            clothesNodeLists.append(viewClothesNode)

        return clothesNodeLists

    # 透過Id查找一筆資料: tuple
    def queryById(self, id):
        execute_str = "SELECT * FROM intelligence_closet.dbo.v_clothes_node WHERE Id = {0}".format(
            id)
        print("queryById: ", execute_str)

        self.cursor.execute(execute_str)
        data = self.cursor.fetchone()

        viewClothesNode = ViewClothesNode()
        viewClothesNode.updateBySQL(data)

        return viewClothesNode

    def queryNodeByPosition(self, position):
        execute_str = "SELECT * FROM intelligence_closet.dbo.v_clothes_node WHERE [Position]  = {0}".format(
            position)
        print("queryNodeByPosition: ", execute_str)

        self.cursor.execute(execute_str)
        data = self.cursor.fetchone()

        viewClothesNode = ViewClothesNode()
        viewClothesNode.updateBySQL(data)

        return viewClothesNode

    # 空缺的位置資訊(範圍 0~9 )
    def vacancyPosition(self):
        for i in range(10):
            if self.queryDataByPosition(i) == None:
                return i

        return -1

    # 透過位置找尋資料
    def queryDataByPosition(self, position):
        execute_str = "SELECT * FROM intelligence_closet.dbo.v_clothes_node WHERE Position = '{0}' ".format(position)
        self.cursor.execute(execute_str)
        data = self.cursor.fetchone()
        return data

    # 大到小分類: name 想找尋的分類
    def sortNameDESC(self, name):
        execute_str = "SELECT * FROM intelligence_closet.dbo.v_clothes_node ORDER BY '{0}' DESC".format(name)
        # print("sortNameDESC", execute_str)

        self.cursor.execute(execute_str)
        data = self.cursor.fetchone()
        return data

    # 大到小分類: name 想找尋的分類
    def sortNameASC(self, name):
        execute_str = "SELECT * FROM intelligence_closet.dbo.v_clothes_node ORDER BY '{0}' ASC".format(name)

        self.cursor.execute(execute_str)
        data = self.cursor.fetchone()
        return data

        # 最後一個位置
    def lastId(self):
        data = self.sortNameDESC('Id')

        # print("data: ", data)
        if data == None:
            return 0

        viewClothesNode = ViewClothesNode()
        viewClothesNode.updateBySQL(data)

        return viewClothesNode.Id

    # 搜尋所有資料: tuple
    def queryBySubCategoryId(self, subCategoryId):
        execute_str = "SELECT * FROM intelligence_closet.dbo.v_clothes_node where SubCategoryId = {0};".format(
            subCategoryId)
        print("queryBySubCategoryId: ", execute_str)

        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()

        clothesNodeLists = []
        for data in datas:
            viewClothesNode = ViewClothesNode()
            viewClothesNode.updateBySQL(data)
            clothesNodeLists.append(viewClothesNode)

        return clothesNodeLists

    # 搜尋所有資料: tuple
    def queryUpperAll(self):
        execute_str = "SELECT * FROM v_clothes_node vcn WHERE CategoryId = 1;"
        print("queryUpperAll: ", execute_str)

        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()

        viewClothesNodeLists = []
        for data in datas:
            viewClothesNode = ViewClothesNode()
            viewClothesNode.updateBySQL(data)
            viewClothesNodeLists.append(viewClothesNode)

        return viewClothesNodeLists

    # 搜尋所有資料: tuple

    def queryLowerAll(self):
        execute_str = "SELECT * FROM v_clothes_node vcn WHERE CategoryId = 2;"
        print("queryLowerAll: ", execute_str)

        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()

        viewClothesNodeLists = []
        for data in datas:
            viewClothesNode = ViewClothesNode()
            viewClothesNode.updateBySQL(data)
            viewClothesNodeLists.append(viewClothesNode)

        return viewClothesNodeLists

    # 搜尋所有資料: tuple

    def queryOtherAll(self):
        execute_str = "SELECT * FROM v_clothes_node vcn WHERE CategoryId != 1 AND CategoryId != 2;"
        print("queryOtherAll: ", execute_str)

        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()

        viewClothesNodeLists = []
        for data in datas:
            viewClothesNode = ViewClothesNode()
            viewClothesNode.updateBySQL(data)
            viewClothesNodeLists.append(viewClothesNode)

        return viewClothesNodeLists
    
    def queryPositionExitNode(self):
        execute_str = "SELECT * FROM v_clothes_node vcn WHERE Position is not null;"
        print("queryPositionExitNode: ", execute_str)

        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()

        viewClothesNodeLists = []
        for data in datas:
            viewClothesNode = ViewClothesNode()
            viewClothesNode.updateBySQL(data)
            viewClothesNodeLists.append(viewClothesNode)

        return viewClothesNodeLists

    def queryPositionIsNull(self):
        execute_str = "SELECT * FROM v_clothes_node vcn WHERE Position is null;"
        print("queryPositionIsNull: ", execute_str)

        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()

        viewClothesNodeLists = []
        for data in datas:
            viewClothesNode = ViewClothesNode()
            viewClothesNode.updateBySQL(data)
            viewClothesNodeLists.append(viewClothesNode)

        return viewClothesNodeLists

    def queryIsFavoriteByCategory(self, category):
        execute_str = ""
        if(category == 0):
            execute_str = "SELECT * FROM v_clothes_node vcn WHERE IsFavorite = 1;"
        elif(category == 1):
            execute_str = "SELECT * FROM v_clothes_node vcn WHERE IsFavorite = 1 AND CategoryId = 1;"
        elif(category == 2):
            execute_str = "SELECT * FROM v_clothes_node vcn WHERE IsFavorite = 1 AND CategoryId = 2;"
        elif(category == 3):
            execute_str = "SELECT * FROM v_clothes_node vcn WHERE IsFavorite = 1 AND CategoryId != 1 AND CategoryId != 2;"
        print("queryIsFavoriteByCategory: ", execute_str)

        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()

        viewClothesNodeLists = []
        for data in datas:
            viewClothesNode = ViewClothesNode()
            viewClothesNode.updateBySQL(data)
            viewClothesNodeLists.append(viewClothesNode)

        return viewClothesNodeLists
