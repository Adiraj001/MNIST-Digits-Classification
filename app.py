import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

custom_objects = {'softmax_v2': tf.nn.softmax}

model = tf.keras.models.load_model('mnistmodel.keras', custom_objects=custom_objects)

image_number = 0

while os.path.isfile(f"digits/{image_number}.png"):
    try:
        # Load image and select the first channel
        img = cv2.imread(f"digits/{image_number}.png")[:, :, 0]
        
        # Necessary Fix: Resize to 28x28 so the model can process it
        img = cv2.resize(img, (28, 28))
        
        # Prepare the array and invert colors (standard MNIST format)
        img = np.invert(np.array([img]))
        
        # Make the prediction
        prediction = model.predict(img)
        
        print(f"This digit is probably a {np.argmax(prediction)}")
        
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()

    except:
        print("Error loading image!")

    finally:
        image_number += 1