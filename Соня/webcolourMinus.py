import numpy as np
import cv2

cap = cv2.VideoCapture(0)
 
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, -1) # ПЕРЕВЕРНИТЕ КАМЕРУ ОБРАТНО
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    hsv_img=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)# конвертируем изображение в hsv
    color_low= (0, 30, 60)# нижний диапозон
    color_hight= (20, 150, 255)#верхний диапозон
    ol=cv2. inRange(hsv_img,color_low,color_hight)#наложение цветовой маскт на изображение, ol присваивает результат
    cv2.imshow("wwww",ol)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()