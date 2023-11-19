import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import math
pyautogui.FAILSAFE= False

wScrn,hScrn = pyautogui.size()
wCam, hCam = 640,480
smoothening = 4

pTime = 0
plocX, plocY  = 0,0
clocX, clocY  = 0,0

#Mediapipe API
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

frameR= 100
tipIds = [4,8,12,16,20]

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5,max_num_hands=1) as hands:
    while cap.isOpened():
        success, img = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        cv2.rectangle(img, (frameR,frameR-50),(wCam-frameR,hCam-frameR-50),(255, 0, 0), 2)
        img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
        img.flags.writeable = False
        results = hands.process(img)
        img.flags.writeable = True
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        lmList=[]
        handType =[]

        if results.multi_hand_landmarks:
            for hand in results.multi_handedness:
                hand_label = hand.classification[0].label
                handType.append(hand_label)
            for hand_landmarks in results.multi_hand_landmarks:
                myHands = results.multi_hand_landmarks[0]
                for id,lm in enumerate(myHands.landmark):
                    h,w,c = img.shape
                    cx,cy = int(lm.x*w),int(lm.y*h)
                    lmList.append([id,cx,cy])
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
        fingers = []
        if len(lmList)!=0:
            x1,y1 = lmList[8][1], lmList[8][2]
            x2,y2 = lmList[12][1], lmList[12][2]

            #Get fingers
            if handType[0] == 'Left':
                if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]: fingers.append(1)
                else: fingers.append(0)
            if handType[0] == 'Right':
                if lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1]: fingers.append(1)
                else: fingers.append(0)
            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]: fingers.append(1)
                else: fingers.append(0)

            #Check index finger is moving in zone.
            if x2 in range(frameR,wCam-frameR) and y2 in range(frameR-50,hCam-frameR-50):
                x3= np.interp(x2,(frameR,wCam-frameR),(0,wScrn))
                y3= np.interp(y2,(frameR-50,hCam-frameR-50),(0,hScrn))
                #Smoothen Values
                clocX = plocX + (x3-plocX)/smoothening
                clocY = plocY + (y3-plocY)/smoothening

                #Move mouse
                if fingers[0]==0 and fingers[1]==1 and fingers[2]==1 and fingers[3]==0 and fingers[4]==0:
                    pyautogui.moveTo(clocX,clocY,duration=0)
                    cv2.circle(img,(x2,y2),10,(255,0,255),cv2.FILLED)
                    plocX,plocY = clocX,clocY

                #Mouse click
            if fingers[1]==0 and fingers[2]==1:
                cv2.circle(img,(x2,y2),10,(0,255,0),cv2.FILLED)
                pyautogui.click()

        cv2.imshow('Mouse Controler', img)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()