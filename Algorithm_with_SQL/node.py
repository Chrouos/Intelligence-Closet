

from unittest import case


class recommend_node:

    # 初始化：位置、分類、顏色、種類、使用次數、創建時間、儲存位置
    def __init__(self, position, category, color, type, usageCounter, createTime, photoPosition):
        self.position = position  # 面對存儲的位置（1, 2, 3, ...)
        self.category = category  # (upper, lower, other, outerwear）
        self.color = color  # 衣物的顏色
        self.type = type  # 衣物的種類
        # self.weather_score = 0  # 每日都會變更，利用function 抓取 中央氣象局 API 分數分數
        self.usageCounter = usageCounter  # 使用次數
        self.createTime = createTime  # 創建時間
        self.photoPosition = photoPosition

        # self.style = style # 衣物的風格

    def refresh_WS(self):

        # 上半身
        if self.category == 'upper':
            if self.type == 'short_TShirt':
                return 1
            elif self.type == 'long_sleeves':
                return 2
            elif self.type == 'sweater':
                return 2

        # 下半身
        elif self.category == 'lower':
            if self.type == 'short_pants':
                return 1
            elif self.type == 'long_skirt':
                return 2
            elif self.type == 'long_pants':
                return 3
            elif self.type == 'short_skirt':
                return 1

        # 其他
        elif self.category == 'coat':
            if self.type == 'thick_coat':
                return 5
            elif self.type == 'down_coat':
                return 9
            elif self.type == 'thin_coat':
                return 3


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
