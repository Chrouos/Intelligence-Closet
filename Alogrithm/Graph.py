from Weather import weather_information_API
import random  # 亂數產生
import networkx as nx  # 生成圖與網路
import matplotlib.pyplot as plt  # 畫圖顯示


class recommend_Graph:
    def __init__(self, city):
        self.node = []  # 節點存放處（物件 node )
        self.edge = []  # 邊的存放處 (權重 {nodeA, nodeB} )
        self.weather_info = weather_information_API(
            city)  # 取得城市當日天氣資訊：溫度、濕度、最高溫、最低溫

    def addNode(self, newNode):

        # 將所有分類不同的上下衣物連線，賦予權重
        for n in self.node:
            self.addEdge(newNode, n)

        self.node.append(newNode)  # 將節點新增至陣列當中

    def printNode(self):
        for n in self.node:
            print('位置：', n.position, '| 顏色：', n.color, '| 分類：', n.category)

    def printEdge(self):
        for e in self.edge:
            print(e)

    # 配分（根據穿搭的顏色進行搭配）（後續新增）
    def addEdge(self, nodeA, nodeB):

        # 先判斷是不是為不同類別
        if nodeA.category == nodeB.category:
            return

        # 給予分數（Not Done）
        w = int(random.random() * 10)

        # 連接邊
        self.edge.append([w, [nodeA, nodeB]])

    def combination(self):
        comb = []
        for e in self.edge:
            total = e[0] + e[1][0].weather_score + e[1][1].weather_score
            comb.append([total, [e[1][0].position, e[1][1].position]])
            # print(e[0], e[1][0].position)

        comb.sort(reverse=True)

        for c in comb:
            print(c)

    def draw(self):
        G = nx.Graph()
        for n in self.node:
            G.add_node(str(n.position))

        edgesList = []

        for e in self.edge:
            edgesList.append((str(e[1][0].position), str(e[1][1].position)))

        G.add_edges_from(edgesList)

        nx.draw(G, with_labels=True, node_color='y')
        plt.show()


'''
建立圖形物件

變數包含：
節點：Node
權重與邊 {w,(A,B)}：Edge

方法包含：

新增節點：：addNode
節點新增至陣列中
將所有上下衣物的邊連接
輸出所有節點資訊：printNode
'''
