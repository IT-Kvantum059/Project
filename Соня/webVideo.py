import cv2
capImg=cv2.VideoCapture(0)# запуск в реальном вр
while(True):
	c=capImg.read()
	#if frame is None:
		#break
	cv2.imshow("hhhh",c)
	g=cv2.waitKey(30)
	if g==ord('g'):
		break
	capImg.release()
	cv2.destroyAllWindows()

	



