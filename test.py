import sys, os
import json
from Model.Domain.color import Color
sys.path.append(os.getcwd())  # 抓取路徑

from Service.categoryService import CategoryService
from Service.cityService import CityService 
from Service.clothesNodeService import ClothesNodeService 
from Service.colorGraphService import ColorGraphService 

# 1. Category
# categoryService = CategoryService()
# print(categoryService.queryAll()) # 搜尋全部 LIST
# print(categoryService.queryById(1)) # 透過ID搜尋一筆資料


# 2. City
# cityService = CityService()
# print("1. 搜尋全部 LIST: ", cityService.queryAll()) # 搜尋全部 LIST
# print("2. 透過ID搜尋一筆資料 (1): ",cityService.queryById(1)) # 透過ID搜尋一筆資料
# print("3. 透過名字搜尋一筆資料 (新北市):",cityService.queryByName("新北市")) # 透過名字搜尋一筆資料

# 3. ClothesNode
# clothesNodeService = ClothesNodeService()
# print(clothesNodeService.queryAll())
# print(clothesNodeService.queryById(2))
# print(clothesNodeService.queryByPosition(2))
# clothesNodeService.updatePositionToNull(5)
# clothesNode_create = '{ "Position": 13,"SubCategoryId": 5, "ColorId": 8, "UserPreferences": 7,  "UsageCounter":4, "CreateTime": "2020/01/01","ModifyTime": "2020/01/01", "FilePosition": "aaa" }'
# print(clothesNodeService.create(clothesNode_create))
# print(clothesNodeService.deleteByPosition(4))

# 4. Color
# colorService = ColorService()
# print("1. 搜尋全部 LIST: ", colorService.queryAll()) # 搜尋全部 LIST
# print("2. 透過ID搜尋一筆資料 (2): ",colorService.queryById(2)) # 透過ID搜尋一筆資料
# print("3. 透過顏色的英文名稱搜尋 ID: ",colorService.queryIdByEngName("BLACK")) # 透過名字搜尋一筆資料

# 5. ColorGraph
# colorGraph = ColorGraphService()
# print("1. 搜尋全部 LIST: ", colorGraph.queryAll()) # 搜尋全部 LIST
# print("3. 透過上半身ID搜尋資料 LIST (0): ",colorGraph.queryUpperByColorId(2)) 
# print("4. 透過下半身ID搜尋資料 LIST (0): ",colorGraph.queryLowerByColorId(2)) 
# print("5. 更新分數(82): ", colorGraph.updateColorScoreById(4, 82)) 
# print("2. 透過ID搜尋一筆資料 (82): ",colorGraph.queryById(82)) # 透過ID搜尋一筆資料
