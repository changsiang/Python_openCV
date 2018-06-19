import cv2
import numpy as np

# Threshold tutorial

cv2.imread('islet.jpg')
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(grayscale, 12, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
adthreshold = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('Islet', img)
cv2.imshow('Threshold', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
