import numpy as np
import cv2

cap = cv2.VideoCapture(0)
 
while(True):
    ret, frame = cap.read() #берем картинку с вебки
    frame = cv2.flip(frame, 1) # ПЕРЕВЕРНИТЕ КАМЕРУ ОБРАТНО
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    height, width = frame.shape[:2]

    i = 0
    a = 0

    while ( i < height):
        frame[i,width//2]=[255, 255, 255]
        i+=1

    while ( a < width):
        frame[height//2,a]=[255, 255, 255]
        a+=1


    
    hsv_img=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)# конвертируем изображение в hsv
    
    color_low= (0, 30, 60)# нижний диапозон цвета
    color_hight= (20, 150, 255)#верхний диапозон цвета
    ol=cv2.inRange(hsv_img,color_low,color_hight)#наложение цветовой маски на изображение, ol присваивает результат

    cv2.imshow("wwww",ol)
    cv2.imshow("1",frame)
    cv2.imshow('IMG',gray2)

cap.release()
cv2.destroyAllWindows()