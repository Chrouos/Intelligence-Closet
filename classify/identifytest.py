import sys, os
sys.path.append(os.getcwd()) # 抓取路徑

from Identify import identify

# 輸入內容為圖片編碼
identify = identify(2)

identify.identifyCategory(); 
identify.identifyColor();
identify.printResult();
    