import tensorflow as tf
from keras import layers, models
import os
import numpy as np
import cv2
from keras.utils import to_categorical

width = 300
height = 300

ruta_train = 'images/'

train_x = []
train_y = []

labels = os.listdir(ruta_train)

#En este caso es gato = 0 , perro = 1
label_map = {label: index for index, label in enumerate(labels)}

for i in os.listdir(ruta_train):
    for j in os.listdir(ruta_train + i):

        img = cv2.imread(ruta_train + i + '/' + j)
        resized_image = cv2.resize(img, (width, height)) / 255.0
        train_x.append(resized_image)
        train_y.append(label_map[i])

x_data = np.array(train_x)
y_data = np.array(train_y)

y_data = to_categorical(y_data, num_classes=len(labels))

model = tf.keras.Sequential([
    layers.Conv2D(32, (3, 3), input_shape=(width, height, 3)),
    layers.Activation('relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),

    layers.Conv2D(32, (3, 3)),
    layers.Activation('relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),

    layers.Conv2D(64, (3, 3)),
    layers.Activation('relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),

    layers.Flatten(),
    #Estas son las neuronas, en este caso 64
    layers.Dense(64),
    layers.Activation('relu'),
    layers.Dropout(0.3),

    layers.Dense(len(labels), activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
epochs = 100
model.fit(x_data, y_data, epochs=epochs)
models.save_model(model, 'ModelCD.keras')
