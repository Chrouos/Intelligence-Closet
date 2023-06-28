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
# from Service.ClothesNodeService import ClothesNodeService 
# clothesNodeService = ClothesNodeService()
# print(clothesNodeService.vacancyPosition()) 


# ----------------------- Arduino Controller ----------------------- #
# from Controller.arduinoController import ArduinoController
# arduinoController = ArduinoController() 
# arduinoController.returnCraneZero()

# 拿取 
# arduinoController.takeTheClothes_single(1)
# arduinoController.takeTheClothes_second(6)
# arduinoController.put_EntranceMidPositionZero_second(1)   
# arduinoController.put_EntranceMidPositionZero(2)

# 存放
# arduinoController.takeTheClothes_single(7)
# arduinoController.entranceToZero()
# arduinoController.put_ZeroPositionZero(7)


# ----------------------- Camara Controller ----------------------- #
# from Controller.camaraController import *
# # 相機物件
# def get_x(r): return './images_original/'+r['image'] # create path to open images in the original folder
# def get_y(r): return r['label'].split(' ') # split the labels using space as a delimitter
# # 讀取圖檔
# clf = joblib.load('Controller/joblib_export.pkl')
# idt = CamaraController(0, clf)  # 選擇攝像頭

# idt.useCamara()          


