class recommend_node:

    # 初始化：位置、分類、天氣、天氣分數
    def __init__(self, position, category, color):
        self.position = position  # 面對存儲的位置（1, 2, 3, ...)
        self.category = category  # 衣物的種類（top, down）
        self.color = color  # 衣物的顏色
        self.weather_score = 0  # 每日都會變更，利用function 抓取 中央氣象局 API 分數分數

    def refresh_WS(self, weather_info):
        # weather_info 包含溫度、濕度、最高溫、最低溫

        # 將分數清空
        self.weather_score = 0

        # 以溫度為判斷標準 (Not Done)
        temp = weather_info[0]


'''
建立節點物件

變數包含：
位置: position
分類（上衣、下褲）: category
天氣分數: weather_score
(未來預定) 類型（運動、休閒等）：Type
方法包含：
刷新天氣分數：refresh_WS
'''
