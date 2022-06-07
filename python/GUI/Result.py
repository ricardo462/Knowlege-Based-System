import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os


class Result(tk.Frame):
    def __init__(self, master, animal, image_path):
        super().__init__(master)
        self.root = master
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        ### Question ###
        ttk.Label(frm, text=f'Your animal is a {animal[0]} with {animal[1]} certain').grid(column=0, row=0) 

        ### Image ###
        image1 = Image.open(image_path)
        test = ImageTk.PhotoImage(image1)

        label1 = ttk.Label(frm, image=test)
        label1.image = test

        # Position image
        label1.grid(column=0, row=1)

        ### Next step ###
        bttn_frm = ttk.Frame(frm, padding=10)
        bttn_frm.grid()
        bttn_frm.grid(column=0, row=2)
        ttk.Button(bttn_frm, text='Try again', command=frm.destroy).grid(column=0, row=0)
        ttk.Button(bttn_frm, text='Close', command=frm.destroy).grid(column=1, row=0)

dir = os.path.abspath(__file__)
dname = os.path.dirname(dir)
dname = os.path.dirname(dname)


root = tk.Tk()
root.title('knowlege Based System')
image_path = '/resources/dog.jpeg'
myapp = Result(root, ['Dog', 0.85], dname + image_path)
myapp.mainloop()