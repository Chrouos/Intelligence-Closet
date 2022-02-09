import requests  # 要獲得天氣API
import re  # 正規表示法：regular expression


# 天氣的物件
class weather_information_API:

    # 初始化：位置、分類、天氣分數
    def __init__(self, city):
        self.__city = city
        self.__dataText = 'NONE'
        self.__temp = 0
        self.__humd = 0
        self.__d_tx = 0
        self.__d_tn = 0

    def setCity(self, newCity):
        self.__city = newCity

    def getCity(self):
        return self.__city

    def dataText_AutoRefresh(self):
        token = 'CWB-A69F077C-C940-4912-9FC2-99F44AA41A25'  # 授權碼
        required_item = 'TEMP,HUMD,D_TX,D_TN'  # 需要的項目：溫度、濕度、今日最高溫、今日最低溫

        # 搜尋的網址：回傳JSON (DONE)
        url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=' + token + '&format=JSON&locationName=' + str(
            self.__city) + '&elementName=' + required_item
        Data = requests.get(url)
        # print('Data Set:' , Data.text)
        self.__dataText = Data.text

    def reTEMP(self):
        # 以下正規表示法取出數值
        re_complete_temp = re.compile(
            '(TEMP)\W+(elementValue)\W+[0-9]+\W[0-9]')
        complete_temp = re_complete_temp.search(str(self.__dataText))

        self.__temp = float(complete_temp.group()[-4:])

        return self.__temp

    def reHUMD(self):
        # 以下正規表示法取出數值
        re_complete_humd = re.compile(
            '(HUMD)\W+(elementValue)\W+[0-9]\W[0-9]{2}')
        complete_humd = re_complete_humd.search(str(self.__dataText))

        self.__humd = float(complete_humd.group()[-4:])

        return self.__humd

    def reD_TX(self):
        # 以下正規表示法取出數值
        re_complete_DTX = re.compile(
            '(D_TX)\W+(elementValue)\W+[0-9]+\W[0-9]+')
        complete_DTX = re_complete_DTX.search(str(self.__dataText))

        self.__d_tx = float(complete_DTX.group()[-5:])

        return self.__d_tx

    def reD_TN(self):
        # 以下正規表示法取出數值
        re_complete_DTN = re.compile(
            '(D_TN)\W+(elementValue)\W+[0-9]+\W[0-9]+')
        complete_DTN = re_complete_DTN.search(str(self.__dataText))

        self.__d_tn = float(complete_DTN.group()[-5:])

        return self.__d_tn

    # 獲得天氣資訊：溫度、濕度、最高溫、最低溫
    def getWeather(self):
        self.dataText_AutoRefresh()  # 更新網址

        # 利用“正規化“只截取想要的資訊
        print('TEMP:', self.reTEMP())
        print('HUMD:', self.reHUMD())
        print("D_TX:", self.reD_TX())
        print("D_TN:", self.reD_TN())

        # 回傳溫度溫度、濕度、最高溫、最低溫
        return (self.__temp, self.__humd, self.__d_tx, self.__d_tn)


'''
建立天氣物件

變數包含：
城市: city
weather API 內的所有資料：dataText
temp：溫度
humd：濕度
d_tx：本日最高溫
d_tn：本日最低溫

方法包含：
刷新網址：：dataText_AutoRefresh（注意，每次使用都要刷新） 獲得溫度：reTEMP（溫度，單位：攝氏）
獲得濕度：：reHUMD（濕度，單位：百分率）
獲得本日最高溫：reD_TX（本日最高溫，單位：攝氏）
獲得本日最低溫：reD_TN（本日最低溫，單位：攝氏）
獲得所有天氣資訊：getWeather（溫度、濕度、最高溫、最低溫）
'''
