import numpy as np
import cv2

kamera=cv2.VideoCapture(0) # wabcam i kullanma
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output3.avi',fourcc, 20.0, (640,480))

while(True):
 ret,cerceve=kamera.read() # video yu cerceveye oturtma
 cerceve = cv2.flip(cerceve, 1)
 #gri_renk=cv2.cvtColor(cerceve , 1) #renk degistirme fonk
 out.write(cerceve)
 cv2.imshow('baslik',cerceve)
 if cv2.waitKey(1) & 0xff == ord('q'): # q harfine basildiginda true olur
    break

kamera.release() #kamerayi kapat
out.release()
cv2.destroyAllWindows()
