import pyodbc
import pandas as pd

from nodeCRUD import nodeCRUD

crud = nodeCRUD()

############### 操作手冊 ###############

# 1. 插入檔案(全新檔案: 使用次數預設為0)
crud.insertData('upper', 'blue', 'long_Tshirt', 'E:\ProgrammingLanguage\git\Intelligence-Closet')

# 2. 搜尋全部的資料(會獲得一份陣列data資料): by v_clothes_information(原因資料更完善)
print("2-1. clothes_information 資料")
for i in crud.queryData():
  print(i)
  
print("2-2. v_clothes_information 資料")
for i in crud.queryViewData():
  print(i)

# 3. 透過位置找尋資料
print("3. 位置5的資料: \n", crud.queryDataByPosition(5))

# 4. 透過分類找尋資料
print("4. 透過分類找尋資料 ex. upper")
for i in crud.queryDataByCategory('upper'):
  print(i)

# 5. Sort
print("5-1. 大到小分類: name 想找尋的分類")
for i in crud.sortNameDESC("Position"):
  print(i)
  
print("5-2. 小到大分類: name 想找尋的分類")
for i in crud.sortNameASC("Position"):
  print(i)

# 6. 空缺的位置資訊(範圍 0~9 )
print("6. 空缺的位置資訊(範圍 0~9:", crud.vacancyPosition()) ## -1 代表位置已滿

# 7. 最後一個位置
print("7.最後一個位置", crud.lastPosition())

# 8. 讓位置變成0 (預設是拿取衣物後)
crud.updatePositionToNull(0)

# 9. 刪除
crud.deleteByPosition(1)
