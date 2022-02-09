from Weather import weather_information_API  # 獲得天氣資訊 API
from Node import recommend_node
from Graph import recommend_Graph

# 以下建立 圖形中的節點 #
node = recommend_node(1, '上', '藍')
node2 = recommend_node(2, '下', '白')
node3 = recommend_node(3, '下', '黑')
node4 = recommend_node(4, '下', '黃')
node5 = recommend_node(5, '上', '黑')
nodeList = [node, node2, node3, node4, node5]

# 圖形
graph = recommend_Graph('埔心')

# 節點內部的測試資料
# print('--- NODE ---')
# print(node.position, node.category, node.weather_score)

# 圖形內部的測試資料
print('--- GRAPH ---')
for n in nodeList:  # 增加節點
    graph.addNode(n)
graph.printNode()
graph.printEdge()
print('---FUNC TEST---')
graph.combination()
# graph.draw() # 畫圖


#print(graph.node[0], graph.node[0].position, graph.node[0].category, graph.node[0].weather_score)
#print(graph.weather_info.getCity() ,graph.weather_info.getWeather())

#### get Weather ####
#print('--- WEATHER ---')
#weather = Weather_information_API('天母')
#print(weather.getCity(), weather.getWeather())
