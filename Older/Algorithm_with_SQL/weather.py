from pickle import NONE
import requests  # 要獲得天氣API
import re  # 正規表示法：regular expression


# 天氣的物件
class weather_information_API:

    # 初始化:
    def __init__(self, city):
        self.__city = city
        self.__dataText = 'NONE'  # 全部的資料
        self.type = 1
        self.__temp = 0  # 溫度
        self.__humd = 0  # 濕度
        self.__d_tx = 0  # 最高溫
        self.__d_tn = 0  # 最低溫
        self.__d_txt = 0  # 最高溫時間點
        self.__d_tnt = 0  # 最低溫時間點

    def setCity(self, newCity):
        self.__city = newCity

    def getCity(self):
        return self.__city

    def getDataText(self):
        return self.__dataText

    # 重整網址
    def dataText_AutoRefresh(self):
        self.type = 1
        
        token = 'CWB-A69F077C-C940-4912-9FC2-99F44AA41A25'  # 授權碼
        # 需要的項目：溫度、濕度、今日最高溫、今日最低溫、最高溫時間、最低溫時間、小時最大風速、最大風速時間
        required_item = 'TEMP,HUMD,D_TX,D_TN,D_TXT,D_TNT'

        # 搜尋的網址：回傳JSON (DONE)
        url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=' + token + '&format=JSON&locationName=' + str(
            self.__city) + '&elementName=' + required_item
        Data = requests.get(url)
        
        # 嘗試判斷是否是無人測站(None = 是!)
        re_complete_work1 = re.compile(
            'location":\[\]')
        complete_work1 = re_complete_work1.search(str(Data.text))
        if(complete_work1 != None):
            url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=' + token + '&format=JSON&locationName=' + str(
            self.__city) + '&elementName=' + required_item
            Data = requests.get(url)
            self.type = 2

        print("TYPE:", self.type)
        self.__dataText = Data.text

    def reTEMP(self):
        # 以下正規表示法取出數值
        re_complete_temp = re.compile(
            '(TEMP)\W+(elementValue)\W+[0-9]+\W[0-9]')
        complete_temp = re_complete_temp.search(str(self.__dataText))
        
        if complete_temp == None:
            re_complete_temp = re.compile(
            '(TEMP)\W+(elementValue)\W+[0-9]+')
            complete_temp = re_complete_temp.search(str(self.__dataText))
            try:
                self.__temp = float(complete_temp.group()[-2:])
            except:
                self.__temp = -1
        else:
            try:
                self.__temp = float(complete_temp.group()[-4:])
            except:
                self.__temp = -1

        return self.__temp

    def reHUMD(self):
        # 以下正規表示法取出數值
        re_complete_humd = re.compile(
                '(HUMD)\W+(elementValue)\W+[0-9]\W[0-9]+')
        complete_humd = re_complete_humd.search(str(self.__dataText))
        
        # 若不剛好等於 1
        if complete_humd == None:
            re_complete_humd = re.compile('(HUMD)\W+(elementValue)\W+[0-9]')
            complete_humd = re_complete_humd.search(str(self.__dataText))
            try:
                self.__humd = float(complete_humd.group()[-1])
            except:
                self.__humd = -1
        else:
            try:
                try:
                    self.__humd = float(complete_humd.group()[-4:])
                except:
                    self.__humd = float(complete_humd.group()[-3:])
            except:
                self.__humd = -1
            

        return self.__humd

    def reD_TX(self):
        # 以下正規表示法取出數值
        re_complete_DTX = re.compile(
            '(D_TX)\W+(elementValue)\W+[0-9]+\W[0-9]+')
        complete_DTX = re_complete_DTX.search(str(self.__dataText))
        
        try:
             self.__d_tx = float(complete_DTX.group()[-5:])
        except:
            self.__d_tx = -1

        return self.__d_tx

    def reD_TN(self):
        # 以下正規表示法取出數值
        re_complete_DTN = re.compile(
            '(D_TN)\W+(elementValue)\W+[0-9]+\W[0-9]+')
        complete_DTN = re_complete_DTN.search(str(self.__dataText))
       
        try:
             self.__d_tn = float(complete_DTN.group()[-5:])
        except:
            self.__d_tn = -1

        return self.__d_tn

    def reD_TXT(self):
        # 以下正規表示法取出數值
        if(self.type == 1):
            re_complete_DTXT = re.compile('(D_TXT)\W+(elementValue)\S{19}')
        elif(self.type == 2):
            re_complete_DTXT = re.compile('D_TXT"\W+\w+\W+\d{4}')
            
        complete_dtxt = re_complete_DTXT.search(str(self.__dataText))
        
        try:
            if(self.type == 1):
                self.__d_txt = str(complete_dtxt.group()[-5:])
            elif(self.type == 2):
                self.__d_txt = str(complete_dtxt.group()[-4:-2] + ":" +  complete_dtxt.group()[-2:])
        except:
            self.__d_txt = -1

        return self.__d_txt

    def reD_TNT(self):
        # 以下正規表示法取出數值
        if(self.type == 1):
            re_complete_DTNT = re.compile('(D_TNT)\W+(elementValue)\S{19}')
        elif(self.type == 2):
            re_complete_DTNT = re.compile('D_TNT"\W+\w+\W+\d{4}')
        complete_dtnt = re_complete_DTNT.search(str(self.__dataText))
      
        try: 
            if(self.type == 1):
                self.__d_tnt = str(complete_dtnt.group()[-5:])
            elif(self.type == 2):
                self.__d_tnt = str(complete_dtnt.group()[-4:-2] + ":" +  complete_dtnt.group()[-2:])
        except:
            self.__d_tnt = -1

        return self.__d_tnt

     # 獲得天氣資訊：溫度、濕度、最高溫、最低溫

    def getWeather(self):
              
        try:
            self.dataText_AutoRefresh()
            # 更新所有溫度資訊
            self.reTEMP()
            self.reHUMD()
            self.reD_TX()
            self.reD_TN()
            self.reD_TXT()
            self.reD_TNT()

            # 回傳溫度溫度、濕度、最高溫、最低溫、最高溫時間點、最低溫時間點
            return (self.__temp, self.__humd, self.__d_tx, self.__d_tn, self.__d_txt, self.__d_tnt)
        except:
            return "此站未提供天氣資訊"

    def printWeather(self):

        # 利用“正規化“只截取想要的資訊
        print("TEMP:", self.reTEMP())
        print("HUMD:", self.reHUMD())
        print("D_TX:", self.reD_TX())
        print("D_TN:", self.reD_TN())
        print("D_TXT:", self.reD_TXT())
        print("D_TNT:", self.reD_TNT())


