import cv2


cap = cv2.VideoCapture(0) # Видео вывод с веб камеры компьютера, при включенной камере


print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # Вывод в консоли размера нашего окна.

while(True):
    cap.set(3,1000) # Установление длины окна
    cap.set(4,900)
    ret, frame = cap.read()
    #frame = cv2.flip(frame, 1) # ПЕРЕВЕРНИТЕ КАМЕРУ ОБРАТНО
    cv2.rectangle(frame, (600, 300), (100,50), (100, 300, 100), 5)
    cv2.imshow("wwww", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  # Ширина окна

print(cap.get(3))
print(cap.get(4))
