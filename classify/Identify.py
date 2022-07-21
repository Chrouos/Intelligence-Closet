
# Identify: 將相機和辨識衣物做成物件

import sys, os
import cv2

from Service.nodeCRUD import nodeCRUD
from Service.weatherScoreCRUD import weatherScoreCRUD
from Service.graphCRUD import graphCRUD
from Service.colorCRUD import colorCRUD

sys.path.append(os.getcwd()) # 抓取路徑
wsCrud = weatherScoreCRUD()
gCrud = graphCRUD()
colorCrud = colorCRUD();

cap = cv2.VideoCapture(0)  # 開啟攝像頭


class identify:
  
  def __init__(self):
    self.nCrud = nodeCRUD()
    self.lastId = self.nCrud.queryIdCount() + 1; # 抓取資料庫最後一位
    
    self.save_path = 'UI/web/public/src/clothes_'+ str(self.lastId) +'.jpg' # 儲存的位置
    
  
  def identifyColor(self):
    ret, frame = cap.read() # 讀取鏡頭畫面
    
    