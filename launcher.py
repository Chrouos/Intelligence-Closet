from asyncio.windows_events import NULL
import json
import os
import sys
from time import sleep

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

import json
from json import load

jsonFile = open('./setting.json','r')
settingJson = json.load(jsonFile)
total_closet_sapce = settingJson['real_closet_space']

user_id = 1
camara_choose = 1

from Controller.camaraController import *
# 相機物件
def get_x(r): return './images_original/'+r['image'] # create path to open images in the original folder
def get_y(r): return r['label'].split(' ') # split the labels using space as a delimitter
# 讀取圖檔
clf = joblib.load('Controller/joblib_export.pkl')


def lock_disc_feet(position, user_lastposition):
    """
        為了使圓盤不要傾倒，將圓盤的腳位進行偏移
        腳位共八點 1 ~ 8
        
        
        + Parameters
        ------------ 
        position: int
            要前往的位置
            
        user_lastposition: int
            目前使用者最後的位置
        
        
        + Examples
        ----------
        # 到使用者的位置
        userDashboardService = UserDashboardService()
        user_dict = userDashboardService.queryById(user_id)
        
        # 找到目前衣櫃內布還有剩餘的位置
        clothesNodeService = ClothesNodeService()
        position = clothesNodeService.vacancyPosition()
        
        # 依據真實腳位移動
        dist_roundTimes = lock_disc_feet(position, user_dict['LastPosition'])

    """
    
    # 腳位共八點, 若剛好同點就轉八次回到原地
    dist_roundTimes = total_closet_sapce 
    if position != user_lastposition:
        dist_roundTimes = (position - user_lastposition) * 3 % total_closet_sapce
    print( "user last position:", user_lastposition, ", go to position:", position, ", 要轉動的次數", dist_roundTimes)
    return dist_roundTimes

# 衣物圖形
@eel.expose
def comb_to_js(): # 獲得天氣推薦衣物組合，給JavaScript (Json)
    
    try:
        # 獲得使用者資訊(1) -> 取得使用者填寫的鄉鎮區編號(2) -> 獲得推薦天氣衣物組合(3)
        userDashboardService = UserDashboardService()               
                        
        user_dict = userDashboardService.queryById(user_id)                         # (1)
        clothesGraphController = ClothesGraphController(user_dict['VillageId'])     # (2)
        graphComb = clothesGraphController.getCombination()                         # (3)

        return graphComb
    except Exception as e:
        print("[Fail] comb_to_js:", e)
        return NULL
    


@eel.expose
def get_all_sc_name():  # 獲得所有的 sub_category 資料
    try:
        scCrud = SubCategoryService()
        datas = scCrud.queryAll()
        return datas
    except Exception as e:
        print("[Fail] get_all_sc_name:", e)
        return NULL


@eel.expose
def get_all_color():  # 獲得所有的 color 資料  
    try:
        colorService = ColorService()
        datas = colorService.queryAll()
        return datas
    except Exception as e:
        print("[Fail] get_all_color:", e)
        return NULL

@eel.expose
def weather_to_js():  # 獲得天氣資訊到JavaScript
    try:
        # 獲得使用者目前居住地(0) -> 中央氣象局 API 獲得天氣資訊(1)
        
        # (0)
        userDashboardService = UserDashboardService()
        user_dict = userDashboardService.queryById(user_id)  
        we = WeatherAPI(user_dict['VillageId'])  # 地點Id
        
        # (1)
        weather_list = we.getWeather()  # 獲得陣列 (11個資訊)

        return weather_list
    except Exception as e:
        print("[Fail] weather_to_js:", e)
        return NULL

@eel.expose
def city_to_js():  # 獲得所有的 city 資料
    try:
        cityService = CityService()
        city_dict = cityService.queryAll()
        return city_dict
    except Exception as e:
        print("[Fail] city_to_js:", e)
        return NULL

@eel.expose
def village_to_js(city):    # 獲得所有的 village 資料
    try:
        viewVillageService = ViewVillageService()
        village_dict = viewVillageService.queryByCityId(city)
        return village_dict
    except Exception as e:
        print("[Fail] village_to_js:", e)
        return NULL


@eel.expose
def user_by_id_to_js(): # 獲得使用者資料 viewUserDashboard
    try:
        viewUserDashboardService = ViewUserDashboardService()
        user_dict = viewUserDashboardService.queryById(user_id)  # 預設為1

        return user_dict
    except Exception as e:
        print("[Fail] user_by_id_to_js:", e)
        return NULL


@eel.expose
def all_user_to_js():   # 所有使用者
    try:
        userDashboardService = UserDashboardService()
        user_dict = userDashboardService.queryAll()

        return user_dict
    except Exception as e:
        print("[Fail] all_user_to_js:", e)
        return NULL

