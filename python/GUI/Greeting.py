import tkinter as tk
from tkinter import ttk

class Greeting(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.root = master
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        ttk.Label(frm, text="Welcome to the Knowlege Base System").grid(column=0, row=0)
        ttk.Label(frm, text='Think aobut an animal in this list:').grid(column=0, row=1)
        ttk.Label(frm, text='Dog, Bat, Tiger, Elephant, Zebra, Giraffe, Turttle, Cheetah, Seagull, Ostrich, Parrot').grid(column=0, row=2)
        ttk.Label(frm, text='Ready?:').grid(column=0, row=3)
        ttk.Button(frm, text='Ready', command=frm.destroy).grid(column=0, row=4)

root = tk.Tk()
myapp = Greeting(root)
myapp.mainloop()