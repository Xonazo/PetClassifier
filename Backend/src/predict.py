import cv2
import numpy as np
from keras import models

width = 300
height = 300

model = models.load_model('ModelCD.keras')

def predict_image(image_predict):
    my_image = cv2.imread(image_predict)
    my_image = cv2.resize(my_image, (width, height))

    result = model.predict(np.array([my_image]))[0]
    
    print(result)

    if result[0] > result[1]:
        prediction = 'cat'
    else:
        prediction = 'dog'
    
    response = {
        'prediction': prediction,
        'cat': float(result[0]),
        'dog': float(result[1])
    }

    return response
