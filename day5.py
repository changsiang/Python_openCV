# Image blending

import cv2
import numpy as np

# load two images
img1 = cv2.imread('islet.jpg', cv2.IMREAD_REDUCED_COLOR_2)
img2 = cv2.imread('Cony_Balloon.png', cv2.IMREAD_REDUCED_COLOR_2)

# Create a ROI
rows, cols, channels = img2.shape
# print('rows >> ', rows)
# print('cols >> ', cols)
# print('channels >> ', channels)
roi = img1[0:rows, 0:cols]

# Now create a mask of cony and its inverse mask
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# print('ret >> ', ret)
# print('mask >> ', mask)
mask_inv = cv2.bitwise_not(mask)

# Now blackout the area of cony in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of cony
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)


# Put cony in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()







