import cv2
import numpy as np
from matplotlib import pyplot as plt
x1 = 100
y1 = 100
y2 = 400
x2 = 400

def get_roi(path, roi): # Фнукция для вывода определенной части изображения
	
	img = cv2.imread(path, 1) 
	#print(img.shape)
	return img[roi[0][0]:roi[0][1], roi[1][0]:roi[1][1]]


if __name__ == "__main__": #Если запустить файл, то код будет читаться отсюда
	
	#1 - путь, а второе значение координат области изображения	
	loli = get_roi("/home/it-14/app.jpg", [(200,300), (400,600)]) 
	
	cv2.imshow("wwww", loli)
	cv2.waitKey(0)

#записка на будущее
#тут может быть дохрена ошибок, так что надо будет сделать Try: except

