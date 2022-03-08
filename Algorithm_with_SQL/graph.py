from Algorithm_with_SQL.weather import weather_information_API
from Service.nodeCRUD import nodeCRUD
import random  # 亂數產生
import networkx as nx  # 生成圖與網路
import matplotlib.pyplot as plt  # 畫圖顯示


class recommend_Graph:
    def __init__(self, city):
        self.node = []  # 節點存放處（物件 node )
        self.edge = []  # 邊的存放處 (權重 {nodeA, nodeB, nodeC} )
        self.weather_info = weather_information_API(city)  # 取得城市當日天氣資訊：溫度、濕度、最高溫、最低溫


'''
建立圖形物件

變數包含:
節點:Node
權重與邊 {w,(A,B,C)}:Edge

方法包含:
新增節點:addNode (節點新增至陣列中, addEdge: 將所有上下衣物的邊連接)
輸出所有節點資訊: printNode
輸出所有邊(包含權重)資訊: printEdge
權重高到低輸出: combination

'''