@eel.expose
def update_user_dashboard(user): # 更改使用者資料
    try:
        userDashboardService = UserDashboardService()
        isSuccess = userDashboardService.updateById(user, user_id)  # 預設為1
        return isSuccess
    except Exception as e:
        print("[Fail] update_user_dashboard:", e)
        return NULL

@eel.expose
def change_user(userId):
    global user_id
    user_id = userId


@eel.expose
def clothes_to_js():    # 獲得所有衣物資訊
    try:
        viewClothesNodeService = ViewClothesNodeService()
        v_clothes_dict = viewClothesNodeService.queryAll()
        return v_clothes_dict
    except Exception as e:
        print("[Fail] update_user_dashboard:", e)
        return NULL


@eel.expose
def upper_clothes_to_js():
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryUpperAll()
    return v_clothes_dict


@eel.expose
def lower_clothes_to_js():
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryLowerAll()
    return v_clothes_dict


@eel.expose
def other_clothes_to_js():
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryOtherAll()
    return v_clothes_dict


@eel.expose
def isFavorite_clothes_to_js(category):
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryIsFavoriteByCategory(category)
    return v_clothes_dict


@eel.expose
def query_clothes_nodes_byPositionIsNull():
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryPositionIsNull()
    return v_clothes_dict


@eel.expose
def query_subCategory_byCategoryId(categoryId):
    viewCategoryClothesService = ViewCategoryClothesService()
    v_subCategory_dict = viewCategoryClothesService.queryByCategoryId(categoryId)  
    # 利用類別搜尋子類別 # 1:上半身, 2:下半身, 3:裙裝, 4:大衣

    return v_subCategory_dict


@eel.expose
def query_clothes_nodes_bySubCategoryId(categoryId):
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryBySubCategoryId(categoryId)  # 利用類別搜尋子類別 # 1:上半身, 2:下半身, 3:裙裝, 4:大衣
    return v_clothes_dict


@eel.expose
def query_clothesNode_byId(clothesId):
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryById(clothesId)

    return v_clothes_dict

@eel.expose
def color_to_js():  # 傳送所有顏色
    colorService = ColorService()
    color_dict = colorService.queryAll()
    return color_dict


@eel.expose
def sub_category_to_js():  # 傳送所有sub catrgory
    subCategoryService = SubCategoryService()
    subCategory_dict = subCategoryService.queryAll()
    return subCategory_dict


@eel.expose
def vacancyPosition():  # 獲得剩餘位置
    clothesNodeService = ClothesNodeService()
    result = clothesNodeService.vacancyPosition()
    return result


@eel.expose
def creat_node_graph(firstClohtesNode, secondClohtesNode, userLike):  # 新增node_graph
    try:
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

        # 修改
        if(nodeGraphService.queryByUpperIdAndLowerId(nodeGraph_dict['UpperId'], nodeGraph_dict['LowerId'])):
            isSuccess = nodeGraphService.updateByUpperIdAndLowerId(nodeGraph_dict)
            # print("update_node_graph: ", firstClohtesNode, secondClohtesNode, userLike)
        # 新增
        else:
            isSuccess = nodeGraphService.create(nodeGraph_dict)
            # print("creat_node_graph: ", firstClohtesNode, secondClohtesNode, userLike)

        return isSuccess
    except Exception as e:
        print("[Fail] creat_node_graph:", e)
        return False


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
        
    return isSuccess

@eel.expose
def delete_clothes_node(clothesNodeId): # clothes node 歸零
    clothesNodeService = ClothesNodeService()
    isSuccess = clothesNodeService.deleteById(clothesNodeId)
    return isSuccess


@eel.expose
def most_subCategory_to_js():  # 傳送存放最多種類的衣服資料
    viewClothesNodeService = ViewClothesNodeService()
    most_subCategory = viewClothesNodeService.queryMostSubCategory()
    return most_subCategory


@eel.expose
def most_color_to_js():  # 傳送存放最多顏色的衣服資料
    viewClothesNodeService = ViewClothesNodeService()
    most_color = viewClothesNodeService.queryMostColor()
    return most_color


@eel.expose
def most_counter_to_js():  # 傳送最常拿出來的衣服資料
    viewClothesNodeService = ViewClothesNodeService()
    most_counter = viewClothesNodeService.queryMostCounter()
    return most_counter


@eel.expose
def query_node_graph_setting(upperId, lowerId):
    nodeGraphService = NodeGraphService()
    v_node_graph = nodeGraphService.queryByUpperIdAndLowerId(upperId, lowerId)
    print("query_node_graph_setting", v_node_graph)
    
    return v_node_graph

