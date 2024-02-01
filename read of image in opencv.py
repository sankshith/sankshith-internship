import cv2
import numpy as np

# Load the image
img = cv2.imread("C:\\Users\\DevAppSys Office\\Documents\\image.png")
imgs = cv2.imwrite("C:\\Users\\DevAppSys Office\\Documents\\image45.png",img)
cv2.imshow('Hello World',img)
print('Height of Image:', int(img.shape[0]), 'pixels')
print('Width of Image: ', int(img.shape[1]), 'pixels')
cv2.imwrite('output.jpg', img)
cv2.imwrite('output.png', img)
print(img.shape)
 
