from tkinter import *
from tkinter import ttk

class GUI:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('knowlege Based System')
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        ttk.Label(frm, text="Welcome to the Knowlege Base System").grid(column=0, row=0)
        ttk.Label(frm, text='Think aobut an animal in this list:').grid(column=0, row=1)
        ttk.Label(frm, text='Dog, Bat, Tiger, Elephant, Zebra, Giraffe, Turttle, Cheetah, Seagull, Ostrich, Parrot').grid(column=0, row=2)
        ttk.Label(frm, text='Ready?:').grid(column=0, row=3)
        ttk.Button(frm, text='Ready').grid(column=0, row=4)
    
    def loop(self):
        self.root.mainloop()