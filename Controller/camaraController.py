# Identify: 將相機和辨識衣物做成物件
import os
import sys

import cv2
import numpy as np

from fastai.vision.all import *
from fastai.vision.widgets import *

import pandas as pd
import joblib
import numpy as np
import cv2

from Service.colorService import ColorService
from Service.ClothesNodeService import ClothesNodeService
from Service.nodeGraphService import NodeGraphService
from Service.viewClothesNodeService import ViewClothesNodeService
from Service.subCategoryService import SubCategoryService

sys.path.append(os.getcwd())  # 抓取路徑



class CamaraController:

    def __init__(self, camara, clf):
        self.clf = clf

        self.color = ''         # 顏色(辨識項目)
        self.category = ''      # 子類別(辨識項目)
        self.isFavorite = 0     # 預設「是否收藏」 

        self.save_path = ""     # 全域端: 儲存的位置
        self.path = ""          # 資料庫: 儲存的位置
        
        self.newOneId = self.getLastId()        # 抓取資料庫的最後一筆Id, (並成為要命名的數字)
        self.chooseCamara = camara  # 選擇照相機

    def getLastId(self):
        clothesNodeService = ViewClothesNodeService()

        self.newOneId = clothesNodeService.lastId() + 1
        
        self.save_path = 'View/mui/public/src/clothes_' + str(self.newOneId) + '.jpg'
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
        print("saveClothesNode_Data:", clothesNode_create)

        clothesNodeService = ClothesNodeService()
        result = clothesNodeService.create(clothesNode_create)

        #新增clothesGraph
        if(result != False):
            clothesNode = clothesNodeService.queryAll()
            clothesNodeLastId = clothesNode[len(clothesNode)-1]["Id"]

            clothesGraph_create = '{{"ClothesNodeLastId": {0}, "CategoryId": {1}}}'.format(
                clothesNodeLastId, categoryId, self.path, self.isFavorite)
            # print("saveClothesGraph_Data:", clothesGraph_create)
            
            nodeGraphService = NodeGraphService()
            nodeGraphService.create(clothesGraph_create)

        return True

    def printResult(self):
        print(" ---------- identify result ----------")
        print("ID: {0}, path: {1}".format(self.newOneId, self.save_path))
        print("color: {0}, category: {1}, path: {2}".format(
            self.color, self.category, self.path))
        print(" ---------- identify result ----------")

    def useCamara(self):
        cap = cv2.VideoCapture(self.chooseCamara, cv2.CAP_DSHOW)  # 開啟攝像頭
        countDown = 7
        
        while True:
            ret, frame = cap.read()  # 讀取鏡頭畫面
            cv2.imshow("capture", frame)  # 生成攝像頭視窗
            countDown = countDown - 0.1
            # TODO: or countDown <= 0
            if cv2.waitKey(1) & 0xFF == ord('q') or countDown <= 0:  # 如果按下q 就截圖儲存並退出
                rotateImg = cv2.rotate(frame, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE) 
                outputSize = cv2.resize(rotateImg, (480, 640)) # to resize the image
                cv2.imwrite(self.save_path, self.white_balance_2(rotateImg))
                break

        cap.release()
        cv2.destroyAllWindows()  # 關閉視窗
        print("save: ", self.save_path)        


    def identifyCategory(self):
        pre = self.clf.predict(self.save_path)
        prediction = "Not_sure"
        if not pre[0]:
            print("NOT SURE")
        else:
            prediction = self.ClassifierLoop(pre)
        self.category = prediction
        
        
        # print("identifyCategory prediction", prediction)

        return self.category

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
            cv2.imwrite('./Controller/colorTmpFolder/' + d + '.jpg',
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

        # 黑色
        lower_black = np.array([0, 0, 0])
        upper_black = np.array([225, 255, 50])
        color_list = []
        color_list.append(lower_black)
        color_list.append(upper_black)
        dict['BLACK'] = color_list

        # #灰色
        lower_gray = np.array([120, 0, 0])
        upper_gray = np.array([150, 100, 100])
        color_list = []
        color_list.append(lower_gray)
        color_list.append(upper_gray)
        dict['GRAY'] = color_list

        # 白色
        # lower_white = np.array([0, 0, 221])
        # upper_white = np.array([180, 30, 255])
        # color_list = []
        # color_list.append(lower_white)
        # color_list.append(upper_white)
        # dict['WHITE'] = color_list

        # 紅色
        lower_red = np.array([156, 43, 46])
        upper_red = np.array([180, 255, 255])
        color_list = []
        color_list.append(lower_red)
        color_list.append(upper_red)
        dict['RED'] = color_list

        # 紅色2
        # lower_red = np.array([0, 43, 46])
        # upper_red = np.array([10, 255, 255])
        # color_list = []
        # color_list.append(lower_red)
        # color_list.append(upper_red)
        # dict['RED2'] = color_list

        # 橙色
        # lower_orange = np.array([11, 43, 46])
        # upper_orange = np.array([25, 255, 255])
        # color_list = []
        # color_list.append(lower_orange)
        # color_list.append(upper_orange)
        # dict['ORANGE'] = color_list

        # 黃色
        lower_yellow = np.array([26, 43, 46])
        upper_yellow = np.array([34, 255, 255])
        color_list = []
        color_list.append(lower_yellow)
        color_list.append(upper_yellow)
        dict['YELLOW'] = color_list

        # 綠色
        # lower_green = np.array([33, 41, 45])
        # upper_green = np.array([104, 107, 106])
        lower_green = np.array([20, 30, 20])
        upper_green = np.array([100, 80, 100])
        color_list = []
        color_list.append(lower_green)
        color_list.append(upper_green)
        dict['GREEN'] = color_list

        # 青色
        lower_cyan = np.array([78, 43, 46])
        upper_cyan = np.array([99, 255, 255])
        color_list = []
        color_list.append(lower_cyan)
        color_list.append(upper_cyan)
        dict['CYAN'] = color_list

        # 藍色
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([120,255,255])
        color_list = []
        color_list.append(lower_blue)
        color_list.append(upper_blue)
        dict['BLUE'] = color_list

        # 紫色
        lower_purple = np.array([120, 200, 110])
        upper_purple = np.array([150, 225, 225])
        color_list = []
        color_list.append(lower_purple)
        color_list.append(upper_purple)
        dict['PURPLE'] = color_list
            
        # 咖啡色
        lower_brown = np.array([5, 20, 40])
        upper_brown = np.array([50, 180, 90]) 
        color_list = []
        color_list.append(lower_brown)
        color_list.append(upper_brown)
        dict['BROWN'] = color_list
        
        # X V X
        
        # 粉紅色
        lower_pink = np.array([130, 10, 40])
        upper_pink = np.array([155, 225, 100])
        color_list = []
        color_list.append(lower_pink)
        color_list.append(upper_purple)
        dict['PINK'] = color_list

        return dict

    
    def ClassifierLoop(self, predict):
        if not predict[0]:
            return "Not_Sure"
        
        label_list = predict[0]
        tensorBase = predict[2]
        
        tens_list = []
        for base in tensorBase:
            if base.item() > 0.5:
                tens_list.append(base.item())
            
        print(tens_list, label_list)
        self.category = label_list[np.argmax(tens_list)]
        
        return  self.category
    


    def white_balance_2(self, img_input):
        '''
        完美反射白平衡
        STEP 1：计算每个像素的R\G\B之和
        STEP 2：按R+G+B值的大小计算出其前Ratio%的值作为参考点的的阈值T
        STEP 3：对图像中的每个点，计算其中R+G+B值大于T的所有点的R\G\B分量的累积和的平均值
        STEP 4：对每个点将像素量化到[0,255]之间
        依赖ratio值选取而且对亮度最大区域不是白色的图像效果不佳。
        :param img: cv2.imread读取的图片数据
        :return: 返回的白平衡结果图片数据
        '''
        img = img_input.copy()
        b, g, r = cv2.split(img)
        m, n, t = img.shape
        sum_ = np.zeros(b.shape)
        for i in range(m):
            for j in range(n):
                sum_[i][j] = int(b[i][j]) + int(g[i][j]) + int(r[i][j])
        hists, bins = np.histogram(sum_.flatten(), 766, [0, 766])
        Y = 765
        num, key = 0, 0
        ratio = 0.01
        while Y >= 0:
            num += hists[Y]
            if num > m * n * ratio / 100:
                key = Y
                break
            Y = Y - 1
        
        sum_b, sum_g, sum_r = 0, 0, 0
        time = 0
        for i in range(m):
            for j in range(n):
                if sum_[i][j] >= key:
                    sum_b += b[i][j]
                    sum_g += g[i][j]
                    sum_r += r[i][j]
                    time = time + 1
        
        avg_b = sum_b / time
        avg_g = sum_g / time
        avg_r = sum_r / time
        
        maxvalue = float(np.max(img))
        # maxvalue = 255
        for i in range(m):
            for j in range(n):
                b = int(img[i][j][0]) * maxvalue / int(avg_b)
                g = int(img[i][j][1]) * maxvalue / int(avg_g)
                r = int(img[i][j][2]) * maxvalue / int(avg_r)
                if b > 255:
                    b = 255
                if b < 0:
                    b = 0
                if g > 255:
                    g = 255
                if g < 0:
                    g = 0
                if r > 255:
                    r = 255
                if r < 0:
                    r = 0
                img[i][j][0] = b
                img[i][j][1] = g
                img[i][j][2] = r
    
        return img
    
    def white_balance_1(self, img):
        '''
        第一種簡單的求均值白平衡法
        :param img: cv2.imread讀取的圖片數據
        :return: 返回的白平衡結果圖片數據
        '''
        # 讀取圖像
        r, g, b = cv2.split(img)
        r_avg = cv2.mean(r)[0]
        g_avg = cv2.mean(g)[0]
        b_avg = cv2.mean(b)[0]
        # 求各個通道所佔增益
        k = (r_avg + g_avg + b_avg) / 3
        kr = k / r_avg
        kg = k / g_avg
        kb = k / b_avg
        r = cv2.addWeighted(src1=r, alpha=kr, src2=0, beta=0, gamma=0)
        g = cv2.addWeighted(src1=g, alpha=kg, src2=0, beta=0, gamma=0)
        b = cv2.addWeighted(src1=b, alpha=kb, src2=0, beta=0, gamma=0)
        balance_img = cv2.merge([b, g, r])
        return balance_img
    
    # https://www.twblogs.net/a/5c36d389bd9eee35b21d46e3
    # https://blog.csdn.net/ruoshui_t/article/details/109310806

    # https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv

    # https://stackoverflow.com/questions/47483951/how-to-define-a-threshold-value-to-detect-only-green-colour-objects-in-an-image/47483966#47483966
    
    
    # https://blog.csdn.net/weixin_43272781/article/details/103787735#
    # (:~SourceReaderCB terminating async callback)