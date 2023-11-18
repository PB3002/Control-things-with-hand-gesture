import tkinter as tk
import cv2
from PIL import Image, ImageTk
import mediapipe as mp

#Mediapipe API
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

tipIds = [4,8,12,16,20]
hands =  mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7,max_num_hands=1)

width,height = 400,300  
cap = cv2.VideoCapture(0)
app = tk.Tk()

cap.set(3, width) 
cap.set(4, height) 

# Create the canvas to display the light bulbs
canvas = tk.Canvas(app, width=700, height=200)
canvas.pack()
move = 125

label_widget = tk.Label(app) 
label_widget.pack() 

# Create the five light bulbs
oval1 = canvas.create_oval(50, 50, 150, 150, fill="gray")
oval2 = canvas.create_oval(50+move, 50, 150+move, 150, fill="gray")
oval3 = canvas.create_oval(50+move*2, 50, 150+move*2, 150, fill="gray")
oval4 = canvas.create_oval(50+move*3, 50, 150+move*3, 150, fill="gray")
oval5 = canvas.create_oval(50+move*4, 50, 150+move*4, 150, fill="gray")

# # Define the functions to change the color of the light bulbs
# def toggle_light_yellow(oval, button):
#     if canvas.itemcget(oval, "fill") == "gray":
#         canvas.itemconfig(oval, fill="yellow")
#         button.config(text="Turn Off")
#     else:
#         canvas.itemconfig(oval, fill="gray")
#         button.config(text="Turn On")

# Continuously update the image on the canvas
def open_camera(): 
    if cap.isOpened():
        success, img = cap.read()
        if success:
            img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
            img.flags.writeable = False
            results = hands.process(img)
            img.flags.writeable = True
            

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
                if handType[0] == 'Left':
                    if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]: fingers.append(1)
                    else: fingers.append(0)
                if handType[0] == 'Right':
                    if lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1]: fingers.append(1)
                    else: fingers.append(0)
                for id in range(1,5):
                    if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]: fingers.append(1)
                    else: fingers.append(0)
            
                #Turn light depends on fingers
                if fingers == [0,0,0,0,0]: print("All lights are out!")
                #YELLOW LIGHT
                if fingers[0]==1:
                    print("Yellow!")
                    if canvas.itemcget(oval1, "fill") == "gray":
                       canvas.itemconfig(oval1, fill="yellow")
                elif fingers[0]==0:
                    canvas.itemconfig(oval1, fill="gray")

                #RED LIGHT
                if fingers[1]==1:
                    print("Red!")
                    if canvas.itemcget(oval2, "fill") == "gray":
                       canvas.itemconfig(oval2, fill="red")
                elif fingers[1]==0:
                    canvas.itemconfig(oval2, fill="gray")
                
                #GREEN LIGHT
                if fingers[2]==1:
                    print("Green!")
                    if canvas.itemcget(oval3, "fill") == "gray":
                       canvas.itemconfig(oval3, fill="Green")
                elif fingers[2]==0:
                    canvas.itemconfig(oval3, fill="gray")

                #BLUE LIGHT
                if fingers[3]==1:
                    print("Blue!")
                    if canvas.itemcget(oval4, "fill") == "gray":
                       canvas.itemconfig(oval4, fill="Blue")
                elif fingers[3]==0:
                    canvas.itemconfig(oval4, fill="gray")

                #ORANGE LIGHT
                if fingers[4]==1:
                    print("Orange!")
                    if canvas.itemcget(oval5, "fill") == "gray":
                       canvas.itemconfig(oval5, fill="Orange")
                elif fingers[4]==0:
                    canvas.itemconfig(oval5, fill="gray")
            
            img = ImageTk.PhotoImage(image=Image.fromarray(img)) 
            label_widget['image'] = img
            label_widget.image = img 
    # Repeat the same process after every 10 seconds 
    label_widget.after(10, open_camera) 

open_camera()
app.resizable(False, False)
app.bind('<Escape>', lambda e: app.quit()) 
app.title("Light Bulb Simulation")
app.mainloop()
