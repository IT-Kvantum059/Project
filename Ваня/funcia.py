import cv2
import numpy as np
from matplotlib import pyplot as plt
from animal import imf
from multiprocessing import Process, Queue
#try:

#except Traceback:
#	print('ИЗОБРАЖЕНИЕ ОБОСРАЛОСЬ')


def get_roi(path, roi, q): # Фнукция для вывода определенной части изображения
	
	img = cv2.imread(path, 1) 
	#print(img.shape)
	q.put(img[roi[0][0]:roi[0][1], roi[1][0]:roi[1][1]])
	return img[roi[0][0]:roi[0][1], roi[1][0]:roi[1][1]]



if __name__ == "__main__": #Если запустить файл, то код будет читаться отсюда
	
	

	#1 - путь, а второе значение координат области изображения	
	# get_roi("/home/it-14/app.jpg", [(200,300), (400,600)]) 
	proc = Process(target = get_roi, args=("/home/it-14/app.jpg" ,[(200,300), (400,600)], Queue() ))
	proc.start()
	proc.join()
	cv2.imshow("wwww", )
	cv2.waitKey(0)

#записка на будущее
#тут может быть дохрена ошибок, так что надо будет сделать Try: except