# ---------------------------------------------------------------------- 硬體啟動 

@eel.expose
def putNullPositionModel_toZero(): # 拿取衣物 2: 把空的模塊放回去
    
    try:
        arduinoController = ArduinoController()
        userDashboardService = UserDashboardService()
        
        user_dict = userDashboardService.queryById(user_id)     # 使用者資訊    
        
        print("將模塊送回位置 {} 號".format(user_dict['LastPosition']))
        arduinoController.put_EntrancePositionZero(user_dict['LastPosition'])
        
        userDashboardService.updateLastPosition(user_id, -1)  # 修改使用者的最後存放位置
        
        return True
        
    except Exception as e:
        print("[putNullPositionModel_toZero] get_camera_identify:", e)

@eel.expose
def updatePositionToNull(node): # 拿取衣物 1
    sleep(1)
    
    try:
        # 變數取得(0) -> Arduino轉動圓盤並將衣物取出(1) -> 完善結果(2)
        
        # (0)
        arduinoController = ArduinoController()
        userDashboardService = UserDashboardService()
        clothesNodeService = ClothesNodeService()
        viewClothesNodeService = ViewClothesNodeService()
        nodeGraphService = NodeGraphService()
        
        # (1)
        print("從歸零位置將位置 {} 的模塊送至入口".format(node['Position']))
        arduinoController.takeClothes_single(node['Position'])
        
        # (2)
        userDashboardService.updateLastPosition(user_id, node['Position'])  # 修改使用者的最後存放位置
        result = clothesNodeService.updatePositionToNull(node['Position'])  # 修改衣物位置為NULL, 使用次數 + 1
        
        vNode = viewClothesNodeService.queryById(node['Id'])
        result = nodeGraphService.deleteByBullPosition(vNode['CategoryId'], vNode['Id'])

        return result

    except Exception as e:
        print("[Fail] updatePositionToNull:", e)
        return NULL


@eel.expose
def updatePositionToNull_TwoClothes(position1, position2, clothes_graph): # 拿取衣物
    sleep(1)
    
    try:
        
        # 準備:   變數取得(0)
        # 第一件: Arduino轉動圓盤並將衣物取出(1) -> 完善結果(2)
        # 第二件: Arduino轉動圓盤並將衣物取出(3) -> 完善結果(4)
        
        # (0)
        arduinoController = ArduinoController()
        userDashboardService = UserDashboardService()
        clothesNodeService = ClothesNodeService()
        nodeGraphService = NodeGraphService()
        viewClothesNodeService = ViewClothesNodeService()
        
        # (1)
        arduinoController.takeClothes_single(position1)
        
        # (2)
        userDashboardService.updateLastPosition(user_id, position1)  # 修改使用者的最後存放位置
        result = clothesNodeService.updatePositionToNull(position1)  # 修改衣物位置為NULL, 使用次數 + 1
        
        vNode = viewClothesNodeService.queryById(clothes_graph['Clothes1Id'])
        result = nodeGraphService.deleteByBullPosition(vNode['CategoryId'], vNode['Id'])
        
        # (3)
        arduinoController.takeClothes_single(position2)
        
        # (4)
        userDashboardService.updateLastPosition(user_id, position2)  # 修改使用者的最後存放位置
        result = clothesNodeService.updatePositionToNull(position2)  # 修改衣物位置為NULL, 使用次數 + 1
        
        vNode = viewClothesNodeService.queryById(clothes_graph['Clothes2Id'])
        result = nodeGraphService.deleteByBullPosition(vNode['CategoryId'], vNode['Id'])

        return result

    except Exception as e:
        print("[Fail] updatePositionToNull:", e)
        return NULL
    

@eel.expose
def storage_old_clothes(clothesNode): # 存放 舊衣物
    sleep(1)
    
    try:
        
        # 變數設定(0) -> Arduino將衣物重新存放(1) -> 衣物資料的位置擺放回來(2) -> 增加該衣物的圖形(3) 
        
        # (0)
        arduinoController = ArduinoController()
        userDashboardService = UserDashboardService()
        clothesNodeService = ClothesNodeService()
        nodeGraphService = NodeGraphService()

        # (1)
        user_dict = userDashboardService.queryById(user_id)     # 使用者資訊    
        
        print("將模塊送回位置 {} 號".format(user_dict['LastPosition']))
        arduinoController.putClothes(user_dict['LastPosition'])
        userDashboardService.updateLastPosition(user_id, -1)      # 修改使用者的最後存放位置
        
        # (2)
        clothesNodeService.updateIdInPosition(user_dict['LastPosition'], clothesNode)    # 將原本的衣服重新加入位置
        
        # (3)
        viewClothesNode = ViewClothesNode()
        if type(clothesNode) is dict:
            viewClothesNode.updateByDict(clothesNode)
        
        if type(clothesNode) is str:
            clothesNode_dic = json.loads(clothesNode)
            viewClothesNode.updateByDict(clothesNode_dic)

        clothesGraph_create =   '{{"ClothesNodeLastId": {0}, "CategoryId": {1}}}'.format(
                                viewClothesNode.Id, 
                                viewClothesNode.CategoryId)
        nodeGraphService.create(clothesGraph_create)
        
        
        return True
    except Exception as e:
        print("storage_old_clothes exception: ", e)
        return False

