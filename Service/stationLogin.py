import sys, os
sys.path.append(os.getcwd()) # 抓取路徑

import matplotlib.pyplot as plt
import time

from stationCRUD import stationCRUD
from crawler.crawler import station

timeRange = []
for i in range(20):
  timeRange.append(i)

stTime = []
for i in range(20):
  stStartTime = time.time()
  st = station()
  st.refreshDataByNet()
  stEndTime = time.time()
  stTime.append(stEndTime - stStartTime)


#############################

crudTime = []
for i in range(20):
  crudStartTime = time.time()
  stCrud = stationCRUD()
  crudEndTime = time.time()
  crudTime.append(crudEndTime - crudStartTime)
  
print(timeRange)
print("----")
print(stTime)
print("----")
print(crudTime)

plt.plot(timeRange, stTime, color=(255/255,100/255,100/255))
plt.plot(timeRange,crudTime, '--', color=(100/255,100/255,255/255))
plt.show()