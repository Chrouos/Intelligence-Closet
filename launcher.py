from asyncio.windows_events import NULL
import json
import os
import sys

import eel

from Model.Domain.clothesNode import ClothesNode

sys.path.append(os.getcwd())  # 抓取路徑
sys.dont_write_bytecode = True  # 不產生 pyc

## Controller
from Controller.crawlerStationController import CrawlerStationController
from Controller.camaraController import CamaraController
from Controller.clothesGraphController import ClothesGraphController
from Controller.weatherInformationAPI import WeatherInformationAPI
from Controller.weatherAPI import WeatherAPI
from Service.colorService import ColorService
from Service.subCategoryService import SubCategoryService
from Service.viewStationService import ViewStationService
from Service.viewVillageService import ViewVillageService
from Service.cityService import CityService
from Service.userDashboardService import UserDashboardService
from Service.ClothesNodeService import ClothesNodeService
from Service.viewClothesNodeService import ViewClothesNodeService, ViewClothesNode
from Service.viewCategoryClothesService import ViewCategoryClothesService
from Service.viewUserDashboardService import ViewUserDashboardService
from Service.nodeGraphService import NodeGraphService
from Controller.arduinoController import ArduinoController


user_id = 1
camara_choose = 1

from Controller.camaraController import *
# 相機物件
def get_x(r): return './images_original/'+r['image'] # create path to open images in the original folder
def get_y(r): return r['label'].split(' ') # split the labels using space as a delimitter
# 讀取圖檔
clf = joblib.load('Controller/joblib_export.pkl')

# 衣物圖形
@eel.expose
def comb_to_js():
    userDashboardService = UserDashboardService()
    user_dict = userDashboardService.queryById(user_id)  # 預設為1

    clothesGraphController = ClothesGraphController(user_dict['VillageId'])
    graphComb = clothesGraphController.getCombination()
    
    # print("comb_to_js: ", graphComb)

    return graphComb


@eel.expose
def get_camera_identify():  # 拍照
    try:
        
        # 將機器送到超音波前(準備拍照)
        arduinoController = ArduinoController()
        arduinoController.storgage_first_half()
        
        idt = CamaraController(camara_choose, clf)
        idt.useCamara()  # 開啟攝象頭講圖片存檔

        idt.identifyCategory()  # 辨識樣式
        idt.identifyColor()  # 辨識顏色
        idt.printResult()  # 輸出結果

        # print("path:", idt.path)
        return [idt.category, idt.color, idt.path, True]

    except Exception as e:
        print("get_camera_identify", e)
        return [NULL, NULL, NULL, False]


@eel.expose
def identify_save_sql(category, color, path, isFavorite):  # 確定存檔
    try:
        arduinoController = ArduinoController()
        
        # 儲存至sql的資料
        idt = CamaraController(camara_choose, clf)
        idt.category = category
        idt.color = color
        idt.path = path
        idt.isFavorite = isFavorite
        # print("identify_save_sql: ", category, color, path, isFavorite)

        # 將衣服送入圓盤(後半段)
        userDashboardService = UserDashboardService()
        user_dict = userDashboardService.queryById(user_id)  # 預設為1
        
        clothesNodeService = ClothesNodeService()
        position = clothesNodeService.vacancyPosition() # 剩餘的位置
        # print("剩餘位置", position)
        
        print("資料庫目前存放在:", user_dict['LastPosition'], ", 目前衣物空缺位置:", position)
        dist_roundTimes = 8
        if position > user_dict['LastPosition']:
            dist_roundTimes = position - user_dict['LastPosition']
        elif position < user_dict['LastPosition']:
            dist_roundTimes = user_dict['LastPosition'] - position
        print("要轉動的次數", dist_roundTimes)
        
        userDashboardService.updateLastPosition(user_id, position)
        arduinoController.storgage_second_half(dist_roundTimes)
        
        idt.saveToSql()  # 存到資料庫

        return True
    except Exception as e:
        # print("identify_save_sql exception: ", e)
        return False


