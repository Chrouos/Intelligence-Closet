import sys, os
sys.path.append(os.getcwd()) # 抓取路徑

from Algorithm_with_SQL.graph import recommend_graph

graph = recommend_graph('板橋')

graph.updateNode() # 更新節點
graph.updateGraph() # 更新圖形

graphComb = graph.getCombination() 