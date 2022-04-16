import eel
from Algorithm_with_SQL.weather import weather_information_API

@eel.expose
def weather_to_js():    # 傳送天氣資訊
  
  we = weather_information_API("埔心") # 地點
  weather_list = we.getWeather() # 獲得陣列(6個資訊)
  print("weather_list", weather_list)
  
  # 以下轉換成 JSON格式的字串
  weather_json = ""
  weather_json += '{"temp":'   + str(weather_list[0])
  weather_json += ',"humd":'   + str(weather_list[1])
  weather_json += ',"d_tx":'   + str(weather_list[2])
  weather_json += ',"d_tn":'   + str(weather_list[3])
  weather_json += ',"d_txt":"' + str(weather_list[4]) + '"'
  weather_json += ',"d_tnt":"' + str(weather_list[5])  + '"}'

  return weather_json

eel.init('UI/web') # eel.init(網頁的資料夾)
eel.start('main.html',size = (600,400)) #eel.start(html名稱, size=(起始大小))
