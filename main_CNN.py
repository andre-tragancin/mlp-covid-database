import cv2
from lbp import LocalBinaryPatterns as LBP
from to_gray import toGray

import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import load_img 
from keras.preprocessing.image import img_to_array 

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

database_name = "COVID-19_Radiography_Dataset"

# images com resolução de 299*299
qtd_max_imgs = 7232 

gray = toGray()

data = []
label = []

for i in range(1,qtd_max_imgs+1):
    id = str(i)

    path_covid = "./database/"+database_name+"/COVID/COVID-"+id+".png"
    path_normal = "./database/"+database_name+"/Normal/Normal-"+id+".png"

    img_covid = cv2.imread(path_covid)
    img_covid = gray.image_to_gray(img_covid)

    img_normal = cv2.imread(path_normal)
    img_normal = gray.image_to_gray(img_normal)
    
    data.append(img_covid)
    label.append(0)
    data.append(img_normal)
    label.append(1)

data = np.asarray(data)
label = np.asarray(label)
x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.20)

x_train = x_train/255.0
x_test = x_test/255.0

print(len(x_train), len(y_train))

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(299, 299)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(2, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=50)

test_loss, test_acc = model.evaluate(x_test,  y_test, verbose=2)

print('\nTest accuracy:', test_acc)