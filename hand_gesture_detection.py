# TechVidvan hand Gesture Recognizer

# import necessary packages

import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
import sound
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import handTrackingModule as htm


def gesture_Recognition():
    flag=[]
    bbox=[]

    # initialize mediapipe
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    mpDraw = mp.solutions.drawing_utils

    # Load the gesture recognizer model
    model = load_model('mp_hand_gesture')

    # Load class names
    f = open('gesture.names', 'r')
    classNames = f.read().split('\n')
    f.close()
    print(classNames)


    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    det=htm.handDetector()
    while True:
        # Read each frame from the webcam
        _, frame = cap.read()    
        x, y, c = frame.shape
        # Flip the frame vertically
        frame = cv2.flip(frame, 1)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        img,noOfHands=det.findHands(frame)
        if noOfHands>0:
            pos,bbox=det.findPos(img,bbox=True)

        # Get hand landmark prediction
        result = hands.process(framergb)

        # print(result)
        
        className = ''

        # post process the result
        landmarks=[]
        if result.multi_hand_landmarks:
            
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    # print(id, lm)
                    lmx = int(lm.x * x)
                    lmy = int(lm.y * y)

                    landmarks.append([lmx, lmy])

                # Drawing landmarks on frames
                mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

                # Predict gesture
                prediction = model.predict([landmarks])
                # print(prediction)
                classID = np.argmax(prediction)
                className = classNames[classID]

            flag.append(className)
            # show the prediction on the frame
            cv2.rectangle(img,(bbox[0]-20,bbox[1]-20),(bbox[0]+100,bbox[1]-60),(255,0,255),cv2.FILLED)
            cv2.putText(img,className,(bbox[0]-15,bbox[1]-35),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
            if len(flag)>8:
                sound.speak(className)
                flag.clear()

        # Show the final output
        cv2.imshow("Output", frame) 

        if cv2.waitKey(1) == ord('q'):
            break

    # release the webcam and destroy all active windows
    cap.release()

    cv2.destroyAllWindows()