from sre_constants import SUCCESS
import handTrackingModule as htm
import cv2 as cv
import math
import pycaw as caw
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pyautogui as pg
import numpy as np 

def cntrl_vol():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    cap= cv.VideoCapture(0)
    detector=htm.handDetector()
    while(True):
            success,img = cap.read()
            img,noOfHands=detector.findHands(img,draw=True)

            pos,bbox=detector.findPos(img,draw=True)
            if noOfHands>1:
                cv.circle(img,(pos[8][1],pos[8][2]),10,(255,255,255),cv.FILLED)
                cv.circle(img,(pos[4][1],pos[4][2]),10,(255,200,155),cv.FILLED)
                cv.line(img,(pos[4][1],pos[4][2]),(pos[8][1],pos[8][2]),(150,134,125),2)
                len=(math.hypot((pos[8][1]-pos[4][1]),(pos[8][2]-pos[4][2])))
                print(len)
                maxLen=170
                minLen=12
                maxvol=0
                minvol=-65
                volLevel=np.interp(len,(minLen,maxLen),(minvol,maxvol))
                volume.SetMasterVolumeLevel(volLevel, None)
                cv.putText(cv.flip(img,1),str(volLevel),(10,200),cv.FONT_HERSHEY_SIMPLEX,2,(90,56,23),8)
            cv.imshow("img",img)
            if cv.waitKey(1)==ord('q'):
                break
    cap.release()
    cv.destroyAllWindows()

