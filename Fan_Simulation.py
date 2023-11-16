from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

class App:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()

        self.image = Image.open("./fan.gif")
        self.photo = ImageTk.PhotoImage(self.image)

        self.label = Label(self.frame, image=self.photo)
        self.label.pack()

        self.freeze_button = Button(self.frame, text="Freeze", command=self.freeze_gif)
        self.freeze_button.pack(side=LEFT)

        self.unfreeze_button = Button(self.frame, text="Unfreeze", command=self.unfreeze_gif)
        self.unfreeze_button.pack(side=LEFT)

        self.is_paused = False

    def freeze_gif(self):
        self.is_paused = True

    def unfreeze_gif(self):
        self.is_paused = False
        self.animate()

    def animate(self):
        if not self.is_paused:
            try:
                self.image.seek(self.image.tell() + 1)
            except EOFError:
                self.image.seek(0)
            self.photo = ImageTk.PhotoImage(self.image)
            self.label.configure(image=self.photo)
            self.master.after(50, self.animate)

root = tk.Tk()
root.title("Fan Simulation") 
app = App(root)
root.mainloop()
