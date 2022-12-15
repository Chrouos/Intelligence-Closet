from Service.viewClothesNodeService import ViewClothesNodeService, ViewClothesNodeDAO
from Service.viewClothesGraphService import ViewClothesGraphService
# from Controller.weatherInformationAPI import WeatherInformationAPI
from Controller.weatherAPI import WeatherAPI

# import random  # 亂數產生
# import networkx as nx  # 生成圖與網路
import matplotlib.pyplot as plt  # 畫圖顯示
import math


class ClothesGraphController:
    def __init__(self, villageId):
        self.weatherAPI = WeatherAPI(villageId)  # 取得城市當日天氣資訊：溫度、濕度、最高溫、最低溫
        
        # 利用資料庫更新所有節點資訊
        self.viewClothesNodeService = ViewClothesNodeService()
        self.nodes = []
        self.updateNode()
        
        # 利用資料庫更新所有圖形資訊
        self.viewClothesGraphService = ViewClothesGraphService()
        self.graphs = []
        self.updateGraph()

        self.comfortableTemp = 26
        
    
    # 更新所有節點資訊
    def updateNode(self):
        self.nodes = self.viewClothesNodeService.queryPositionExitNode()

    def updateGraph(self):
        self.graphs = []
        allGraph = self.viewClothesGraphService.queryAll()
        
        # 製成圖形
        for gNode in allGraph:
            
            if gNode['UpperClothesId'] != None and gNode['LowerClothesId'] != None:
                viewClothesNodeDAO = ViewClothesNodeDAO()
                self.graphs.append([
                                    viewClothesNodeDAO.queryById(gNode['UpperClothesId']),
                                    viewClothesNodeDAO.queryById(gNode['LowerClothesId']),
                                    gNode['TotalScore'],
                                    gNode['TotalPreferences'],
                                    gNode['UserLike']])
            # ^ 衣物節點1, 衣物節點2, 天氣分數總分, 喜好分數總分, 
        

    def printNode(self):
        for n in self.nodes:
            print("編號: {0}\n位置: {1}\n衣服種類:{2}".format(n['Id'], n['Position'], n['SubCategoryName'])) 
            print("顏色:{0}\n檔案位置:{1}".format(n['ColorName'], n['FilePosition']))
            print("-------------")
            
    def printEdge(self):
        for graph in self.graphs:
            print("位置: {0} & {1}, 樣式: {4}{2} & {5}{3}, 天氣分數:{6}, 喜好分數:{7}, 組合喜好分數: {8}".format(graph[0].Position, graph[1].Position, graph[0].CategoryName, graph[1].CategoryName, graph[0].ColorName, graph[1].ColorName, graph[2], graph[3], graph[4]))
            # print(gr[0].position, gr[1].position)

    def getCombination(self):
        
        combs = []
        
        weather_dict = self.weatherAPI.getWeather()
        # 還相差的溫度 abs((26 + user_weatherLike - now_weather) - weather_score)
        diff = round(self.comfortableTemp - int(weather_dict['T']), 3)
        self.weatherAPI.printWeather()
        print("最適合溫度 - 現在溫度 = 相差溫度: {} - {} = {}".format(self.comfortableTemp, weather_dict['T'], diff))
        
        
        # 弄成 dict增加可讀性
        combs_dict_list = []
        
        
        # 公式: ( 26 - 使用者喜好) - ( diff - 天氣分數總合)
        for graph in self.graphs:
            # result = math.floor((diff - graph[2]))
            result = abs(diff -  - graph[2])
            print("result: ", result, graph[2])
            combs.append([  result,
                            graph[0].Position, graph[1].Position,
                            graph[0].ColorName, graph[1].ColorName,
                            graph[0].SubCategoryName, graph[1].SubCategoryName,
                            graph[0].FilePosition, graph[1].FilePosition])
            
            combs_dict_list.append({'ResultScore': result,
                                    'Clothes1Id': graph[0].Id, 'Clothes2Id': graph[1].Id,
                                    'Clothes1Position': graph[0].Position, 'Clothes2Position': graph[1].Position,
                                    'Clothes1Color': graph[0].ColorName, 'Clothes2Color': graph[1].ColorName,
                                    'Clothes1Name': graph[0].SubCategoryName, 'Clothes2Name': graph[1].SubCategoryName,
                                    'Clothes1Path': graph[0].FilePosition, 'Clothes2Path': graph[1].FilePosition})
        
        # combs.sort(reverse = False)
        
        
        
        for c in combs:
            print(c)

        print("combs_dict_list: ", combs_dict_list)
        return combs_dict_list
        
        
    def changeCity(self, villageId):
        self.weatherAPI.villageId = villageId
        self.weatherAPI.getWeather()
    
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
