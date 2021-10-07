# код который обводит контуры объекта на фото

import numpy as np

import cv2

fileName = '/home/sophia/Изображения/u.jpg' 

image = cv2.imread(fileName)

hsv_img = cv2.cvtColor( image, cv2.COLOR_BGR2HSV )

hsv_min = np.array((2, 28, 65), np.uint8)
hsv_max = np.array((26, 238, 255), np.uint8)

hsv_msk = cv2.inRange( hsv_img, hsv_min, hsv_max ) #применяем цветовой филь
contours, hierarchy = cv2.findContours( hsv_msk, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours( image, contours, -1, (255,0,0),3, cv2.LINE_AA, hierarchy, 2)

cv2.imshow('contours', image) 

cv2.waitKey()
cv2.destroyAllWindows()