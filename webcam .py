#Download IP webcam application from play store
import cv2
import numpy as np
url = "http://10.100.30.7:8080/video"
#Type ip address for 
cp = cv2.VideoCapture(url)
while(True):
    ret, frame=cp.read()
    #_,frame=cp.read()
    if frame is not None:
        cv2.imshow("frame",frame)
    '''    
    #desroy using "q"
    q=cv2.waitKey(1)
    if q==ord("q"):
        break
    '''
    #destroy using Esc key
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cp.release()    

cv2.destroyAllWindows()    