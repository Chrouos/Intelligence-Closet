# Identify: 將相機和辨識衣物做成物件

import collections
import os
import sys

import cv2
import numpy as np
import tensorflow as tf
from keras_preprocessing import image

from Service.colorCRUD import colorCRUD
from Service.nodeCRUD import nodeCRUD
from Service.weatherScoreCRUD import weatherScoreCRUD

cap = cv2.VideoCapture(0)  # 開啟攝像頭
sys.path.append(os.getcwd())  # 抓取路徑


class identify:

    def __init__(self):
        self.lastId = -1  # 抓取資料庫最後一位
        self.save_path = 'UI/web/public/src/clothes_' + str(self.lastId) + '.jpg'  # 儲存的位置
        self.color = ''
        self.category = ''

    def getLastId(self):
        nCrud = nodeCRUD()
        self.lastId = nCrud.queryIdCount() + 1
        self.save_path = 'UI/web/public/src/clothes_' + str(self.lastId) + '.jpg'

        return self.lastId

    def saveToSql(self):

            
        print("SAVE TO SQL: ")
        wsCrud = weatherScoreCRUD()
        colorCrud = colorCRUD()
        nCrud = nodeCRUD()

        colorId = colorCrud.queryIdByEngName(self.color)
        weatherScoreId = wsCrud.queryByClothesTypeWSId(self.category)
        print(colorId, weatherScoreId, self.save_path)

        return nCrud.insertData(colorId, weatherScoreId, self.save_path)


    def printResult(self):
        print(" ---------- identify result ----------")
        print("ID: {0}, path: {1}".format(self.lastId, self.save_path))
        print("color: {0}, category: {1}".format(self.color, self.category))
        print(" ---------- identify result ----------")

    def useCamara(self):
        ret, frame = cap.read()  # 讀取鏡頭畫面
        cv2.imshow("capture", frame)  # 生成攝像頭視窗
        cv2.imwrite(self.save_path, frame)
        print("save: ", self.save_path)

    def identifyCategory(self):
        cls_list = ['Blazer', '', 'Body', 'Dress,Top',
                    'Hat', 'Hoodie', 'Longsleeve', 'Not_sure', '',
                    'Outwear', 'Pants', 'Polo', 'Shirt', 'Shoes',
                    'Shorts', '', 'Skirt', 'T-Shirt', '',
                    'Undershirt']

        # 關閉GPU加速功能(建議安裝無GPU版本，縮短初始化時間)
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
        # 開啟800字典
        words_path = 'classify/archive/images.csv'
        file1 = open(words_path, 'rt', encoding='Big5')
        file1.close()

        model = tf.compat.v1.keras.models.load_model('classify/h5/eff_final.h5')
        try:
            img = image.load_img(self.save_path, target_size=(224, 224))
        except Exception as e:
            print(self.save_path, e)

        # 圖檔預處理
        img = np.expand_dims(img, axis=0)  # 轉換通道
        img = img / 255  # rescale

        pred = model.predict(img)[0]
        index = np.argmax(pred)
        prediction = cls_list[index]

        self.category = prediction
        # print("CATEGORY: ", self.category)
        
        cap.release()
        cv2.destroyAllWindows()  # 關閉視窗

    def identifyColor(self):
        frame = cv2.imread(self.save_path)

        self.color = self.getColor(frame)
        # print("COLOR: ", self.color)

        return self.color

    # 處理圖片
    def getColor(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maxsum = -100
        color = None
        color_dict = self.getColorList()
        for d in color_dict:
            mask = cv2.inRange(hsv, color_dict[d][0], color_dict[d][1])
            cv2.imwrite('./classify/images/tmp/' + d + '.jpg', mask)
            binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
            binary = cv2.dilate(binary, None, iterations=2)
            cnts, hiera = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            sum = 0
            for c in cnts:
                sum += cv2.contourArea(c)
            if sum > maxsum:
                maxsum = sum
                color = d

        return color

    # opencv計算機視覺庫函數處理
    def getColorList(self):
        # 定義字典存放顏色分量上下限
        # 例如：{顏色: [min分量, max分量]}
        # {'red': [array([160,  43,  46]), array([179, 255, 255])]}
        dict = collections.defaultdict(list)

        # 黑色
        lower_black = np.array([0, 0, 0])
        upper_black = np.array([180, 255, 46])
        color_list = []
        color_list.append(lower_black)
        color_list.append(upper_black)
        dict['black'] = color_list

        # #灰色
        lower_gray = np.array([0, 0, 46])
        upper_gray = np.array([180, 43, 220])
        color_list = []
        color_list.append(lower_gray)
        color_list.append(upper_gray)
        dict['gray'] = color_list

        # 白色
        lower_white = np.array([0, 0, 221])
        upper_white = np.array([180, 30, 255])
        color_list = []
        color_list.append(lower_white)
        color_list.append(upper_white)
        dict['white'] = color_list

        # 紅色
        lower_red = np.array([156, 43, 46])
        upper_red = np.array([180, 255, 255])
        color_list = []
        color_list.append(lower_red)
        color_list.append(upper_red)
        dict['red'] = color_list

        # 紅色2
        lower_red = np.array([0, 43, 46])
        upper_red = np.array([10, 255, 255])
        color_list = []
        color_list.append(lower_red)
        color_list.append(upper_red)
        dict['red2'] = color_list

        # 橙色
        lower_orange = np.array([11, 43, 46])
        upper_orange = np.array([25, 255, 255])
        color_list = []
        color_list.append(lower_orange)
        color_list.append(upper_orange)
        dict['orange'] = color_list

        # 黃色
        lower_yellow = np.array([26, 43, 46])
        upper_yellow = np.array([34, 255, 255])
        color_list = []
        color_list.append(lower_yellow)
        color_list.append(upper_yellow)
        dict['yellow'] = color_list

        # 綠色
        lower_green = np.array([35, 43, 46])
        upper_green = np.array([77, 255, 255])
        color_list = []
        color_list.append(lower_green)
        color_list.append(upper_green)
        dict['green'] = color_list

        # 青色
        lower_cyan = np.array([78, 43, 46])
        upper_cyan = np.array([99, 255, 255])
        color_list = []
        color_list.append(lower_cyan)
        color_list.append(upper_cyan)
        dict['cyan'] = color_list

        # 藍色
        lower_blue = np.array([100, 43, 46])
        upper_blue = np.array([124, 255, 255])
        color_list = []
        color_list.append(lower_blue)
        color_list.append(upper_blue)
        dict['blue'] = color_list

        # 紫色
        lower_purple = np.array([125, 43, 46])
        upper_purple = np.array([155, 255, 255])
        color_list = []
        color_list.append(lower_purple)
        color_list.append(upper_purple)
        dict['purple'] = color_list

        return dict
