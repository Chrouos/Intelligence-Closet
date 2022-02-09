from Weather import weather_information_API # 獲得天氣資訊 API
from Node import recommend_node
from Graph import recommend_Graph


weather = weather_information_API("天母")

print(weather.getWeather())