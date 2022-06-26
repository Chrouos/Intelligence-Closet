import sys, os
sys.path.append(os.getcwd()) # 抓取路徑

from Service.nodeCRUD import nodeCRUD

class recommend_node:

    

    # 初始化：位置、分類、顏色、種類、使用次數、創建時間、儲存位置
    def __init__(self, position, ndCrud):
        self.position = position  # 面對存儲的位置（1, 2, 3, ...)

        self.data = ndCrud.queryDataByPosition(position)[0]
        
        self.clothesName = self.data[3] # 衣物名稱 (ex. 長裙、長褲)
        self.color = self.data[5] # 衣物的顏色
        self.userPreferences = self.data[6] # 使用者喜好程度
        self.categoryName = self.data[8] # 衣物分類
        self.clothesStyle = self.data[9]
        self.usageCounter = self.data[10]  # 使用次數
        self.createTime = self.data[11]
        self.modifytime = self.data[12]
        self.filePosition = self.data[13]
        self.weatherScore = self.data[14]
        self.level = self.data[15]

    def printNodeData(self):
        print("position:", self.position)
        print("clothesName:", self.clothesName)
        print("color:", self.color)
        print("userPreferences:", self.userPreferences)
        print("categoryName:", self.categoryName)
        print("clothesStyle:", self.clothesStyle)
        print("usageCounter:", self.usageCounter)
        print("createTime:", self.createTime)
        print("modifytime:", self.modifytime)
        print("filePosition:", self.filePosition)
        print("weatherScore:", self.weatherScore)
        print("level:", self.level)
        


'''
建立節點物件

變數包含:
位置: position
分類(上衣、下褲): category
天氣分數: weather_score
衣物的種類: type
(未來預定) 類型(運動、休閒等): style
方法包含:
刷新天氣分數:refresh_WS
'''

'''
衣物資料庫包含:
上:
1. 短袖(1): short_TShirt
2. 薄長袖(2): long_sleeves
3. 針織毛衣(2): sweater

上(可疊穿) outerwear:
1. 厚毛衣(5): thick_sweater
2. 帽T(4): cap_T

下:
1. 短褲(1): short_pants
2. 長裙(2): long_skirt
3. 長褲(3): long_pants
4. 短裙(0.5): short_skirt

其他1:
1. 厚外套(5): thick_coat
2. 羽絨衣(9): down_coat
3. 薄外套(3): thin_coat

其他2:
1. 發熱衣服(3): thermals
2. 圍巾(4): muffler

'''
