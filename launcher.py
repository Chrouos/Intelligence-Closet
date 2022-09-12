from asyncio.windows_events import NULL
import json
import os
import sys

import eel

sys.path.append(os.getcwd())  # 抓取路徑
sys.dont_write_bytecode = True  # 不產生 pyc

## Controller
from Controller.crawlerStationController import CrawlerStationController
from Controller.camaraController import CamaraController
from Controller.clothesGraphController import ClothesGraphController
from Controller.weatherInformationAPI import WeatherInformationAPI
from Service.colorService import ColorService
from Service.subCategoryService import SubCategoryService
from Service.viewStationService import ViewStationService
from Service.cityService import CityService
from Service.userDashboardService import UserDashboardService
from Service.clothesNodeService import ClothesNodeService
from Service.viewClothesNodeService import ViewClothesNodeService
from Service.viewCategoryClothesService import ViewCategoryClothesService

user_id = 1


# 衣物圖形
@eel.expose
def comb_to_js():
    userDashboardService = UserDashboardService()
    user_dict = userDashboardService.queryById(user_id)  # 預設為2

    clothesGraphController = ClothesGraphController(user_dict['StationName'])
    graphComb = clothesGraphController.getCombination()
    # print("comb_to_js: ", graphComb)

    return graphComb


@eel.expose
def get_camera_identify():  # 拍照
    try:
        idt = CamaraController(0)
        idt.getLastId()  # 獲得ID，目的是為了建立存檔位置
        idt.useCamara()  # 開啟攝象頭講圖片存檔

        idt.identifyCategory()  # 辨識樣式
        idt.identifyColor()  # 辨識顏色
        idt.printResult()  # 輸出結果

        print("path:", idt.path)
        return [idt.category, idt.color, idt.path, True]

    except Exception as e:
        print("get_camera_identify", e)
        return [NULL, NULL, NULL, False]


@eel.expose
def identify_save_sql(category, color, save_path, isFavorite):  # 確定存檔
    try:
        # 儲存至sql的資料
        idt = CamaraController(0)
        idt.category = category
        idt.color = color
        idt.save_path = save_path
        idt.isFavorite = isFavorite

        print("identify_save_sql: ", category, color, save_path, isFavorite)

        idt.saveToSql()  # 存到資料庫

        return True
    except Exception as e:
        print("GET CAMARA FALSE", e)
        return False


@eel.expose
def get_all_sc_name():
    scCrud = SubCategoryService()
    datas = scCrud.queryAll()

    print("get_all_sc_name", datas)
    return datas


@eel.expose
def get_all_color():
    colorService = ColorService()
    datas = colorService.queryAll()

    print("get_all_color", datas)
    return datas


################################################################################## weather
@eel.expose
def weather_to_js(st):  # 傳送天氣資訊

    # userDashboardService = UserDashboardService()
    # user_dict = userDashboardService.queryById(user_id) # 預設為2

    # we = WeatherInformationAPI(user_dict['StationName'])  # 地點
    we = WeatherInformationAPI(st)
    weather_list = we.getWeather()  # 獲得陣列(6個資訊)
    print("weather_to_js", weather_list)

    return weather_list


@eel.expose
def station_city_to_js():  # 傳送所有縣市資訊

    cityService = CityService()
    city_dict = cityService.queryAll()

    print("city: ", city_dict)
    return city_dict


@eel.expose
def station_station_to_js(city):
    viewStationService = ViewStationService()
    station_dict = viewStationService.queryByCityId(city)

    print("station: ", station_dict, city)
    return station_dict


################################################################################## user


@eel.expose
def user_by_id_to_js():
    userDashboardService = UserDashboardService()
    user_dict = userDashboardService.queryById(user_id)  # 預設為2

    print("user_by_id_to_js: ", user_dict)
    return user_dict


@eel.expose
def all_user_to_js():
    userDashboardService = UserDashboardService()
    user_dict = userDashboardService.queryAll()

    print("all_user_to_js: ", user_dict)
    return user_dict


@eel.expose
def update_user_dashboard(user):
    userDashboardService = UserDashboardService()
    isSuccess = userDashboardService.updateById(user, user_id)  # 預設為2

    print("update_user_dashboard", isSuccess)

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

    print("clothes_to_js", v_clothes_dict)

    return v_clothes_dict


@eel.expose
def upper_clothes_to_js():
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryUpperAll()

    print("upper_clothes_to_js", v_clothes_dict)

    return v_clothes_dict


@eel.expose
def lower_clothes_to_js():
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryLowerAll()

    print("lower_clothes_to_js", v_clothes_dict)

    return v_clothes_dict


@eel.expose
def other_clothes_to_js():
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryOtherAll()

    print("other_clothes_to_js", v_clothes_dict)

    return v_clothes_dict


@eel.expose
def query_subCategory_byCategoryId(categoryId):
    viewCategoryClothesService = ViewCategoryClothesService()
    v_subCategory_dict = viewCategoryClothesService.queryByCategoryId(
        categoryId)  # 利用類別搜尋子類別 # 1:上半身, 2:下半身, 3:裙裝, 4:大衣
    print("query_subCategory_byCategoryId", v_subCategory_dict)

    return v_subCategory_dict


@eel.expose
def query_clothes_nodes_bySubCategoryId(categoryId):
    viewClothesNodeService = ViewClothesNodeService()
    v_clothes_dict = viewClothesNodeService.queryBySubCategoryId(
        categoryId)  # 利用類別搜尋子類別 # 1:上半身, 2:下半身, 3:裙裝, 4:大衣
    print("query_clothes_nodes_bySubCategoryId", v_clothes_dict)

    return v_clothes_dict


eel.init('View/mui')  # eel.init(網頁的資料夾)
# eel.start('User.html', size=(1920, 1080))  # eel.start(html名稱, size=(起始大小))

eel.start('User.html', size=(1920, 1080))  # eel.start(html名稱, size=(起始大小))
