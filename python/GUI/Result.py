import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os

from numpy import size


class Result(tk.Frame):
    def __init__(self, master, animal, image_path):
        super().__init__(master)
        self.root = master
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        ### Result ###
        ttk.Label(frm, text=f'Your animal is a {animal[0]} with {animal[1]} certain').grid(column=0, row=0) 

        ### Image ###
        image = Image.open(image_path)
        #print(image.size)
        resized_image = image.resize((400, 205))
        test = ImageTk.PhotoImage(resized_image)

        label = ttk.Label(frm, image=test)
        label.image = test

        # Position image
        label.grid(column=0, row=1)

        ### Next step ###
        bttn_frm = ttk.Frame(frm, padding=10)
        bttn_frm.grid()
        bttn_frm.grid(column=0, row=2)
        ttk.Button(bttn_frm, text='Try again', command=frm.destroy).grid(column=0, row=0)
        ttk.Button(bttn_frm, text='Close', command=frm.destroy).grid(column=1, row=0)

if __name__ == '__main__':
    dir = os.path.abspath(__file__)
    dname = os.path.dirname(dir)
    dname = os.path.dirname(dname)
    dname = os.path.dirname(dname)

    cheetah = 'animal es cheetah'
    tigre = 'animal es tigre'
    perro = 'animal es perro'
    tortuga = 'animal es tortuga'
    jirafa = 'animal es jirafa'
    cebra = 'animal es cebra'
    murcielago = 'animal es murciélago'
    gaviota = 'animal gaviota'
    avestruz = 'animal es avestruz'
    loro = 'animal es loro'
    elefante = 'animal es elefante'

    images = {perro:'dog.jpeg',
            murcielago:'bat.jpeg',
            tigre:'tiger.jpeg',
            elefante:'elephant.jpeg',
            cebra:'zebra.jpeg',
            jirafa:'giraffe.jpeg', 
            tortuga:'turttle.jpeg',
            cheetah:'cheetah.jpeg',
            gaviota:'seagull.jpeg',
            avestruz:'ostrich.jpeg',
            loro:'parrot.jpeg'}

    for element in images: 
        file = images[element]     
        root = tk.Tk()
        root.title('knowlege Based System')
        image_path = '/resources/' + file
        myapp = Result(root, [element, 0.85], dname + image_path)
        myapp.mainloop()