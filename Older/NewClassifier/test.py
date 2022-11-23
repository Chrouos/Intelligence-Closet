import fastbook
fastbook.setup_book()


from fastai.vision.all import *
from fastai.vision.widgets import *

import pandas as pd
import joblib
import numpy as np
import cv2

def get_x(r): return './images_original/'+r['image'] # create path to open images in the original folder
def get_y(r): return r['label'].split(' ') # split the labels using space as a delimitter
def ClassifierLoop(predict):
    label_list = predict[0]
    tensorBase = predict[2]
    
    tens_list = []
    for base in tensorBase:
        if base.item() > 0.5:
            tens_list.append(base.item())
        
    print(tens_list, label_list)
    print(label_list[np.argmax(tens_list)])
    
    return label_list[np.argmax(tens_list)]

# 讀取圖檔
clf = joblib.load('./Controller/joblib_export.pkl')
img = cv2.imread('./Older/NewClassifier/test_picture/clothes_2.jpg')
ClassifierLoop(clf.predict(img))

img = cv2.imread('./Older/NewClassifier/test_picture/clothes_3.jpg')
ClassifierLoop(clf.predict(img))

img = cv2.imread('./Older/NewClassifier/test_picture/clothes_4.jpg')
ClassifierLoop(clf.predict(img))

img = cv2.imread('./Older/NewClassifier/test_picture/clothes_6.jpg')
ClassifierLoop(clf.predict(img))

# img = cv2.imread('./Older/NewClassifier/test_picture/clothes_7.jpg')
# ClassifierLoop(clf.predict(img))


