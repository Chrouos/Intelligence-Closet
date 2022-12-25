import sys, os
sys.dont_write_bytecode = True  # 不產生 pyc
sys.path.append(os.getcwd())  # 抓取路徑

# from Service.ClothesNodeService import ClothesNodeService
# clothesNodeService = ClothesNodeService()
# print(clothesNodeService.vacancyPosition())

# from Controller.arduinoController import ArduinoController
# arduinoController = ArduinoController()
# arduinoController.Test_get()
# arduinoController.storgage_first_half()
# arduinoController.pickUp_one_clothes(1)


# from Controller.clothesGraphController import ClothesGraphController
# clothesGraphController = ClothesGraphController(1)
# clothesGraphController.printEdge()
# clothesGraphController.getCombination()

# from Controller.weatherAPI import WeatherAPI
# we = WeatherAPI(12)
# we.getDataText()
# we.getWeather()
# we.printWeather()