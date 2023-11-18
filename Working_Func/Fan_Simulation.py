from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import mediapipe as mp

#Mediapipe API
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

tipIds = [4,8,12,16,20]
hands =  mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7,max_num_hands=1)

app = tk.Tk()  
cap = cv2.VideoCapture(0)
cap.set(3,400)
cap.set(4,300)

label_widget = tk.Label(app) 
label_widget.pack() 

class Fan:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()

        self.image = Image.open("./GUI_cache/fan.gif")
        self.photo = ImageTk.PhotoImage(self.image)

        self.label = Label(self.frame, image=self.photo)
        self.label.pack()

        self.freeze_button = Button(self.frame, text="Freeze", command=self.freeze_gif)
        self.freeze_button.pack(side=LEFT)

        self.unfreeze_button = Button(self.frame, text="Unfreeze", command=self.unfreeze_gif)
        self.unfreeze_button.pack(side=LEFT)

        self.is_paused = False

    def hide_all_button(self):
        self.freeze_button.pack_forget()
        self.unfreeze_button.pack_forget()

    def freeze_gif(self):
        self.is_paused = True
        self.freeze_button.config(state=DISABLED)
        self.unfreeze_button.config(state=NORMAL)

    def unfreeze_gif(self):
        self.is_paused = False
        self.freeze_button.config(state=NORMAL)
        self.unfreeze_button.config(state=DISABLED)
        self.animate()

    def animate(self):
        if not self.is_paused:
            try:
                self.image.seek(self.image.tell() + 2)
            except EOFError:
                self.image.seek(0)
            self.photo = ImageTk.PhotoImage(self.image)
            self.label.configure(image=self.photo)
            self.master.after(50, self.animate)

    def open_camera(self): 
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
                    total = fingers.count(1)
                
                    if total == 5: 
                        self.unfreeze_button.invoke()
                    else: 
                        self.freeze_button.invoke()

                img = ImageTk.PhotoImage(image=Image.fromarray(img)) 
                label_widget['image'] = img
                label_widget.image = img 
                # Repeat the same process after every 10 seconds 
                label_widget.after(10, self.open_camera) 


app.resizable(False, False)
app.bind('<Escape>', lambda e: app.quit()) 
app.title("Fan Simulation") 
fan = Fan(app)
fan.hide_all_button()
fan.open_camera()
app.mainloop()
