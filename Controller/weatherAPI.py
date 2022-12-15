from cmath import e
import requests  # 要獲得天氣API
import urllib.parse # url encode
import json

from Service.viewUserDashboardService import ViewUserDashboardService
from Service.viewVillageService import ViewVillageService

user_id = 1

# 天氣的物件
class WeatherAPI:

    # 初始化:
    def __init__(self, villageId):
        self.__villageId = villageId
        self.__dataText = {}  # 全部的資料
        self.type = 1
        self.__T = 0  # 溫度
        self.__AT = 0  # 體感溫度
        self.__UVI = 0  # 紫外線指數
        self.__MaxAT = 0  # 最高體感溫度
        self.__MinAT = 0  # 最低體感溫度
        self.__Wx = 0  # 天氣現象
        self.__WS = 0  # 風速
        self.__RH = 0  # 相對溼度
        self.__PoP12h = 0  # 12h降雨機率
        self.__CI = 0  # 舒適度

    def setVillageId(self, newVillageId):
        self.__villageId = newVillageId

    def getVillage(self):
        return self.__villageId

    def getDataText(self):
        return self.__dataText

    # 重整網址
    def dataText_AutoRefresh(self):
        self.type = 1
        viewVillageService = ViewVillageService()
        viewVillage = viewVillageService.queryById(self.__villageId)
        dayLocationId = 'F-D0047-' + viewVillage['DayAPIId']
        weekLocationId = 'F-D0047-' + viewVillage['WeekAPIId']

        token = 'CWB-A69F077C-C940-4912-9FC2-99F44AA41A25'  # 授權碼
        # 需要的項目：溫度、體感溫度、天氣現象、風速、相對溼度、12h降雨機率、舒適度、天氣描述
        required_item = 'T,AT,Wx,WS,RH,PoP12h,CI,WeatherDescription'
        # 每3小時
        # 搜尋的網址：回傳JSON (DONE)
        url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-093?Authorization=' + token + '&locationId=' + dayLocationId+ '&locationName=' + urllib.parse.quote(viewVillage['VillageName']) + '&elementName=' + required_item
        # print(url)
        Data = requests.get(url)
        data_json = Data.json()
        locations = data_json['records']['locations'][0]['location'][0]['weatherElement']

        data_dict ={}

        for location in locations:
            elementName = location['elementName']
            value = location['time'][0]['elementValue'][0]['value']
            data_dict[elementName] = value
        
        # 每12小時
        # 需要的項目：紫外線指數、最高體感溫度、最低體感溫度
        required_item = 'MaxAT,MinAT,UVI'
        url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-093?Authorization=' + token + '&locationId=' + weekLocationId+ '&locationName=' + urllib.parse.quote(viewVillage['VillageName']) + '&elementName=' + required_item

        Data = requests.get(url)
        data_json = Data.json()

        locations = data_json['records']['locations'][0]['location'][0]['weatherElement']

        for location in locations:
            elementName = location['elementName']
            value = location['time'][0]['elementValue'][0]['value']
            data_dict[elementName] = value

        self.__dataText = data_dict
        self.__T = data_dict['T']  # 溫度
        self.__AT = data_dict['AT']  # 體感溫度
        self.__UVI = data_dict['UVI']  # 紫外線指數
        self.__MaxAT = data_dict['MaxAT']  # 最高體感溫度
        self.__MinAT = data_dict['MinAT']  # 最低體感溫度
        self.__Wx = data_dict['Wx']  # 天氣現象
        self.__WS = data_dict['WS']  # 風速
        self.__RH = data_dict['RH']  # 相對溼度
        self.__PoP12h = data_dict['PoP12h']  # 12h降雨機率
        self.__CI = data_dict['CI']  # 舒適度


    def getWeather(self):

        try:
            self.dataText_AutoRefresh()
            # 更新所有溫度資訊

            weather_dict = self.__dataText

            print(weather_dict)

            # 回傳溫度、體感溫度、紫外線指數、最高體感溫度、最低體感溫度、天氣現象、風速、相對溼度、12h降雨機率、舒適度、天氣描述
            return weather_dict
        except:
            return "此站未提供天氣資訊"

    def printWeather(self):

        # 利用“正規化“只截取想要的資訊
        print("T:", self.__T)



'''
建立天氣物件

變數包含:
鄉鎮: village
weather API 內的所有資料:dataText
T : 溫度
AT: 體感溫度
UVI: 紫外線指數
MaxAT: 最高體感溫度
MinAT: 最低體感溫度
Wx: 天氣現象
WS: 風速
RH: 相對溼度
PoP12h: 12h降雨機率
CI: 舒適度
WeatherDescription: 天氣描述

方法包含:
刷新網址:dataText_AutoRefresh(!! 註: 每次使用都要刷新) 

獲得所有天氣資訊:getWeather(溫度、濕度、最高溫、最低溫、最高溫時間段、最低溫時間段) (!! 註:不需要使用 dataText_AutoRefresh )
輸出所有天氣資訊:printWeather(溫度、濕度、最高溫、最低溫、最高溫時間段、最低溫時間段)
'''