@eel.expose
def get_all_sc_name():
    scCrud = SubCategoryService()
    datas = scCrud.queryAll()

    # print("get_all_sc_name", datas)
    return datas


@eel.expose
def get_all_color():
    colorService = ColorService()
    datas = colorService.queryAll()

    # print("get_all_color", datas)
    return datas


################################################################################## weather


@eel.expose
def weather_to_js():  # 傳送天氣資訊

    userDashboardService = UserDashboardService()
    user_dict = userDashboardService.queryById(user_id)  # 預設為2

    we = WeatherAPI(user_dict['VillageId'])  # 地點Id
    weather_list = we.getWeather()  # 獲得陣列(11個資訊)
    # print("weather_to_js", weather_list)

    return weather_list


@eel.expose
def city_to_js():  # 傳送所有縣市資訊

    cityService = CityService()
    city_dict = cityService.queryAll()

    # print("city: ", city_dict)
    return city_dict


@eel.expose
def station_station_to_js(city):
    viewStationService = ViewStationService()
    station_dict = viewStationService.queryByCityId(city)

    # print("station: ", station_dict, city)
    return station_dict


@eel.expose
def village_to_js(city):
    viewVillageService = ViewVillageService()
    village_dict = viewVillageService.queryByCityId(city)

    # print("village: ", village_dict, city)
    return village_dict


################################################################################## user


@eel.expose
def user_by_id_to_js():
    viewUserDashboardService = ViewUserDashboardService()
    user_dict = viewUserDashboardService.queryById(user_id)  # 預設為2

    # print("user_by_id_to_js: ", user_dict)
    return user_dict


@eel.expose
def all_user_to_js():
    userDashboardService = UserDashboardService()
    user_dict = userDashboardService.queryAll()

    # print("all_user_to_js: ", user_dict)
    return user_dict


@eel.expose
def update_user_dashboard(user):
    userDashboardService = UserDashboardService()
    isSuccess = userDashboardService.updateById(user, user_id)  # 預設為2

    # print("update_user_dashboard", isSuccess)

    return isSuccess


@eel.expose
def change_user(userId):
    global user_id
    user_id = userId


################################################################################## clothes node


@eel.expose
def clothes_to_js():
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryAll()

    # print("clothes_to_js", v_clothes_dict)

    return v_clothes_dict


@eel.expose
def upper_clothes_to_js():
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryUpperAll()

    # print("upper_clothes_to_js", v_clothes_dict)

    return v_clothes_dict


@eel.expose
def lower_clothes_to_js():
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryLowerAll()

    # print("lower_clothes_to_js", v_clothes_dict)

    return v_clothes_dict


@eel.expose
def other_clothes_to_js():
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryOtherAll()

    # print("other_clothes_to_js", v_clothes_dict)

    return v_clothes_dict


@eel.expose
def isFavorite_clothes_to_js(category):
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryIsFavoriteByCategory(category)

    # print("other_clothes_to_js", v_clothes_dict)

    return v_clothes_dict


@eel.expose
def query_clothes_nodes_byPositionIsNull():
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryPositionIsNull()

    # print("clothes_to_js", v_clothes_dict)

    return v_clothes_dict


@eel.expose
def query_subCategory_byCategoryId(categoryId):
    viewCategoryClothesService = ViewCategoryClothesService()
    v_subCategory_dict = viewCategoryClothesService.queryByCategoryId(
        categoryId)  # 利用類別搜尋子類別 # 1:上半身, 2:下半身, 3:裙裝, 4:大衣
    # print("query_subCategory_byCategoryId", v_subCategory_dict)

    return v_subCategory_dict


@eel.expose
def query_clothes_nodes_bySubCategoryId(categoryId):
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryBySubCategoryId(
        categoryId)  # 利用類別搜尋子類別 # 1:上半身, 2:下半身, 3:裙裝, 4:大衣
    # print("query_clothes_nodes_bySubCategoryId", v_clothes_dict)

    return v_clothes_dict


