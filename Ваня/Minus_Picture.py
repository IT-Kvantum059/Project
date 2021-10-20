import numpy as np

import cv2 as cv

img0 = cv.imread('/home/it-14/756038770746465.jpg')
img_sm = cv.resize(img0,(int(img0.shape[1]/100), int(img0.shape[0]/100)))
cv.imwrite('/home/it-14/756038770746465.jpg', img_sm)

filename = "/home/it-14/756038770746465.jpg"
img1 = cv.imread(filename)

while True:
	
	

	cv.imshow("GOVNO_SOBAKI", img1)
	g = cv.waitKey(20)
	if g & 0XFF == ord("q"):
		break
