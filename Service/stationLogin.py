import sys, os
sys.path.append(os.getcwd()) # 抓取路徑

import matplotlib.pyplot as plt
import time

from stationCRUD import stationCRUD


stCrud = stationCRUD()
print(stCrud.queryCityByName('臺北市'))

##