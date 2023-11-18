import cv2
import mediapipe as mp
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#Mediapipe API
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Volume Control Library Usage
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
minVol , maxVol , volBar, volPer= -20, 0 , 400, 0

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, img = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
        img.flags.writeable = False
        results = hands.process(img)
        img.flags.writeable = True
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        lmList=[]

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                myHands = results.multi_hand_landmarks[0]
                for id,lm in enumerate(myHands.landmark):
                    h,w,c = img.shape
                    cx,cy = int(lm.x*w),int(lm.y*h)
                    lmList.append([id,cx,cy])
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        #Get cordinate of the thumb and the index finger
        if len(lmList)!=0:
            x1,y1 = lmList[4][1], lmList[4][2]
            x2,y2 = lmList[8][1], lmList[8][2]
            cx, cy = (x1+x2)//2,(y1+y2)//2
            #Calculate the length between the thumb and the index finger
            d = math.sqrt((x2-x1)**2+(y2-y1)**2)

            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            cv2.circle(img,(x2,y2),15,(255,0,255),cv2.FILLED)
            cv2.line(img, (x1,y1),(x2,y2),(255,0,255),3)
            cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)

            #Set volume depends on the length
            if d < 50:
                vol = -96
                cv2.line(img,(x1,y1),(x2,y2),(0,0,255),3)
            else:
                vol = np.interp(d, [25, 270], [minVol, maxVol])

            volume.SetMasterVolumeLevel(vol, None)
            volBar = np.interp(d, [50, 270], [400, 150])
            volPer = np.interp(vol, [minVol, maxVol], [0, 100])

            #Volume bar drawing
            cv2.rectangle(img, (50, 150), (50, int(volBar)), (0, 0, 0), 3)
            cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
            cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

        cv2.imshow('Volume Controler', img)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
