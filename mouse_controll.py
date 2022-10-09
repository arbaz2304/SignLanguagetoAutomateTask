import cv2 as cv
from cv2 import reduce
from sklearn.cluster import cluster_optics_xi
import handTrackingModule as htm
import pyautogui as pg
import numpy as np
def mouse_control():
    reduce=140
    smooth=10
    wCam,hCam=640,480
    wScr,hScr=pg.size()
    cLocx,cLocy,pLocx,pLocy=0,0,0,0
    i=0

    cap= cv.VideoCapture(0)
    detector=htm.handDetector(maxHands=1)
    cap.set(3,480)
    cap.set(4,640)


    while(True):
        i+=1
        success,img = cap.read()
        img,noOfHands=detector.findHands(img,draw=True)
        pos,bbox=detector.findPos(img,draw=True,bbox=True)
        print(bbox)
            # index of middle and index finger
        if noOfHands>=1:
            x1,y1=pos[8][1:]
            x2,y2=pos[12][1:]
            #check up fingers:
            fingers=detector.fingersUp()
            cv.rectangle(img,(100,50),(wCam-100,hCam-120),(0,0,0),2)
            if fingers[1]==1 and fingers[2]==0:
                cv.circle(img,(x1,y1),10,(255,0,0),cv.FILLED)
                #convet screen
                x3=np.interp(x1,(100,wCam-100),(0,wScr))
                y3=np.interp(y1,(50,hCam-120),(0,hScr))
                cLocx=pLocx+(x3-pLocx)/smooth
                cLocy=pLocy+(y3-pLocy)/smooth
                pg.moveTo(wScr-cLocx,cLocy)
                pLocx,pLocy=cLocx,cLocy

            if fingers[1]==1 and fingers[2]==1 and fingers[3]==0:
                len,img,li=detector.findDistance(8,12,img,True)
                if len<30:
                    cv.circle(img,(li[4],li[5]),10,(0,255,255),cv.FILLED)
                    pg.click()
        cv.imshow("img",img)
        
        # if cv.waitKey(1)==ord('s'):
            
            
        #     cv.imwrite('img'+str(i)+'.jpg',cropImg)
        if cv.waitKey(1)==ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()


