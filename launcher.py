import json
import os
import sys

import eel

from Algorithm_with_SQL.graph import recommend_graph
from Algorithm_with_SQL.weather import weather_information_API
from Service.stationCRUD import stationCRUD
from classify.Identify import identify

sys.path.append(os.getcwd())  # 抓取路徑

graph = recommend_graph('板橋')


@eel.expose
def weather_to_js(weatherPosition):  # 傳送天氣資訊

    graph.changeCity(weatherPosition[0])

    we = weather_information_API(weatherPosition[0])  # 地點
    weather_list = we.getWeather()  # 獲得陣列(6個資訊)

    print("weather_list: ", weather_list)
    print("weather_position: ", weatherPosition)

    # 以下轉換成 JSON格式的字串
    weather_dict = {
        'temp': weather_list[0], 'humd': weather_list[1],
        'd_tx': weather_list[2], 'd_tn': weather_list[3],
        'd_txt': weather_list[4], 'd_tnt': weather_list[5]
    }

    weather_json = json.dumps(weather_dict)

    weather_json = ""
    weather_json += '{"temp":' + str(weather_list[0])
    weather_json += ',"humd":"' + str(weather_list[1] * 100) + '"'
    weather_json += ',"d_tx":' + str(weather_list[2])
    weather_json += ',"d_tn":' + str(weather_list[3])
    weather_json += ',"d_txt":"' + str(weather_list[4]) + '"'
    weather_json += ',"d_tnt":"' + str(weather_list[5]) + '"}'

    print(weather_json)

    return weather_json


@eel.expose
def station_city_to_js():  # 傳送所有縣市資訊

    stCrud = stationCRUD()
    st_all_city = stCrud.queryCity()

    str_city = ""

    for index in range(len(st_all_city)):
        if index != 0:
            str_city += ","
        str_city += str(st_all_city[index])

    print("city: ", str_city)
    return str(str_city)


@eel.expose
def station_station_to_js(city):
    stCrud = stationCRUD()
    st_station_in_city = stCrud.queryStationNameByCityName(city[0])

    # st = station()
    # st.refreshDataByNet()
    # st_station_in_city = st.getStationByCity(city[0])

    str_station = ""

    for index in range(len(st_station_in_city)):
        if index != 0:
            str_station += ","
        str_station += str(st_station_in_city[index])

    print("station: ", str_station)
    return str(str_station)


@eel.expose
def comb_to_js():
    graph.updateNode()  # 更新節點
    graph.updateGraph()  # 更新圖形

    graphComb = graph.getCombination()

    return graphComb


@eel.expose
def get_camera_identify(): # 拍照
    try:
        idt = identify()
        idt.getLastId()  # 獲得ID，目的是為了建立存檔位置
        idt.useCamara()  # 開啟攝象頭講圖片存檔

        idt.identifyCategory()  # 辨識樣式
        idt.identifyColor()  # 辨識顏色
        idt.printResult()  # 輸出結果

        return [idt.category, idt.color, idt.save_path]
    except:
        return False

def identify_save_sql(category, color, save_path): # 確定存檔
    try:
        idt = identify()
        idt.category = category
        idt.color = color
        idt.save_path = save_path

        idt.saveToSql()  # 存到資料庫

        return True
    except:
        print("GET CAMARA FALSE")
        return False


eel.init('UI/web')  # eel.init(網頁的資料夾)
eel.start('post.html', size=(1920, 1080))  # eel.start(html名稱, size=(起始大小))
