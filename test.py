import sys, os
import json
from Model.Domain.color import Color
from Model.Domain.station import Station
sys.path.append(os.getcwd())  # 抓取路徑

from Service.categoryService import CategoryService
from Service.cityService import CityService 
from Service.colorService import ColorService 
from Service.clothesNodeService import ClothesNodeService 
from Service.colorGraphService import ColorGraphService 
from Service.stationService import StationService 
from Service.subCategoryService import SubCategoryService 
from Service.userCombsService import UserCombsService 
from Service.userDashboardService import UserDashboardService 
from Service.viewCategoryClothesService import ViewCategoryClothesService 
from Service.viewClothesGraphService import ViewClothesGraphService 
from Service.viewClothesNodeService import ViewClothesNodeService 
from Service.viewColorGraphService import  ViewColorGraphService
from Service.viewStationService import  ViewStationService


## Controller
from Controller.crawlerStationController import CrawlerStationController
from Controller.camaraController import CamaraController
from Controller.clothesGraphController import ClothesGraphController
from Controller.weatherInformationAPI import WeatherInformationAPI

# 1. Category
# categoryService = CategoryService()
# print(categoryService.queryAll()) # 搜尋全部 LIST
# print(categoryService.queryById(1)) # 透過ID搜尋一筆資料


# 2. City
# cityService = CityService()
# print("1. 搜尋全部 LIST: ", cityService.queryAll()) # 搜尋全部 LIST
# print("2. 透過ID搜尋一筆資料 (1): ",cityService.queryById(1)) # 透過ID搜尋一筆資料
# print("3. 透過名字搜尋一筆資料 (新北市):",cityService.queryByName("新北市")) # 透過名字搜尋一筆資料
# print("4. 新增: ", cityService.create("無名小鎮"))

# 3. ClothesNode
# clothesNodeService = ClothesNodeService()
# print("最後一個位子:", clothesNodeService.lastId())
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
# print("3. 透過顏色的英文名稱搜尋 ID: ",colorService.queryIdByEngName("black")) # 透過名字搜尋一筆資料

# 5. ColorGraph
# colorGraph = ColorGraphService()
# print("1. 搜尋全部 LIST: ", colorGraph.queryAll()) # 搜尋全部 LIST
# print("3. 透過上半身ID搜尋資料 LIST (0): ",colorGraph.queryUpperByColorId(2)) 
# print("4. 透過下半身ID搜尋資料 LIST (0): ",colorGraph.queryLowerByColorId(2)) 
# print("5. 更新分數(82): ", colorGraph.updateColorScoreById(4, 82)) 
# print("2. 透過ID搜尋一筆資料 (82): ",colorGraph.queryById(82)) # 透過ID搜尋一筆資料

# 6. Station
# station = StationService()
# print("1. 搜尋全部 LIST: ", station.queryAll()) # 搜尋全部 LIST
# print("2. 透過CityId找: ", station.queryByCityId(2))
# station_create = '{ "StationNumber": "ABCDE", "StationName": "測試站號", "CityId": 0, "Address": "Address",  "Remark": "Remark", "Work": "0"}'
# station.create(station_create)
# station.deleteById(1276)
# station.deleteAllData()

# 7. SubCategory
# subCategoryService = SubCategoryService()
# print("1. 搜尋全部 LIST: ", subCategoryService.queryAll()) # 搜尋全部 LIST
# print("2. 透過Id找: ", subCategoryService.queryById(2))
# print("3. 透過CategoryId找: ", subCategoryService.queryByCategoryId(2))
# subCategoryService.updateScoreById(0, 16)

# 8. UserCombs
# userCombsService = UserCombsService()
# print("1. 搜尋全部 LIST: ", userCombsService.queryAll()) # 搜尋全部 LIST
# print("2. 透過Id找: ", userCombsService.queryById(2))

# 9. UserDashboard
# userDashboardService = UserDashboardService()
# print("1. 搜尋全部 LIST: ", userDashboardService.queryAll()) # 搜尋全部 LIST
# print("2. 透過Id找: ", userDashboardService.queryById(2))

# 10. ViewCategoryClothes
# viewCategoryClothesService = ViewCategoryClothesService()
# print("1. 搜尋全部 LIST: ",viewCategoryClothesService.queryAll())
# print(viewCategoryClothesService.queryById(2))

# 11. ViewClothesGraphService
# viewClothesGraphService = ViewClothesGraphService()
# print("1. 搜尋全部 LIST: ",viewClothesGraphService.queryAll())
# print(viewClothesGraphService.queryById(2))

# 12 ViewClothesNode
# viewClothesNodeService = ViewClothesNodeService()
# print("1. 搜尋全部 LIST: ",viewClothesNodeService.queryAll())
# print(viewClothesNodeService.queryById(2))
# print(viewClothesNodeService.queryPositionExitNode())

# 13. ViewColorGraph 
# viewColorGraphService = ViewColorGraphService()
# print("1. 搜尋全部 LIST: ",viewColorGraphService.queryAll())
# print(viewColorGraphService.queryByLowerColorId(2))
# print(viewColorGraphService.queryByUpperColorId(2))

# 14. Station
# viewStationService = ViewStationService()
# print("1. 搜尋全部 LIST: ", viewStationService.queryAll()) # 搜尋全部 LIST
# print("2. 透過CityId找: ", viewStationService.queryByCityId(2))
# station_create = '{ "StationNumber": "ABCDE", "StationName": "測試站號", "CityId": 0, "Address": "Address",  "Remark": "Remark", "Work": "0"}'


#####################################

# 更新站別 !!
# crawlerStationController = CrawlerStationController()
# crawlerStationController.refreshAllData()

# 相機物件
# camaraController = CamaraController()
# camaraController.getLastId()
# camaraController.useCamara()
# camaraController.identifyColor()
# camaraController.identifyCategory()
# camaraController.saveToSql()
# camaraController.printResult()


# 圖形物件
# clothesGraphController = ClothesGraphController('板橋')
# clothesGraphController.updateNode()
# clothesGraphController.printNode()
# clothesGraphController.printEdge()
# clothesGraphController.getCombination()

## 天氣物件
# weatherInformationAPI = WeatherInformationAPI('花蓮')
# weatherInformationAPI.getWeather()
# weatherInformationAPI.printWeather()