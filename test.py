import sys, os
import json
sys.path.append(os.getcwd())  # 抓取路徑


from Service.categoryService import CategoryService
from Service.cityService import CityService 
from Service.clothesNodeService import ClothesNodeService 


# 1. Category
# categoryService = CategoryService()
# print(categoryService.queryAll()) # 搜尋全部: LIST
# print(categoryService.queryById(1)) # 透過ID搜尋一筆資料


# 2. City
# cityService = CityService()
# print(cityService.queryAll()) # 搜尋全部: LIST
# print(cityService.queryById(1)) # 透過ID搜尋一筆資料
# print(cityService.queryByName("新北市")) # 透過名字搜尋一筆資料

# 3. ClothesNode
clothesNodeService = ClothesNodeService()
# print(clothesNodeService.queryAll())
# print(clothesNodeService.queryById(2))
# print(clothesNodeService.queryByPosition(2))
# clothesNodeService.updatePositionToNull(5)
# clothesNode_create = '{ "Position": 13,"SubCategoryId": 5, "ColorId": 8, "UserPreferences": 7,  "UsageCounter":4, "CreateTime": "2020/01/01","ModifyTime": "2020/01/01", "FilePosition": "aaa" }'
# print(clothesNodeService.create(clothesNode_create))
# print(clothesNodeService.deleteByPosition(4))