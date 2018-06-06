import cv2
import numpy as np

# cap = cv2.VideoCapture(0)
# while(True):
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("gray", gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

conycry = cv2.imread('conycry.png', cv2.IMREAD_COLOR)
# Draw Some Line
# cv2.line(conycry, (0, 0), (150, 150), (255, 150, 255), 10)
# cv2.rectangle(conycry, (30, 50), (200, 250), (0, 0, 255), 10)
# cv2.imshow('conycry', conycry)
# cv2.rectangle(conycry, (30, 10), (200, 250), (0, 0, 255), 2)
# cv2.circle(conycry, (121, 135), 70, (0, 255, 0), 2)
cv2.imshow('conycry', conycry)
cv2.waitKey(0)
cv2.destroyAllWindows()
