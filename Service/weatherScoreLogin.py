import sys, os
sys.path.append(os.getcwd()) # 抓取路徑
from weatherScoreCRUD import weatherScoreCRUD

wsCrud = weatherScoreCRUD()
print("1. 輸入clothesType獲得CategoryId: " , wsCrud.queryByClothesTypeCategoryId('Blazer'))

print("2. 輸入clothesType獲得Id: " , wsCrud.queryByClothesTypeWSId('Blazer'))