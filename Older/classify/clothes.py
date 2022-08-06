import numpy as np
import pandas as pd
from PIL import Image
import os
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
from sklearn.utils import shuffle
from sklearn.utils import class_weight
from sklearn.preprocessing import minmax_scale

import random
import cv2
from imgaug import augmenters as iaa
import warnings
warnings.filterwarnings('ignore')


import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Dropout, Activation, Input, BatchNormalization, GlobalAveragePooling2D
from tensorflow.keras import layers
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
from tensorflow.keras.experimental import CosineDecay
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.applications import EfficientNetB3, ResNet50
from tensorflow.keras.layers.experimental.preprocessing import RandomCrop,CenterCrop, RandomRotation

label = pd.read_csv('./archive/images.csv')

labels = list(label['label'].unique())

#print(labels)

path = './archive/images_compressed/'
y = pd.get_dummies(label['label'])
x = pd.DataFrame()
x['image_id'] = label['image'] + '.jpg'
#x['label'] = label['label']
x['filepath'] = path+ label['image'] + '.jpg'

file_list = os.listdir('./archive/images_compressed')

x = list(x['filepath'].values)

for idx,tmp in enumerate(x):
    if (tmp in file_list):
        print('False in ' + str(idx))

path = './archive/images_compressed/'
y = pd.get_dummies(label['label'])
x = pd.DataFrame()
x['image_id'] = label['image'] + '.jpg'
#x['label'] = label['label']
x['filepath'] = path+ label['image'] + '.jpg'

x = list(x['filepath'].values)
y = list(y.values)

delete = [533,702,859,1659,1759]
for de in delete:
    del y[de]
    del x[de]

img_size = 224
img_shape = (img_size,img_size,3)
batch_size = 32
epochs = 20
dropout_rate = 0.5
num_of_predict = len(y[0])
len_data = 4000

train_img = []
for idx,img in enumerate(x):
    try:
        tmp = cv2.imread(img,cv2.IMREAD_COLOR)
        tmp = cv2.resize(tmp,dsize=(img_size,img_size),
                         interpolation=cv2.INTER_AREA)
        train_img.append(tmp)
    except Exception as e:
        print(str(e)+str(idx))
train_img = np.array(train_img)

#print(len(train_img),len(y))

train_img = np.array(train_img)/255.
y = np.array(y)

train_x = train_img[:4000]
val_x = train_img[4000:]
train_y = y[:4000]
val_y = y[4000:]

del train_img
del y

data_augmentation_layers = tf.keras.Sequential(
    [
        layers.experimental.preprocessing.RandomCrop(height=img_size, width=img_size),
        layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"),
        layers.experimental.preprocessing.RandomRotation(0.25),
        layers.experimental.preprocessing.RandomZoom((-0.2, 0)),
        layers.experimental.preprocessing.RandomContrast((0.2,0.2))
    ]
)

efficientnet = EfficientNetB3(weights='imagenet',
                              include_top=False,
                              input_shape=img_shape,
                              drop_connect_rate=dropout_rate)

inputs = Input(shape=img_shape)
#augmented = data_augmentation_layers(inputs) #Augmentation
efficientnet = efficientnet(inputs) #efficientnet
pooling = layers.GlobalAveragePooling2D()(efficientnet) #globalaveragepooling
dropout = layers.Dropout(dropout_rate)(pooling) #dropout
outputs = Dense(len(val_y[0]), activation="softmax")(dropout)
model2 = Model(inputs=inputs, outputs=outputs)

decay_steps = int(round(4000*0.8/batch_size))*epochs
cosine_decay = CosineDecay(initial_learning_rate=3e-5, decay_steps=decay_steps, alpha=0.3)

model2.compile(loss=tf.keras.losses.CategoricalCrossentropy(),
               optimizer=tf.keras.optimizers.Adam(cosine_decay), metrics=["accuracy"])

model2.summary()

history=model2.fit(train_x,train_y,batch_size=batch_size,epochs=25,
                   validation_data=(val_x,val_y))

model2.evaluate(x=val_x,y=val_y)
model2.save('./h5/eff_final.h5')
