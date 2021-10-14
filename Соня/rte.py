
import cv2


cap = cv2.VideoCapture(0);               # Видео вывод с веб камеры компьютера, при включенной камере
cap = cv2.VideoCapture("VIDEO0102.mp4"); # Вывод с видео файла

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # Вывод в консоли размера нашего окна.


cap.set(3,1280) # Установление длины окна
cap.set(4,700)  # Ширина окна

print(cap.get(3))
print(cap.get(4))

