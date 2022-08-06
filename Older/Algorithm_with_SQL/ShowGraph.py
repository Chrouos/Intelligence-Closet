import sys, os
sys.path.append(os.getcwd()) # 抓取路徑
from graph import recommend_graph

from Service.graphCRUD import graphCRUD
from Service.nodeCRUD import nodeCRUD

graph = recommend_graph('板橋') # 初始話 圖像

print("1. 輸出所有node資訊:\n")
graph.printNode()

print("2. 輸出所有圖像節點:")
graph.printEdge()

print("3. 最適合的組合")
graph.getCombination()