@eel.expose
def getNullPositionModel_toEntrance(): # 拿空的模塊在入口等待
    
    try:
        # 變數
        arduinoController = ArduinoController()
        clothesNodeService = ClothesNodeService()
        userDashboardService = UserDashboardService()
        
        # 獲取資訊
        position = clothesNodeService.vacancyPosition()         # 衣櫃內布，剩餘的位置
        
        # 取得資料
        print("從歸零位置將空模塊送至入口")
        arduinoController.takeClothes_single(position)
        userDashboardService.updateLastPosition(user_id, position)  # 修改最後存放位置
        
        return True
        
    except Exception as e:
        print("[getNullPositionModel_toEntrance] get_camera_identify:", e)
        return NULL

@eel.expose
def put_cancel(): # 取消
    
    try:
        # 變數
        arduinoController = ArduinoController()
        clothesNodeService = ClothesNodeService()
        userDashboardService = UserDashboardService()
        
        # (0)
        user_dict = userDashboardService.queryById(user_id)     # 使用者資訊    
        
        # (1)
        print("[取消] 將模塊送回位置 {} 號".format(user_dict['LastPosition']))
        arduinoController.putClothes(user_dict['LastPosition'])
        userDashboardService.updateLastPosition(user_id, -1)  # 修改最後存放位置
        
        return True
        
    except Exception as e:
        print("[getNullPositionModel_toEntrance] get_camera_identify:", e)
        return NULL

@eel.expose
def get_camera_identify():  # 拍照
    try:
        
        # 啟動Arduino將模型車送到超音波前，準備拍照(1) -> 拍照(2) -> 辨識結果(3)
        arduinoController = ArduinoController()
        idt = CamaraController(camara_choose, clf)  # 選擇攝像頭
        
        # (1)
        print("將模塊從入口送至歸零位置，等待拍照")
        arduinoController.entranceToZero()         # 將拿取衣物歸位等待拍照
        
        # (2) 
        idt.useCamara()                     

        # (3) 
        idt.identifyCategory()                      # 辨識樣式          
        idt.identifyColor()                         # 辨識顏色         
        idt.printResult()                           # 輸出結果

        return [idt.category, idt.color, idt.path, True]

    except Exception as e:
        print("[Fail] get_camera_identify:", e)
        return [NULL, NULL, NULL, False]


@eel.expose
def identify_save_sql(category, color, path, isFavorite):  # 辨識完的結果 -> 確定存檔
    sleep(1)
    
    try:
        
        # 獲得資訊(0) -> Arduino將衣物送入存放位置，後半段(1) -> 將資料存到資料庫(2)
        
        # 變數設定
        arduinoController = ArduinoController()
        clothesNodeService = ClothesNodeService()
        userDashboardService = UserDashboardService()
        idt = CamaraController(camara_choose, clf)
        
        # (0)
        user_dict = userDashboardService.queryById(user_id)     # 使用者資訊    
        
        # (1)
        print("將模塊送回位置 {} 號".format(user_dict['LastPosition']))
        arduinoController.put_ZeroPositionZero(user_dict['LastPosition'])                                  # 啟動機器轉動所需次數 + 存放
        
        # (2)
        idt.category = category     # 類別
        idt.color = color           # 顏色
        idt.path = path             # 存放的位置
        idt.isFavorite = isFavorite # 是否喜愛(由前端送入)
        idt.saveToSql()             # 存到資料庫
        
        userDashboardService.updateLastPosition(user_id, -1)  # 修改最後存放位置

        return [True]
    except Exception as e:
        print("[Fail] identify_save_sql:", e)
        return False



# ------------------------------------------ 啟動器

eel.init('View/mui')  # eel.init(網頁的資料夾)
# eel.start('User.html', mode='chrome-app', port=8080, cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])

# eel.start('User.html', size=(1920, 1080))  # eel.start(html名稱, size=(起始大小))
eel.start('User.html',mode='chrome-app', size=(1920, 1080), cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])  # eel.start(html名稱, size=(起始大小))
# eel.start('User.html', mode='chrome', cmdline_args=['--kiosk'])
