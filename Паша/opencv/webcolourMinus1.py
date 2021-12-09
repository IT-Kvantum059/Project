import numpy as np
import cv2

cap = cv2.VideoCapture(0)
 
while(True):
    ret, frame = cap.read() #берем картинку с вебки
    frame = cv2.flip(frame, 1) # ПЕРЕВЕРНИТЕ КАМЕРУ ОБРАТНО
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    resized_image = cv2.resize(frame, (3, 2)) 

    print(resized_image[1,0])

    hsv_img=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)# конвертируем изображение в hsv
    frame[0,10]=[255, 255, 255]

    color_low= (0, 30, 60)# нижний диапозон цвета
    color_hight= (20, 150, 255)#верхний диапозон цвета    

    ol=cv2.inRange(hsv_img,color_low,color_hight)#наложение цветовой маски на изображение, ol присваивает результат
    cv2.imshow("wwww",ol)
    cv2.imshow("1",frame)    
    cv2.imshow("2",resized_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()