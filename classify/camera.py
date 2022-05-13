import cv2
import os

my_path = os.getcwd()

cap = cv2.VideoCapture(0)  # 開啟攝像頭
my_path = "e:/ProgrammingLanguage/git/Intelligence-Closet/classify" # 不同路徑

while True:
    ret, frame = cap.read() # 讀取鏡頭畫面

    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    height,width,ret=frame.shape

    cx=int(width/2)
    cy=int(height/2)

    pixel_center=hsv_frame[cx,cy]
    hue_value=pixel_center[0]
    hue_value1=pixel_center[1]
    hue_value2=pixel_center[2]

    color="Undefined"
    if hue_value2<50:
        color="BLACK"
    elif hue_value1<20:
        color="WHITE"
    elif hue_value<5:
        color="RED"
    elif hue_value<22:
        color="ORANGE"
    elif hue_value<33:
        color="YELLOW"
    elif hue_value<94:
        color="GREEN"
    elif hue_value<131:
        color="BLUE"
    elif hue_value<167:
        color="PURPLE"
    elif hue_value>=167:
        color="RED"


    #cv2.putText(frame,color,(10,50),0,1,(0,0,0),2)
    print(pixel_center)
    #cv2.circle(frame,(cx,cy),5,(0,0,0),3)

    cv2.imshow("capture", frame)  # 生成攝像頭視窗

    if cv2.waitKey(1) & 0xFF == ord('q'):  # 如果按下q 就截圖儲存並退出
        cv2.imwrite(my_path + "./images/test.png", frame)  # 儲存路徑
        break

cap.release()
cv2.destroyAllWindows() # 關閉視窗

cls_list = ['Not_sure',
 'T-Shirt',
 'Shoes',
 'Shorts',
 'Shirt',
 'Pants',
 'Skirt',
 'Other',
 'Top',
 'Outwear',
 'Dress',
 'Body',
 'Longsleeve',
 'Undershirt',
 'Hat',
 'Polo',
 'Blouse',
 'Hoodie',
 'Skip',
 'Blazer']

from keras.preprocessing import image
#from keras.models import load_model
import tensorflow as tf
#from keras import backend as K
import numpy as np
import os



 
# 關閉GPU加速功能(建議安裝無GPU版本, 縮短初始化時間)
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# 開啟800字典
words_path = my_path + './archive/images.csv'
file1 = open(words_path, 'rt', encoding='Big5')
labels = list(file1.read())
file1.close()

# 載入模型
model_path = my_path + './h5/eff_final.h5'
model = tf.compat.v1.keras.models.load_model(model_path)

# 讀取照片
img_path = my_path + './images/test.png'
try:
    img = image.load_img(img_path, target_size=(224, 224))
except Exception as e:
    print(img_path, e)

# 圖檔預處理
#img = image.img_to_array(img) # 灰階
img = np.expand_dims(img, axis=0) # 轉換通道
img = img/255 # rescale

# 計算機率與預測結果
pred = model.predict(img)[0]
print(pred) # 機率list
index = np.argmax(pred)
prediction = cls_list[index]
print('\ncolor:',color)
print('category:',prediction) # 預測結果