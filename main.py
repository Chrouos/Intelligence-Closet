from crawler.crawler import station
from Service.nodeCRUD import nodeCRUD
from Algorithm_with_SQL.weather import weather_information_API
from Algorithm_with_SQL.graph import recommend_Graph
from Algorithm_with_SQL.node import recommend_node


station = station()  # 各站
crud = nodeCRUD()  # SQL ServeR
# # 圖形
graph = recommend_Graph('埔心')


# weather = weather_information_API('埔心')
# print(weather.getWeather())

Datas = crud.queryData()
for data in Datas:
    print(data)
    node = recommend_node(data[0], data[1], data[2], data[4])
    graph.addNode(node)

graph.printNode()
# print(graph.node)
graph.refresh_allWeatherScore()
# graph.systemRecommend()
