import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("/home/it-14/app.jpg", 1) 
print(img.shape)
# img[250:500, 400:600]
cv2.imshow("wwww", img[1:30, 2:49])
cv2.waitKey(0)

# while(True):
#     #frame = cv2.flip(frame, 1) # ПЕРЕВЕРНИТЕ КАМЕРУ ОБРАТНО
#     print(img.shape)
#     img[250:500, 250:500]

#     cv2.imshow("wwww", img )
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#   # Ширина окна

