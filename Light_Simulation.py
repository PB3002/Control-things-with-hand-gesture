import tkinter as tk

class LightBulb:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=200, height=200)
        self.canvas.pack()
        self.oval = self.canvas.create_oval(50, 50, 150, 150, fill="gray")
        self.button = tk.Button(master, text="Turn On", command=self.toggle_light)
        self.button.pack()

    def toggle_light(self):
        if self.canvas.itemcget(self.oval, "fill") == "gray":
            self.canvas.itemconfig(self.oval, fill="yellow")
            self.button.config(text="Turn Off")
        else:
            self.canvas.itemconfig(self.oval, fill="gray")
            self.button.config(text="Turn On")

root = tk.Tk()
root.title("Light Bulb Simulation") 
app = LightBulb(root)
root.mainloop()
