from crawler.crawler import station
from Service.nodeCRUD import nodeCRUD
from Algorithm_with_SQL.weather import weather_information_API
from Algorithm_with_SQL.graph import recommend_Graph
from Algorithm_with_SQL.node import recommend_node


station = station()  # 各站
crud = nodeCRUD()  # SQL ServeR
graph = recommend_Graph('埔心')  # 圖形


Datas = crud.queryDataInNode()

for data in Datas:
    node = recommend_node(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], crud)
    graph.addNode(node)

# graph.printEdge()
# print(graph.edge)
graph.combination()
