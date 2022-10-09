from cgitb import reset
import cv2 as cv
import mediapipe as mp
import time 
 
cap= cv.VideoCapture(0)

mpHands=  mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
# objct hands 
hands=mpHands.Hands(max_num_hands=2, min_detection_confidence=0.7)
while(True):
    success,img= cap.read()
    RGBimg=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    result=hands.process(RGBimg)
    
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                # print(id,lm)
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                if id==0:
                    cv.circle(img,(cx,cy),10,(0,0,0),cv.FILLED)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    # print(result.multi_hand_landmarks)
    cv.imshow("image",img)
    if cv.waitKey(1)== ord('q'):
        break
cap.release()
cv.destroyAllWindows()