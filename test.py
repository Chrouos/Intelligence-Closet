import sys, os
sys.path.append(os.getcwd()) # 抓取路徑

from Algorithm_with_SQL.graph import recommend_graph

graph = recommend_graph('板橋') # 初始話 圖像

graph.getCombination()