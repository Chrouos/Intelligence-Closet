import json
import os
import sys

import eel
sys.path.append(os.getcwd())  # 抓取路徑



eel.init('View/main')  # eel.init(網頁的資料夾)
eel.start('store.html', size=(1080, 720))  # eel.start(html名稱, size=(起始大小))
