import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os


class Result(tk.Frame):
    def __init__(self, master, animals, image_path, controller):
        super().__init__(master)
        self.controller = controller 

        frm = ttk.Frame(master, padding=10)
        frm.grid()

        ### Directory ###
        dir = os.path.abspath(__file__)
        dname = os.path.dirname(dir)
        dname = os.path.dirname(dname)
        dname = os.path.dirname(dname)

        row = 0
        idx = 0
        for img, animal in enumerate(animals):
            image_frm = ttk.Frame(frm, padding=10)
            ### Result ###
            ttk.Label(image_frm, text=f'Your animal is a {animal[0]} with {animal[1]} certain').grid(column=0, row=0) 

            ### Image ###
            
            path = '/resources/' + image_path[img]
            image = Image.open(dname + path)
            resized_image = image.resize((300, 154))
            test = ImageTk.PhotoImage(resized_image)

            label = ttk.Label(image_frm, image=test)
            label.image = test

            # Position image
            label.grid(column=0, row=1)

            image_frm.grid(column=idx, row=row)
            idx += 1
            if idx // 3 == 1:
                row += 1
                idx = 0

        ### Next step ###
        bttn_frm = ttk.Frame(frm, padding=10)
        bttn_frm.grid(column=0, row=row + 1)
        ttk.Button(bttn_frm, text='Try again', command=self.try_again).grid(column=0, row=0)
        ttk.Button(bttn_frm, text='Close', command=master.destroy).grid(column=1, row=0)

    def try_again(self):
        self.controller.try_again()    


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