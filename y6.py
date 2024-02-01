import cv2
import numpy as np

# Load the image
img = cv2.imread("C:\\Users\\DevAppSys Office\\Documents\\image.png",cv2.IMREAD_GRAYSCALE)

# Display the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
