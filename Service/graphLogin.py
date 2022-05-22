
from graphCRUD import graphCRUD

graphCRUD = graphCRUD()

print("1. 搜尋全部徒圖型相關:\n", graphCRUD.queryAll())

print("2. 透過ViewId回傳:\n",graphCRUD.queryById(1))