# from Weather import weather_information_API  # 獲得天氣資訊 API
# from Node import recommend_node
# from Graph import recommend_Graph

# # 以下建立 圖形中的節點 #
# node = recommend_node(1, 'upper', '藍', 'long_TShirt')
# node2 = recommend_node(2, 'lower', '白', 'long_pants')
# node3 = recommend_node(3, 'lower', '黑', 'short_pants')
# node4 = recommend_node(4, 'lower', '黃', 'long_skirt')
# node5 = recommend_node(5, 'upper', '黑', 'short_TShirt')
# node6 = recommend_node(6, 'other', '紅', 'coat')
# node7 = recommend_node(7, 'other', '黑', 'downCoat')

# nodeList = [node, node2, node3, node4, node5, node6, node7]

# # 圖形
# graph = recommend_Graph('埔心')
# for n in nodeList:  # 增加節點
#     graph.addNode(n)

# # graph.printEdge()
# # print(graph.otherList)

# graph.refresh_allWeatherScore()
# graph.systemRecommend()

# print(graph.weather_info.getWeather())
