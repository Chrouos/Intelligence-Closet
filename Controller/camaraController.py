# Identify: 將相機和辨識衣物做成物件

import collections
import os
import sys
from unicodedata import category

import cv2
import numpy as np
import tensorflow as tf
from keras_preprocessing import image
import time

from Service.colorService import ColorService
from Service.ClothesNodeService import ClothesNodeService
from Service.ClothesNodeUpperService import ClothesNodeUpperService
from Service.ClothesNodeLowerService import ClothesNodeLowerService
from Service.ClothesNodeOtherService import ClothesNodeOtherService
from Service.nodeGraphService import NodeGraphService

from Service.viewClothesNodeService import ViewClothesNodeService

from Service.subCategoryService import SubCategoryService

sys.path.append(os.getcwd())  # 抓取路徑


class CamaraController:

    def __init__(self, camara):
        self.newOneId = -1  # 抓取資料庫最後一位

        self.getLastId()
        self.color = ''
        self.category = ''
        self.isFavorite = 0

        self.path = ""

        self.chooseCamara = camara

    def getLastId(self):
        clothesNodeService = ViewClothesNodeService()

        self.newOneId = clothesNodeService.lastId() + 1
        self.save_path = 'View/mui/public/src/clothes_' + str(
            self.newOneId) + '.jpg'
        self.path = "./public/src/clothes_" + str(self.newOneId) + ".jpg"

        return self.newOneId

    def saveToSql(self):

        # 呼叫Service
        subCategoryService = SubCategoryService()
        colorService = ColorService()

        #獲得必要資訊
        colorId = colorService.queryIdByEngName(self.color)
        subcategory = subCategoryService.queryIdAndCategoryByClothesType(
            self.category)
        subCategoryId = subcategory[0]
        categoryId = subcategory[1]

        clothesNode_create = '{{"SubCategoryId": {0}, "ColorId": {1}, "FilePosition": "{2}", "IsFavorite": {3}}}'.format(
            subCategoryId, colorId, self.path, self.isFavorite)
        print("saveData:", clothesNode_create)

        clothesNodeService = ClothesNodeService()
        clothesNodeService.create(clothesNode_create)

        # if categoryId == 1:
        #     clothesNodeService = ClothesNodeUpperService()
        #     clothesNodeService.create(clothesNode_create)
        # elif categoryId == 2:
        #     clothesNodeService = ClothesNodeLowerService()
        #     clothesNodeService.create(clothesNode_create)
        # else:
        #     clothesNodeService = ClothesNodeOtherService()
        #     clothesNodeService.create(clothesNode_create)

        return True

    def printResult(self):
        print(" ---------- identify result ----------")
        print("ID: {0}, path: {1}".format(self.newOneId, self.save_path))
        print("color: {0}, category: {1}, path: {2}".format(
            self.color, self.category, self.path))
        print(" ---------- identify result ----------")

    def useCamara(self):
        cap = cv2.VideoCapture(self.chooseCamara)  # 開啟攝像頭
        countDown = 1
        while True:
            ret, frame = cap.read()  # 讀取鏡頭畫面
            cv2.imshow("capture", frame)  # 生成攝像頭視窗
            countDown = countDown - 0.1
            if cv2.waitKey(1) & 0xFF == ord(
                    'q') or countDown <= 0:  # 如果按下q 就截圖儲存並退出

                outputSize = cv2.resize(frame,
                                        (480, 640))  # to resize the image
                # cv2.imwrite(self.save_path, outputSize)

                cap.release()
                cv2.destroyAllWindows()  # 關閉視窗
                # print("save: ", self.save_path)

                break

    def identifyCategory(self):
        cls_list = [
            'Blazer', '', 'Body', 'Dress', 'Hat', 'Hoodie', 'Longsleeve',
            'Not_sure', '', 'Outwear', 'Pants', 'Polo', 'Shirt', 'Shoes',
            'Shorts', '', 'Skirt', 'T-Shirt', '', 'Undershirt'
        ]

        # 關閉GPU加速功能(建議安裝無GPU版本，縮短初始化時間)
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

        # 開啟800字典
        words_path = './Controller/classify/archive/images.csv'
        file1 = open(words_path, 'rt', encoding='Big5')
        labels = list(file1.read())
        file1.close()

        # 載入模型
        model = tf.compat.v1.keras.models.load_model(
            './Controller/classify/h5/training_model.h5')

        cls_list = [
            'Blazer(x)', 'Blouse', 'Body', 'Dress', 'Hat', 'Hoodie',
            'Longsleeve', 'Not_sure', 'Other', 'Outwear', 'Pants', 'Polo',
            'Shirt', 'Shoes', 'Shorts', 'Skip', 'Skirt', 'T-Shirt', 'Top',
            'Undershirt'
        ]

        try:
            img = image.load_img(self.save_path, target_size=(224, 224))
        except Exception as e:
            print(self.save_path, e)

        # 圖檔預處理
        img = np.expand_dims(img, axis=0)  # 轉換通道
        img = img / 255  # rescale

        pred = model.predict(img)[0]  # 計算機率與預測結果
        #print(pred) # 機率list
        index = np.argmax(pred)
        prediction = cls_list[index]

        self.category = prediction

        return self.category
        # print("CATEGORY: ", self.category)

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
            cv2.imwrite('./Controller/classify/colorTmpFolder/' + d + '.jpg',
                        mask)
            binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
            binary = cv2.dilate(binary, None, iterations=2)
            cnts, hiera = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_SIMPLE)
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

        #黑色
        lower_black = np.array([0, 0, 0])
        upper_black = np.array([250, 255, 30])
        color_list = []
        color_list.append(lower_black)
        color_list.append(upper_black)
        dict['BLACK'] = color_list

        #灰色
        lower_gray = np.array([0, 0, 46])
        upper_gray = np.array([180, 43, 220])
        color_list = []
        color_list.append(lower_gray)
        color_list.append(upper_gray)
        dict['GRAY'] = color_list

        #白色
        # lower_white = np.array([0, 0, 221])
        # upper_white = np.array([180, 30, 255])
        # color_list = []
        # color_list.append(lower_white)
        # color_list.append(upper_white)
        # dict['WHITE'] = color_list

        #紅色
        lower_red = np.array([0, 150, 50])
        upper_red = np.array([10, 255, 255])
        color_list = []
        color_list.append(lower_red)
        color_list.append(upper_red)
        dict['RED'] = color_list

        #粉紅色
        lower_pink = np.array([156, 43, 46])
        upper_pink = np.array([180, 255, 255])
        color_list = []
        color_list.append(lower_pink)
        color_list.append(upper_pink)
        dict['PINK'] = color_list

        #橘色
        lower_orange = np.array([15, 150, 0])
        upper_orange = np.array([25, 255, 255])
        color_list = []
        color_list.append(lower_orange)
        color_list.append(upper_orange)
        dict['ORANGE'] = color_list

        #黃色
        lower_yellow = np.array([26, 43, 46])
        upper_yellow = np.array([34, 255, 255])
        color_list = []
        color_list.append(lower_yellow)
        color_list.append(upper_yellow)
        dict['YELLOW'] = color_list

        #綠色
        lower_green = np.array([45, 150, 54])
        upper_green = np.array([65, 255, 255])
        color_list = []
        color_list.append(lower_green)
        color_list.append(upper_green)
        dict['GREEN'] = color_list

        #青色
        lower_cyan = np.array([78, 43, 46])
        upper_cyan = np.array([99, 255, 255])
        color_list = []
        color_list.append(lower_cyan)
        color_list.append(upper_cyan)
        dict['CYAN'] = color_list

        #藍色
        lower_blue = np.array([100, 43, 46])
        upper_blue = np.array([124, 255, 255])
        color_list = []
        color_list.append(lower_blue)
        color_list.append(upper_blue)
        dict['BLUE'] = color_list

        #紫色
        lower_purple = np.array([125, 43, 46])
        upper_purple = np.array([155, 255, 255])
        color_list = []
        color_list.append(lower_purple)
        color_list.append(upper_purple)
        dict['PURPLE'] = color_list

        return dict

    # https://www.twblogs.net/a/5c36d389bd9eee35b21d46e3
    # https://blog.csdn.net/ruoshui_t/article/details/109310806

    # https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv

    # https://stackoverflow.com/questions/47483951/how-to-define-a-threshold-value-to-detect-only-green-colour-objects-in-an-image/47483966#47483966