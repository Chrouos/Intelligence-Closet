# 個人的帳號密碼 sql server, 請不要更動crudAccount.py (輸入自己的即可)
from Model.DAO.crudAccount import ExportSQLLink
from Model.Domain.nodeGraph import NodeGraph

import pyodbc
import pandas as pd


class NodeGraphDAO:

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
            print('NodeGraphDAO 操作成功')

        except:
            print('NodeGraphDAO 操作錯誤')

        self.cnxn = cnxn
        self.cursor = cnxn.cursor()

    # 搜尋所有資料: tuple
    def queryAll(self):
        execute_str = "SELECT * FROM intelligence_closet.dbo.node_graph;"
        print("queryAll: ", execute_str)

        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()

        nodeGraphLists = []
        for data in datas:
            nodeGraph = NodeGraph()
            nodeGraph.updateBySQL(data)
            nodeGraphLists.append(nodeGraph)
        return nodeGraphLists

    # 透過Id查找一筆資料: tuple
    def queryById(self, id):
        execute_str = "SELECT * FROM intelligence_closet.dbo.node_graph WHERE Id = {0}".format(
            id)
        print("queryById: ", execute_str)

        self.cursor.execute(execute_str)
        data = self.cursor.fetchone()

        nodeGraph = NodeGraph()
        if data != None:
            nodeGraph.updateBySQL(data)

        return nodeGraph

    def queryByUpperId(self, id):
        execute_str = "SELECT * FROM intelligence_closet.dbo.node_graph where UpperId = {0};".format(
            id)
        print("queryByUpperId: ", execute_str)

        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()

        nodeGraphLists = []
        for data in datas:
            nodeGraph = NodeGraph()
            nodeGraph.updateBySQL(data)
            nodeGraphLists.append(nodeGraph)

        return nodeGraphLists

    def queryByLowerId(self, id):
        execute_str = "SELECT * FROM intelligence_closet.dbo.node_graph where LowerId = {0};".format(
            id)
        print("queryByLowerId: ", execute_str)

        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()

        nodeGraphLists = []
        for data in datas:
            nodeGraph = NodeGraph()
            nodeGraph.updateBySQL(data)
            nodeGraphLists.append(nodeGraph)
        return nodeGraphLists

    def queryByOtherId(self, id):
        execute_str = "SELECT * FROM intelligence_closet.dbo.node_graph where OtherId = {0};".format(
            id)
        print("queryByOtherId: ", execute_str)

        self.cursor.execute(execute_str)
        datas = self.cursor.fetchall()

        nodeGraphLists = []
        for data in datas:
            nodeGraph = NodeGraph()
            nodeGraph.updateBySQL(data)
            nodeGraphLists.append(nodeGraph)
        return nodeGraphLists

    def updateCombLikeById(self, score, id):
        execute_str = "UPDATE intelligence_closet.dbo.node_graph SET CombLike = {0}, ModifyTime = GETDATE() WHERE Id = {1}".format(
            score, id)
        print("updateCombLikeById: ", execute_str)

        self.cursor.execute(execute_str)
        self.cnxn.commit()

        return True

    def create(self, combs):
        execute_str = "INSERT INTO intelligence_closet.dbo.node_graph (UpperId, LowerId, UserLike, CreateTime, ModifyTime) VALUES (" \
            + "{0}, {1}, {2}, GETDATE(), GETDATE())".format(combs.UpperId, combs.LowerId, combs.UserLike)

        print("create: ", execute_str)

        self.cursor.execute(execute_str)
        self.cnxn.commit()

        return True

    def createOther(self, combs):
        execute_str = "INSERT INTO intelligence_closet.dbo.node_graph (UpperId, LowerId, UserLike, CreateTime, ModifyTime) VALUES (" \
            + "null, null, 0, GETDATE(), GETDATE() )".format()

        print("create: ", execute_str)

        self.cursor.execute(execute_str)
        self.cnxn.commit()

        return True
