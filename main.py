from Alogritme_with_SQL.weather import weather_information_API
from crawler.crawler import station

station = station()
for city in station.allCity:
    print(city)


enterCity = input(str("Please input you want to search: "))
print(station.getStationByCity(enterCity))
