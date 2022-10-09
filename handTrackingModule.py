from cgitb import reset
from turtle import position
import cv2 as cv
import mediapipe as mp
import time 
import math
 

class handDetector():
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        self.mpHands=  mp.solutions.hands
        self.mpDraw = mp.solutions.drawing_utils
        # objct hands 
        self.hands=self.mpHands.Hands(max_num_hands=self.maxHands, min_detection_confidence=self.detectionCon)
        self.tipIds=[4,8,12,16,20]

    def findHands(self,img,draw=False):
        img=img
        RGBimg=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.result=self.hands.process(RGBimg)
        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                if draw==True:
                    self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
            noOfHands=len(self.result.multi_hand_landmarks)
            return img,noOfHands
        return img,0

    def findPos(self,img,handNo=0,draw=False,bbox=False):
        xList = []
        yList = []
        bbox = []
        self.lmList = []
        myHand=None
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                # print(id, cx, cy)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 5, (255, 0, 255), cv.FILLED)
            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = xmin, ymin, xmax, ymax
    
            if bbox:
                cv.rectangle(img, (bbox[0] - 20, bbox[1] - 20),
            (bbox[2] + 20, bbox[3] + 20), (0, 255, 0), 2)
        
        return self.lmList, bbox

    def fingersUp(self):
        fingers = []
        # Thumb
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # 4 Fingers
        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

    def findDistance(self, p1, p2, img, draw=True):

        x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
        x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        
        if draw:
            cv.circle(img, (x1, y1), 10, (0,255,255),cv.FILLED)
            cv.circle(img, (x2, y2), 10,(0,255,255),cv.FILLED)
            cv.line(img, (x1, y1), (x2, y2), (0, 0, 0), 1)
            cv.circle(img, (cx, cy), 10, (128,0,128), cv.FILLED)
        
        length = math.hypot(x2 - x1, y2 - y1)
        return length, img, [x1, y1, x2, y2, cx, cy]






def main():
    cap= cv.VideoCapture(0)
    detector=handDetector(maxHands=1)
    while(True):
        success,img = cap.read()
        img,noOfHands=detector.findHands(img,draw=True)

        if noOfHands>0:
            pos,bbox=detector.findPos(img,draw=True)
            print(detector.fingersUp())
        cv.imshow("img",cv.flip(img,1))
        if cv.waitKey(1)==ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

if __name__=="__main__":
    main()