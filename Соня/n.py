import numpy as np

import cv2 as cv

img0=cv.imread ('/home/sophia/Изображения/u.jpg')

img_sm = cv.resize(img0,(int(img0.shape[1]/100), int(img0.shape[0]/100)))
cv.imwrite('/home/sophia/Изображения/u4.jpg',img_sm)
#средннее квадр смещение