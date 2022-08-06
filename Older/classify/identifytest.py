import os
import sys

sys.path.append(os.getcwd())  # 抓取路徑

print(sys.path)

from Identify import identify

# 輸入內容為圖片編碼
identify = identify()

lastId = identify.getLastId()

print("SQL LAST ID: {0}".format(lastId))
identify.useCamara()

identify.identifyCategory()
identify.identifyColor()
identify.printResult()
print(identify.saveToSql())
