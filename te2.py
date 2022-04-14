# import os
# os.system("E:/ProgrammingLanguage/Envir/python376/python.exe launcher.py")
# input()


from Algorithm_with_SQL.weather import weather_information_API
from crawler.crawler import station
# import re

# st = station()
# print(st.getStationByCity("新北市"))

we = weather_information_API("桶後") # 地點
we.dataText_AutoRefresh()
print(we.getDataText())
print(we.getWeather()) # 獲得陣列(6個資訊)

