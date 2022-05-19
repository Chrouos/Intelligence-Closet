import sys, os
sys.path.append(os.getcwd()) # 抓取路徑
from node import recommend_node

# from Service.nodeCRUD import nodeCRUD

# ndCrud = nodeCRUD()
# print(ndCrud.queryDataByPosition(1))

node = recommend_node(1)
node.printNodeData()