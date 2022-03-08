

class recommend_node:

    # 初始化：位置、分類、天氣、天氣分數
    def __init__(self, position, category, color, type, usageCounter , createTime, position):
        self.position = position  # 面對存儲的位置（1, 2, 3, ...)
        self.category = category  # (upper, lower）
        self.color = color  # 衣物的顏色
        self.type = type  # 衣物的種類
        self.weather_score = 0  # 每日都會變更，利用function 抓取 中央氣象局 API 分數分數
        self.usageCounter = usageCounter # 使用次數
        self.createTime = createTime # 創建時間
        
        self.photoPosition = position
        self.__comfortableTemp = 26 # 人體最適溫度
        
        # self.style = style # 衣物的風格
              
    def refresh_WS(self, weather_info):
        # weather_info 包含溫度、濕度、最高溫、最低溫、最高溫時間段、最低溫時間段
        
        
        
        return 0
        
    def setComfortableTemp(self, newTemp):
        self.__comfortableTemp = newTemp
          
     


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
2. 長袖(2): long_TShirt
3. 毛衣(3): sweater


下:
1. 短褲(1): short_pants
2. 長裙(2): long_skirt
3. 長褲(3): long_pants
4. 短裙(0.5): short_skirt

其他1:
1. 外套(5): coat
2. 羽絨衣(8): downCoat

其他2:
1. 發熱衣服(3): thermals
2. 圍巾(4): muffler

'''
