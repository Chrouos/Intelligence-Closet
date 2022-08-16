import json
import os
import sys

import eel
sys.path.append(os.getcwd())  # 抓取路徑

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

user_id = 2

# 衣物圖形
@eel.expose
def comb_to_js():
    clothesGraphController = ClothesGraphController('板橋')
    graphComb = clothesGraphController.getCombination()
    print("comb_to_js: ", graphComb)

    return graphComb

@eel.expose
def get_camera_identify(): # 拍照
    try:
        idt = CamaraController()
        idt.getLastId()             # 獲得ID，目的是為了建立存檔位置
        idt.useCamara()             # 開啟攝象頭講圖片存檔

        idt.identifyCategory()      # 辨識樣式
        idt.identifyColor()         # 辨識顏色
        idt.printResult()            # 輸出結果

        return [idt.category, idt.color, idt.save_path, True]
    except Exception as e: 
        print("get_camera_identify", e)
        return False
    
@eel.expose
def identify_save_sql(category, color, save_path): # 確定存檔
    try:
        idt = CamaraController()
        idt.category = category
        idt.color = color
        idt.save_path = save_path
        print(category, color, save_path)

        idt.saveToSql()  # 存到資料庫

        return True
    except:
        print("GET CAMARA FALSE")
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
def weather_to_js(weatherPosition):  # 傳送天氣資訊

    we = WeatherInformationAPI(weatherPosition)  # 地點
    weather_list = we.getWeather()  # 獲得陣列(6個資訊)
    print(weatherPosition, weather_list)

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
    user_dict = userDashboardService.queryById(user_id) # 預設為2
    
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
    print("user: ", user, type(user))
    isSuccess = userDashboardService.updateById(user, user_id) # 預設為2 
    
    print("update_user_dashboard", isSuccess)
    
    return isSuccess
    
@eel.expose
def change_user(userId):
    global user_id 
    user_id = userId

eel.init('View/main')  # eel.init(網頁的資料夾)
eel.start('lobby.html', size=(1080, 720))  # eel.start(html名稱, size=(起始大小))