@eel.expose
def query_clothesNode_byId(clothesId):
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryById(clothesId)
    # print("query_clothesNode_byId", v_clothes_dict)

    return v_clothes_dict


# 拿取衣物
@eel.expose
def updatePositionToNull(position):
    arduinoController = ArduinoController()
    
    userDashboardService = UserDashboardService()
    user_dict = userDashboardService.queryById(user_id)  # 預設為1
    
    dist_roundTimes = position - user_dict['LastPosition']
    if dist_roundTimes == 0:
        dist_roundTimes = 8
    print("要轉動的次數", dist_roundTimes)
    arduinoController.pickUp_one_clothes(dist_roundTimes)
    userDashboardService.updateLastPosition(user_id, position)
    
    clothesNodeService = ClothesNodeService()
    result = clothesNodeService.updatePositionToNull(position)
    
    # print("query_clothesNode_byId", result)

    return result


@eel.expose
def color_to_js():  # 傳送所有顏色

    colorService = ColorService()
    color_dict = colorService.queryAll()

    # print("color: ", color_dict)
    return color_dict


@eel.expose
def sub_category_to_js():  # 傳送所有sub catrgory

    subCategoryService = SubCategoryService()
    subCategory_dict = subCategoryService.queryAll()

    # print("subCategory: ", subCategory_dict)
    return subCategory_dict


@eel.expose
def vacancyPosition():
    clothesNodeService = ClothesNodeService()
    result = clothesNodeService.vacancyPosition()
    # print("vacancyPosition", result)

    return result


################################################################################## clothes node graph


@eel.expose
def creat_node_graph(firstClohtesNode, secondClohtesNode, userLike):  # 新增node_graph
    nodeGraph_dict = {}
    if(firstClohtesNode['CategoryId'] == 1):
        nodeGraph_dict['UpperId'] = firstClohtesNode['Id']
        nodeGraph_dict['LowerId'] = secondClohtesNode['Id']
        nodeGraph_dict['OtherId'] = NULL
        nodeGraph_dict['UserLike'] = userLike


    elif(secondClohtesNode['CategoryId'] == 1):
        nodeGraph_dict['UpperId'] = secondClohtesNode['Id']
        nodeGraph_dict['LowerId'] = firstClohtesNode['Id']
        nodeGraph_dict['OtherId'] = NULL
        nodeGraph_dict['UserLike'] = userLike

    # 儲存至node_graph sql的資料
    nodeGraphService = NodeGraphService()

    if(nodeGraphService.queryByUpperIdAndLowerId(nodeGraph_dict['UpperId'], nodeGraph_dict['LowerId'])):
        isSuccess = nodeGraphService.updateByUpperIdAndLowerId(nodeGraph_dict)
        print("update_node_graph: ", firstClohtesNode, secondClohtesNode, userLike)
    else:
        isSuccess = nodeGraphService.create(nodeGraph_dict)
        print("creat_node_graph: ", firstClohtesNode, secondClohtesNode, userLike)

    return isSuccess


@eel.expose
def update_clothes_node(clothesNode): # 更新 clothes node
    clothesNodeService = ClothesNodeService()
    
    isSuccess = clothesNodeService.updateById(clothesNode)
    
    # 修改衣物時若修改了類別
    clothesNodeService.ChangeCategory_UpdateTheGraph(clothesNode)
    

    print("update_clothes_node", isSuccess)

    return isSuccess


@eel.expose
def return_zero_clothes_node(clothesNodeId): # clothes node 歸零
    clothesNodeService = ClothesNodeService()
    isSuccess = clothesNodeService.returnZeroClothesNode(clothesNodeId)

    # print("return_zero_clothes_node", isSuccess)

    return isSuccess

