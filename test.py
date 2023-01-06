import sys, os

sys.dont_write_bytecode = True  # 不產生 pyc
sys.path.append(os.getcwd())  # 抓取路徑

# from Service.ClothesNodeService import ClothesNodeService
# clothesNodeService = ClothesNodeService()
# print(clothesNodeService.vacancyPosition())

# from Service.userDashboardService import UserDashboardService
# userDashboardService = UserDashboardService()
# user_dict = userDashboardService.queryById(1)  # 預設為1
# print(user_dict['LastPosition'])

# -----------------------  硬體控制
from Controller.arduinoController import ArduinoController
arduinoController = ArduinoController()
arduinoController.car_back_now()
# arduinoController.car_front_now()

# arduinoController.storgage_first_half()
# arduinoController.Test_get()
# arduinoController.storgage_first_half()
# arduinoController.pickUp_one_clothes(1)


# from Controller.clothesGraphController import ClothesGraphController
# clothesGraphController = ClothesGraphController(204)
# clothesGraphController.getCombination()
# clothesGraphController.printEdge()

# from Controller.weatherAPI import WeatherAPI
# we = WeatherAPI(12)
# we.getDataText()
# we.getWeather()
# we.print_dataText()


# from Controller.camaraController import CamaraController
# import joblib
# # 相機物件
# def get_x(r): return './images_original/'+r['image'] # create path to open images in the original folder
# def get_y(r): return r['label'].split(' ') # split the labels using space as a delimitter
# # 讀取圖檔
# clf = joblib.load('Controller/joblib_export.pkl')
# camaraController = CamaraController(1, clf)
# camaraController.useCamara()
# camaraController.identifyCategory()
# camaraController.identifyColor()
# camaraController.printResult()
# camaraController.saveToSql()


# --------------------------- 換位子
# from Service.userDashboardService import UserDashboardService   
# userDashboardService = UserDashboardService()
# user_dict = userDashboardService.queryById(1)  # 預設為1
# user_dict['LastPosition'] = 1

# for position in range(1, 9, 1):
#     dist_roundTimes = 8
#     if position != user_dict['LastPosition']:
#         dist_roundTimes = (position - user_dict['LastPosition']) * 3 % 8
#     print( "user last position:", user_dict['LastPosition'], ", go to position:", position, ", 要轉動的次數", dist_roundTimes)

