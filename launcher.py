import eel
from Algorithm_with_SQL.weather import weather_information_API
from crawler.crawler import station

@eel.expose
def weather_to_js(weatherPostion):    # 傳送天氣資訊
  
  we = weather_information_API(weatherPostion) # 地點
  weather_list = we.getWeather() # 獲得陣列(6個資訊)
  print("weather_list: ", weather_list)
  print("weather_position: ", weatherPostion)
  
  # 以下轉換成 JSON格式的字串
  weather_json = ""
  weather_json += '{"temp":'   + str(weather_list[0])
  weather_json += ',"humd":'   + str(weather_list[1])
  weather_json += ',"d_tx":'   + str(weather_list[2])
  weather_json += ',"d_tn":'   + str(weather_list[3])
  weather_json += ',"d_txt":"' + str(weather_list[4]) + '"'
  weather_json += ',"d_tnt":"' + str(weather_list[5])  + '"}'

  return weather_json


@eel.expose
def station_city_to_js(): # 傳送所有縣市資訊
  
  st_all_city = station().getAllCity()
  str_city = ""
  
  for index in range(len(st_all_city)):
    if(index != 0): 
      str_city += ","
    str_city += str(st_all_city[index])
    
  print("city: ", str_city)
  return str(str_city)

@eel.expose
def station_station_to_js(city):
  
  st_station_in_city = station().getStationByCity(city)
  str_station = ""
  
  for index in range(len(st_station_in_city)):
    if(index != 0): 
      str_station += ","
    str_station += str(st_station_in_city[index])
    
  print("station: ", str_station)
  return str(str_station)

eel.init('UI/web') # eel.init(網頁的資料夾)
eel.start('main.html',size=(1920,1080)) #eel.start(html名稱, size=(起始大小))
