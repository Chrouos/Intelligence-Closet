# all station url: https://e-service.cwb.gov.tw/wdps/obs/state.htm
import requests
from bs4 import BeautifulSoup


class station:

    # 利用爬蟲獲得所有城市和站名：allCity, allStation
    def __init__(self):
        self.allCity = []  # 所有城市
        self.allStation = []  # 所有站名
        self.allInformation = [] # 所有資訊 (0.站號, 1.站名, 2.城市, 3.地址, 4.資料起始資料, 5.備註) 

    def getAllCity(self):
        return self.allCity

    def getAllStation(self):
        return self.allStation
    
    def getAllInformation(self):
        return self.allInformation

    def getStationByCity(self, city):
        print('getStationByCity: ', city);
        try:
            index = self.allCity.index(city)
            return self.allStation[index]
        except:
            return False
        
    def refreshDataByNet(self):
        # Basic information
        url = "https://e-service.cwb.gov.tw/wdps/obs/state.htm"  # 現存測站網站 url
        
        # 假資訊，仿造真實使用者進入的感覺
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36'}

        # 開爬
        try:
            response = requests.get(url, headers=headers, timeout=(1, 7))  # timeout => 避免載入過久
            response.encoding = 'utf8'  # use UTF-8
            soup = BeautifulSoup(response.text, "html.parser")
            # print(soup.prettify()) # 輸出排版後的資訊
        except:
            print("Error")

        # 搜尋指定資料
        div_existing_station = soup.find('div', id='existing_station')
        div_tr = div_existing_station.find_all('tr')  # limit = 10
        
        # 擷取 tr 中
        for tr in div_tr:
            try:
                td = tr.find_all('td')
                
                # 0.站號 1.站名 2.城市 3.地址 4.資料起始日期 5.備註
                currentData = [td[0].text, td[1].text, td[5].text, td[6].text, td[7].text, td[9].text]
                self.allInformation.append(currentData)
                
                # 把所有縣市放入 allCity
                if td[5].text not in self.allCity:  # 若沒有此縣市 新增！
                    self.allCity.append(td[5].text)
                    self.allStation.append([])
                self.allStation[self.allCity.index(td[5].text)].append(td[1].text)  # 把所有站名放到對應的城市編號（ex. 新北為０、台北為１）
            except:
                td = tr.find_all('th')
        


'''
station
變數
allCity: 所有城市
allStation: 所有城市中的站名

getStationByCity: 利用城市的名稱找所有站名

'''
