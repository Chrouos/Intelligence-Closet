from Algorithm_with_SQL.weather import weather_information_API
from Service.nodeCRUD import nodeCRUD
# import random  # 亂數產生
# import networkx as nx  # 生成圖與網路
import matplotlib.pyplot as plt  # 畫圖顯示


class recommend_Graph:
    def __init__(self, city):
        self.node = []  # 節點存放處（物件 node )
        self.edge = []  # 邊的存放處 (權重 {nodeA, nodeB} )
        self.otherList = []  # 儲存其他衣物 (物件 node)
        self.weather_info = weather_information_API(city)  # 取得城市當日天氣資訊：溫度、濕度、最高溫、最低溫

        self.comfortableTemp = 26

    def addNode(self, newNode):

        # 若為其他類別，存入即結束
        if newNode.category == 'other':
            self.otherList.append(newNode)
            return

        # 將所有分類不同的上下衣物連線，賦予權重
        for n in self.node:
            # 先判斷是不是為不同類別
            if n.category != newNode.category:
                self.addEdge(n, newNode)

        self.node.append(newNode)  # 將節點新增至陣列當中

    # 配分（根據穿搭的顏色進行搭配）（後續新增）
    def addEdge(self, nodeA, nodeB):

        w = self.colorAllocation(nodeA.color, nodeB.color)

        # 連接邊
        self.edge.append([w, [nodeA, nodeB]])

    def colorAllocation(self, A_color, B_color):

        # 同色系
        if A_color == B_color:
            return 6
        else:
            if A_color == 'black' or B_color == 'black':
                if A_color == 'gray' or B_color == 'gray':
                    return 5
                elif A_color == 'white' or B_color == 'white':
                    return 5
                elif A_color == 'cream' or B_color == 'cream':
                    return 4
                else:
                    return 3
            elif A_color == 'white' or B_color == 'white':
                if A_color == 'gray' or B_color == 'gray':
                    return 4
                elif A_color == 'cream' or B_color == 'cream':
                    return 5
                else:
                    return 3
            else:
                if A_color == 'gray' or B_color == 'gray':
                    return 3
                elif A_color == 'cream' or B_color == 'cream':
                    return 2
                else:
                    return 3

    # print out

    def printNode(self):
        for n in self.node:
            print('位置：', n.position, '| 顏色：', n.color, '| 分類：', n.category)

    def printEdge(self):
        for e in self.edge:
            print(e[0], ": ", e[1][0].position, e[1][1].position, " | ", e[1][0].category, e[1][1].category)

    def combination(self):
        combs = []

        # 使用26度法則計算分數
        self.weather_info.dataText_AutoRefresh()

        # 還相差的溫度
        diff = round(self.comfortableTemp - self.weather_info.reTEMP(), 2)
        # diff = 16  # 代表目前10度
        print("最適合溫度 - 現在溫度 = 相差溫度: {} - {} = {}".format(self.comfortableTemp, self.weather_info.reTEMP(), diff))

        scoreBase = 40
        needCoat = ''
        for e in self.edge:

            # 公式計算
            stillNeed = diff - (int(e[1][0].weatherScore) + int(e[1][1].weatherScore))
            if stillNeed >= 9:
                needCoat = '你需要加件厚外套'
            elif stillNeed >= 5:
                needCoat = '建議你加件薄外套'
            else:
                needCoat = '還不需要加外套'

            total = round(scoreBase - abs((diff - stillNeed) * 1.2), 2)
            combs.append([total + e[0], [e[1][0].position, e[1][1].position], [e[1][0].type, e[1][1].type], needCoat])

        combs.sort(reverse=True)
        for comb in combs:
            print(comb)

    #!### GET, SET

    def setcomfortableTemp(self, newTemp):
        self.comfortableTemp = newTemp

    def refresh_allWeatherScore(self):
        for n in self.node:
            n.refresh_WS(self.weather_info.getWeather())


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
