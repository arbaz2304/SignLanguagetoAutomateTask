import handTrackingModule as htm
import cv2 as cv
import mycanvas



def draw():
    cap=cv.VideoCapture(0)
    det=htm.handDetector(maxHands=1)
    fingers=[]
    flag=[]
    while (True):
        suc,img=cap.read()
        img,noOfHands=det.findHands(img)
        if noOfHands>0:
            pos,bbox=det.findPos(img,bbox=True)
            fingers =det.fingersUp()
            if fingers==[0,0,0,0,0]:
                cv.rectangle(img,(bbox[0]-20,bbox[1]-20),(bbox[0]+90,bbox[1]-60),(255,0,255),cv.FILLED)
                cv.putText(img,'circle',(bbox[0]-15,bbox[1]-35),cv.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
                flag.append('circle')
                
            elif fingers==[0,1,0,0,1]:
                cv.rectangle(img,(bbox[0]-20,bbox[1]-20),(bbox[0]+90,bbox[1]-60),(255,0,255),cv.FILLED)
                cv.putText(img,'rectangle',(bbox[0]-15,bbox[1]-35),cv.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
                flag.append('rectangle')
                
            elif fingers==[0,1,1,1,0]:
                cv.rectangle(img,(bbox[0]-20,bbox[1]-20),(bbox[0]+90,bbox[1]-60),(255,0,255),cv.FILLED)
                cv.putText(img,'triangle',(bbox[0]-15,bbox[1]-35),cv.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
                flag.append('triangle')

            elif fingers==[0,1,0,0,0]:
                cv.rectangle(img,(bbox[0]-20,bbox[1]-20),(bbox[0]+90,bbox[1]-60),(255,0,255),cv.FILLED)
                cv.putText(img,'turn Left',(bbox[0]-15,bbox[1]-35),cv.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
                flag.append('turn Left')

            elif fingers==[0,1,1,0,0]:
                cv.rectangle(img,(bbox[0]-20,bbox[1]-20),(bbox[0]+95,bbox[1]-60),(255,0,255),cv.FILLED)
                cv.putText(img,'turn Right',(bbox[0]-15,bbox[1]-35),cv.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
                flag.append('turn Right')

            if len(flag)>15:
                mycanvas.draw(flag[8])
                flag.clear()

            # cv.circle(img,(bbox[0],bbox[1]),5,(0,0,0),cv.FILLED)
            

            

        cv.imshow('img',img)

        if cv.waitKey(1)==ord('q'):
            break

    cv.destroyAllWindows()
    cap.release()