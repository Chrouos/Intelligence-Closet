import sys, os

sys.dont_write_bytecode = True  # 不產生 pyc
sys.path.append(os.getcwd())  # 抓取路徑

# ----------------------- 測試 JSON ----------------------- #
# import json
# from json import load
# jsonFile = open('./setting.json','r')
# settingJson = json.load(jsonFile)
# print(settingJson['real_closet_space'])


# ----------------------- ClothesNode Service ----------------------- #
from Service.ClothesNodeService import ClothesNodeService 
clothesNodeService = ClothesNodeService()
clothesNodeService
# print(clothesNodeService.vacancyPosition()) 


# ----------------------- Arduino Controller ----------------------- #
# from Controller.arduinoController import ArduinoController
# arduinoController = ArduinoController() 
# arduinoController.returnCraneZero()
# arduinoController.putClothes(1)
# 拿取 
# arduinoController.takeClothes_single(2)
# arduinoController.put_EntrancePositionZero(2)
# 存放
# arduinoController.takeClothes_single(2)
# arduinoController.entranceToZero()
# arduinoController.put_ZeroPositionZero(1)

