# выделяе предмет заданого цвета
import cv2
img1 = cv2.imread('/home/sophia/Изображения/u.jpg')#ссылка на фотку
cv2.imshow("hhhh",img1)#оригинал
hsv_img=cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)# конвертируем изображение в hsv
color_low= (0, 30, 60)# нижний диапозон
color_hight= (20, 150, 255)#верхний диапозон
ol=cv2. inRange(hsv_img,color_low,color_hight)#наложение цветовой маскт на изображение, ol присваивает результат
cv2.imshow("wwww",ol)
cv2.waitKey(0)
