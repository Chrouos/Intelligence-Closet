import sys, os
sys.dont_write_bytecode = True  # 不產生 pyc
sys.path.append(os.getcwd())  # 抓取路徑


from Controller.arduinoController import ArduinoController

arduinoController = ArduinoController()
arduinoController.storage()