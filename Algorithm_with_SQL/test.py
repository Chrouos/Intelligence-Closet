from weather import weather_information_API



weather = weather_information_API('五股')
print(weather.getWeather())

weather = weather_information_API('埔心')
print(weather.getWeather())