@eel.expose
def return_zero_clothes_node_graph(firstClohtesNode, secondClohtesNode): # clothes node graph 歸零
    nodeGraph_dict = {}
    if(firstClohtesNode['CategoryId'] == 1):
        nodeGraph_dict['UpperId'] = firstClohtesNode['Id']
        nodeGraph_dict['LowerId'] = secondClohtesNode['Id']
        nodeGraph_dict['OtherId'] = NULL
        nodeGraph_dict['UserLike'] = 0


    elif(secondClohtesNode['CategoryId'] == 1):
        nodeGraph_dict['UpperId'] = secondClohtesNode['Id']
        nodeGraph_dict['LowerId'] = firstClohtesNode['Id']
        nodeGraph_dict['OtherId'] = NULL
        nodeGraph_dict['UserLike'] = 0

    # 儲存至node_graph sql的資料
    nodeGraphService = NodeGraphService()

    if(nodeGraphService.queryByUpperIdAndLowerId(nodeGraph_dict['UpperId'], nodeGraph_dict['LowerId'])):
        isSuccess = nodeGraphService.updateByUpperIdAndLowerId(nodeGraph_dict)
        
    # print("return_zero_clothes_node_graph: ", firstClohtesNode, secondClohtesNode, 0)

    return isSuccess

@eel.expose
def delete_clothes_node(clothesNodeId): # clothes node 歸零
    clothesNodeService = ClothesNodeService()
    isSuccess = clothesNodeService.deleteById(clothesNodeId)

    # print("delete_clothes_node", isSuccess)

    return isSuccess


# 硬體啟動

@eel.expose
def arduino_car_back_now():
    
    arduinoController = ArduinoController()
    arduinoController.car_back_now()
    
    return true

@eel.expose
def query_node_graph_setting(upperId, lowerId):
    nodeGraphService = NodeGraphService()
    v_node_graph = nodeGraphService.queryByUpperIdAndLowerId(upperId, lowerId)
    print("query_node_graph_setting", v_node_graph)
    
    return v_node_graph

@eel.expose
def storage_old_clothes(clothesNode):
    try:
        arduinoController = ArduinoController()

        # 將衣服送入圓盤(後半段)
        userDashboardService = UserDashboardService()
        user_dict = userDashboardService.queryById(user_id)  # 預設為1
        
        clothesNodeService = ClothesNodeService()
        position = clothesNodeService.vacancyPosition() # 剩餘的位置
        # print("剩餘位置", position)
        print("資料庫目前存放在:", user_dict['LastPosition'], ", 目前衣物空缺位置:", position)
        dist_roundTimes = 8
        if position > user_dict['LastPosition']:
            dist_roundTimes = position - user_dict['LastPosition']
        elif position < user_dict['LastPosition']:
            dist_roundTimes = user_dict['LastPosition'] - position
        print("要轉動的次數", dist_roundTimes)
        print(clothesNode)
        
        viewClothesNode = ViewClothesNode()
        if type(clothesNode) is dict:
            viewClothesNode.updateByDict(clothesNode)
        
        if type(clothesNode) is str:
            clothesNode_dic = json.loads(clothesNode)
            viewClothesNode.updateByDict(clothesNode_dic)
        
        userDashboardService.updateLastPosition(user_id, position)
        clothesNodeService.updateIdInPosition(position, clothesNode) #TODO: 
        arduinoController.storgage_second_half(dist_roundTimes)

        clothesGraph_create = '{{"ClothesNodeLastId": {0}, "CategoryId": {1}}}'.format(
            viewClothesNode.Id, viewClothesNode.CategoryId)
        print("saveClothesGraph_Data:", clothesGraph_create)
        
        nodeGraphService = NodeGraphService()
        nodeGraphService.create(clothesGraph_create)
        
        

        return True
    except Exception as e:
        print("storage_old_clothes exception: ", e)
        return False

eel.init('View/mui')  # eel.init(網頁的資料夾)
# eel.start('User.html', size=(1920, 1080))  # eel.start(html名稱, size=(起始大小))

# eel.start('User.html',mode='chrome-app', size=(1920, 1080), cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])  # eel.start(html名稱, size=(起始大小))

eel.start('User.html', mode='chrome-app', port=8080, cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])

# eel.start('User.html', mode='chrome', cmdline_args=['--kiosk'])
