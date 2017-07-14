import numpy as np
import cv2
cam = cv2.VideoCapture(0)


while(True):
# Capture frame-by-frame
    ret, frame = cam.read()
# Our operations on the frame come here
    gray = cv2.cvtColor(frame, 1)
# Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):    #İşletim sisteminiz 64 bit ise 0xFF ile ve'lemeniz gerekir.
        break
# When everything done, release the capture
    cam.release()
    cv2.destroyAllWindows()
