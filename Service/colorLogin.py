
from colorCRUD import colorCRUD

graphCRUD = colorCRUD()

print("1. 搜尋全部顏色相關:\n", graphCRUD.queryAll())

print("2. 搜尋ID 關鍵字顏色英文名稱:\n", graphCRUD.queryIdByEngName('BLACK'))

