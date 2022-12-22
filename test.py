import sys, os
sys.dont_write_bytecode = True  # 不產生 pyc
sys.path.append(os.getcwd())  # 抓取路徑


# from Controller.arduinoController import ArduinoController
# arduinoController = ArduinoController()
# arduinoController.storgage_first_half()


from Controller.clothesGraphController import ClothesGraphController
clothesGraphController = ClothesGraphController(1)
clothesGraphController.printEdge()
clothesGraphController.getCombination()

# from Controller.weatherAPI import WeatherAPI
# we = WeatherAPI(12)
# we.getDataText()
# we.getWeather()
# we.printWeather()