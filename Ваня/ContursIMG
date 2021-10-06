#данная программа определяет контуры каких-либо изображений
#взято здесь: https://www.youtube.com/watch?v=Sr0KQftXcEg

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/home/izackfostar/python/4.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

_, binary = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
plt.imshow(binary,cmap="gray")
plt.show()

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(img, contours, -1,(0,255,0,), 2)
plt.imshow(img)
plt.show()
