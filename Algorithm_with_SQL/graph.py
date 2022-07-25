from Algorithm_with_SQL.node import recommend_node
from Algorithm_with_SQL.weather import weather_information_API
from Service.nodeCRUD import nodeCRUD
from Service.graphCRUD import graphCRUD
from Service.crudAccount import exportSQLLink

# import random  # 亂數產生
# import networkx as nx  # 生成圖與網路
import matplotlib.pyplot as plt  # 畫圖顯示
import math


class recommend_graph:
    def __init__(self, city):
        self.weather_info = weather_information_API(city)  # 取得城市當日天氣資訊：溫度、濕度、最高溫、最低溫
        
        # 利用資料庫更新所有節點資訊
        self.ndCrud = nodeCRUD()
        self.nodes = []
        self.updateNode()
        
        # 利用資料庫更新所有圖形資訊
        self.gpCrud = graphCRUD()
        self.graphs = []
        self.updateGraph()

        self.comfortableTemp = 26

    def updateNode(self):
        self.nodes = []
        allPositions = self.ndCrud.exitPosition()
        for position in allPositions:
            self.nodes.append(recommend_node(position, self.ndCrud))

    def updateGraph(self):
        self.graphs = []
        allGraph = self.gpCrud.queryAll()
        for gNode in allGraph:
            self.graphs.append([recommend_node(gNode[1], self.ndCrud), recommend_node(gNode[2], self.ndCrud), gNode[9], gNode[12], ])
            # ^ 衣物節點1, 衣物節點2, 天氣分數總分, 喜好分數總分, 
        

    def printNode(self):
        # for n in self.graph:
        #     print('位置：', n.position, '| 顏色：', n.color, '| 分類：', n.category)
        for n in self.nodes:
            print("-------------")
            n.printNodeData();
            print("-------------")
            
    def printEdge(self):
        for graph in self.graphs:
            print("位置: {0} & {1}, 樣式: {4}{2} & {5}{3}, 天氣分數:{6}, 喜好分數:{7}".format(graph[0].position, graph[1].position, graph[0].clothesName, graph[1].clothesName, graph[0].color, graph[1].color, graph[2], graph[3]))
            # print(gr[0].position, gr[1].position)

    def getCombination(self):
        
        combs = []
        
        self.weather_info.dataText_AutoRefresh()
        
        # 還相差的溫度
        diff = round(self.comfortableTemp - self.weather_info.reTEMP(), 2)
        # self.weather_info.printWeather()
        print("最適合溫度 - 現在溫度 = 相差溫度: {} - {} = {}".format(self.comfortableTemp, self.weather_info.reTEMP(), diff))
        
        
        # 弄成 dict增加可讀性
        combs_dict_list = []
        
        for graph in self.graphs:
            result = math.pow(math.floor((diff - graph[2])), 2)
            combs.append([result,
                          graph[0].position, graph[1].position,
                          graph[0].clothesName, graph[1].clothesName,
                          graph[0].filePosition, graph[1].filePosition])
            
            combs_dict_list.append({'resultScore': result, 
                                    'clothes1Position': graph[0].position, 'clothes2Position': graph[1].position,
                                    'clothes1Name': graph[0].clothesName, 'clothes2Name': graph[0].clothesName,
                                    'clothes1Path': graph[0].filePosition, 'clothes2Path': graph[1].filePosition})
        
        combs.sort(reverse = False)
        
        
        
        for c in combs:
            print(c)
            
        return combs_dict_list;
        
        
    def changeCity(self, city):
        self.weather_info.city = city
        self.weather_info.dataText_AutoRefresh()
    
'''
建立圖形物件

變數包含:
節點:Node
權重與邊 {w,(A,B)}:Edge

方法包含:
新增節點:addNode (節點新增至陣列中, addEdge: 將所有上下衣物的邊連接)
輸出所有節點資訊: printNode
輸出所有邊(包含權重)資訊: printEdge
權重高到低輸出: combination

顏色:
黑
灰
白
米 cream
紅
藍
黃
綠

'''
