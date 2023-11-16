from tkinter import *
import tkinter as tk
import os

def btn_light():
    print("Button light Clicked")
    os.system('python ./Light_Simulation.py')
    
def btn_mouse():
    print("Button mouse Clicked")
    
def btn_volume():
    print("Button volume Clicked")
    
def btn_fan():
    print("Button fan Clicked")
    os.system('python ./Fan_Simulation.py')


window = Tk()

window.geometry("450x400")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 400,
    width = 450,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"./GUI_cache/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_light,
    relief = "flat")

b0.place(
    x = 76, y = 65,
    width = 135,
    height = 135)

img1 = PhotoImage(file = f"./GUI_cache/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_volume,
    relief = "flat")

b1.place(
    x = 238, y = 65,
    width = 135,
    height = 135)

img2 = PhotoImage(file = f"./GUI_cache/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_mouse,
    relief = "flat")

b2.place(
    x = 76, y = 227,
    width = 135,
    height = 135)

img3 = PhotoImage(file = f"./GUI_cache/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_fan,
    relief = "flat")

b3.place(
    x = 238, y = 227,
    width = 135,
    height = 135)

canvas.create_text(
    225.0, 47.5,
    text = "Control it with just a Hand",
    fill = "#001739",
    font = ("BeVietnamPro-Bold", int(24.0)))

window.resizable(False, False)
window.title("Hand Gesture Controling")
window.mainloop()
