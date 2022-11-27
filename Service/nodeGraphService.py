from Model.DAO.nodeGraphDAO import NodeGraphDAO
from Model.Domain.nodeGraph import NodeGraph

import json


class NodeGraphService:

    # 建構子: 呼叫SQL
    def __init__(self):
        self.nodeGraphDAO = NodeGraphDAO()

    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        datas = self.nodeGraphDAO.queryAll()

        nodeGraph_dict = []
        for data in datas:
            nodeGraph_dict.append({
                'Id': data.Id,
                'UpperId': data.UpperId,
                'LowerId': data.LowerId,
                'OtherId': data.OtherId,
                'UserLike': data.UserLike,
                'CreateTime': data.CreateTime,
                'ModifyTime': data.ModifyTime
            })

        return nodeGraph_dict

    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.nodeGraphDAO.queryById(id)

        nodeGraph_dict = {
            'Id': data.Id,
            'UpperId': data.UpperId,
            'LowerId': data.LowerId,
            'OtherId': data.OtherId,
            'UserLike': data.UserLike,
            'CreateTime': data.CreateTime,
            'ModifyTime': data.ModifyTime
        }
        return nodeGraph_dict

    def queryByUpperId(self, id):
        datas = self.nodeGraphDAO.queryByUpperId(id)

        nodeGraph_dict = []
        for data in datas:
            nodeGraph_dict.append({
                'Id': data.Id,
                'UpperId': data.UpperId,
                'LowerId': data.LowerId,
                'OtherId': data.OtherId,
                'UserLike': data.UserLike,
                'CreateTime': data.CreateTime,
                'ModifyTime': data.ModifyTime
            })
        return nodeGraph_dict

    def queryByLowerId(self, id):
        datas = self.nodeGraphDAO.queryLowerId(id)

        nodeGraph_dict = []
        for data in datas:
            nodeGraph_dict.append({
                'Id': data.Id,
                'UpperId': data.UpperId,
                'LowerId': data.LowerId,
                'OtherId': data.OtherId,
                'UserLike': data.UserLike,
                'CreateTime': data.CreateTime,
                'ModifyTime': data.ModifyTime
            })
        return nodeGraph_dict

    def queryByOtherId(self, id):
        datas = self.nodeGraphDAO.queryByOtherId(id)

        nodeGraph_dict = []
        for data in datas:
            nodeGraph_dict.append({
                'Id': data.Id,
                'UpperId': data.UpperId,
                'LowerId': data.LowerId,
                'OtherId': data.OtherId,
                'UserLike': data.UserLike,
                'CreateTime': data.CreateTime,
                'ModifyTime': data.ModifyTime
            })
        return nodeGraph_dict

    def updateUserLikeById(self, combLike, id):
        self.nodeGraphDAO.updateUserLikeById(combLike, id)
        return True

    def create(self, jso):
        if isinstance(jso, str):
            nodeGraph_dict = json.loads(jso)
        else:
            nodeGraph_dict = jso
        
        nodeGraph = NodeGraph()
        nodeGraph.updateByDict(nodeGraph_dict)
        return self.nodeGraphDAO.create(nodeGraph)