'''
建立天氣物件

變數包含:
城市: city
weather API 內的所有資料:dataText
temp: 溫度
humd: 濕度
d_tx: 本日最高溫
d_tn: 本日最低溫
d_txt: 本日最高溫之時間
d_tnt: 本日最低溫之時間
# h_fx: 小時最大陣風風速, 單位 公尺/秒
# h_fxt: 小時最大陣風時間, hhmm (小時分鐘)

方法包含:
刷新網址:dataText_AutoRefresh(!! 註: 每次使用都要刷新) 
獲得溫度:reTEMP(溫度, 單位:攝氏)
獲得濕度:reHUMD(濕度, 單位:百分率)
獲得本日最高溫:reD_TX(本日最高溫, 單位:攝氏)
獲得本日最低溫:reD_TN(本日最低溫, 單位:攝氏)
獲得本日最高溫之時間: reD_TXT(本日最高溫發生時間, hhmm (小時分鐘))
獲得本日最低溫之時間: reD_TNT(本日最低溫發生時間, hhmm (小時分鐘))
獲得所有天氣資訊:getWeather(溫度、濕度、最高溫、最低溫、最高溫時間段、最低溫時間段) (!! 註:不需要使用 dataText_AutoRefresh )
輸出所有天氣資訊:printWeather(溫度、濕度、最高溫、最低溫、最高溫時間段、最低溫時間段)
'''
