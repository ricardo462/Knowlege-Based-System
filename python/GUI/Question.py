import tkinter as tk
from tkinter import ttk


class Question(tk.Frame):
    def __init__(self, master, question, number=1):
        super().__init__(master)
        self.root = master
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        ### Question ###
        ttk.Label(frm, text=f'Question {number}: {question}').grid(column=0, row=0)

        ### Sacle bar ###
        bar_frm = ttk.Frame(frm, padding=10)
        bar_frm.grid()
        bar_frm.grid(column=0, row=1)
        ttk.Label(bar_frm, text='No').grid(column=0, row=0)
        ttk.Scale(bar_frm, value=0.5).grid(column=1, row=0)
        ttk.Label(bar_frm, text='Yes').grid(column=2, row=0)

        ### Confirmation ###
        ttk.Button(frm, text='Next Question', command=frm.destroy).grid(column=0, row=2)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('knowlege Based System')
    myapp = Question(root, 'The animal that you are thinking of has hair?')
    myapp.mainloop()