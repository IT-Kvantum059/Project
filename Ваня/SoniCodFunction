
import numpy as np
import cv2 as cv2
EXAMPLE="/home/it-6/Изображения/Обои/big-floppa-meme.png"

def imf(frame, example=EXAMPLE):#функция сравнения кадра из видео с эталоном
	imageExample = cv2.imread(example,0)#
	image1 = cv2.imread(frame,0)
	resized1= cv2.resize(image1, (8,8), interpolation = cv2.INTER_AREA) #Уменьшим картинку,INTER_AREA это передискретизации с использованием отношения площади пикселя, понятия не имею что это, но оно работае

	resized = cv2.resize(imageExample, (8,8), interpolation = cv2.INTER_AREA) #Уменьшим картинку,INTER_AREA это передискретизации с использованием отношения площади пикселя, понятия не имею что это, но оно работае

	avg=resized.mean()#функция mean ищет среднее арифметическое масива изображения
	avg1=resized1.mean()
	s,threshold_image=cv2.threshold(resized,avg,255, 0)#Функция threshold возвращает изображение, в котором все пиксели, которые темнее 127 заменены на 0, а все, которые ярче 127, — на 255

	d,threshold_image1=cv2.threshold(resized1,avg1,255, 0)#Функция threshold возвращает изображение, в котором все пиксели, которые темнее 127 заменены на 0, а все, которые ярче 127, — на 255
	similar_coeff = np.sum((threshold_image1-threshold_image)**2)
	
	return similar_coeff

if __name__ == "__main__":

	print(imf("/home/it-6/Изображения/Обои/388156-svetik.jpg"))#   кадры из видео
