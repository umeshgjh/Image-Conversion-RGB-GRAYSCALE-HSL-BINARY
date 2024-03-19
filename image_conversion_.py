# -*- coding: utf-8 -*-
"""Image Conversion .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jh6MzRCfiO32aslNkEpux-aKrUL_9VfQ
"""

import numpy as np
import cv2
from google.colab.patches import cv2_imshow
photo = cv2.imread('/content/My Photograph.jpg')
print("ORIGINAL IMAGE")
photo.shape
cv2_imshow(photo)
photo.size
Gray = cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)
print("GRAY SCALE")
cv2_imshow(Gray)
"""RGB to HSL"""
print("HSL MODEL")
hsl = cv2.cvtColor(photo,cv2.COLOR_BGR2HSV)
cv2_imshow(hsl)
"""**RGB to YCrCb Conversion**"""

r2y = cv2.cvtColor(photo,cv2.COLOR_BGR2YCrCb)
print('YCrCb MODEL')
cv2_imshow(r2y)
cv2.imwrite('ycrcb.jpeg',r2y)

# Convert the RGB image to binary
threshold_value = 127
binary_image = np.zeros_like(photo)
binary_image[photo > threshold_value] = 255

print("BINARY IMAGE")
cv2_imshow(binary_image)

