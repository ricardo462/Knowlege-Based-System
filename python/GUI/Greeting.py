import tkinter as tk
from tkinter import ttk

class Greeting(tk.Frame):
    def __init__(self, master, controller, alpha, beta, gamma, delta, epsilon):
        super().__init__(master)
        self.root = master
        self.controller = controller

        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        ttk.Label(frm, text="Welcome to the Knowlege Base System").grid(column=0, row=0)
        ttk.Label(frm, text='Think aobut an animal in this list:').grid(column=0, row=1)
        ttk.Label(frm, text='Dog, Bat, Tiger, Elephant, Zebra, Giraffe, Turttle, Cheetah, Seagull, Ostrich, Parrot').grid(column=0, row=2)
        ttk.Label(frm, text='Ready?:').grid(column=0, row=3)
        

        ### Settings frame ###
        settings_frame = ttk.Frame(frm, padding=10)
        settings_frame.grid(column=0, row=4)
        ttk.Label(settings_frame, text='alpha: ').grid(column=0, row=0)
        self.alpha = self.get_entry(settings_frame, alpha)
        self.alpha.grid(column=1, row=0)

        ttk.Label(settings_frame, text='beta: ').grid(column=0, row=1)
        self.beta = self.get_entry(settings_frame, beta)
        self.beta.grid(column=1, row=1)

        ttk.Label(settings_frame, text='gamma: ').grid(column=0, row=2)
        self.gamma = self.get_entry(settings_frame, gamma)
        self.gamma.grid(column=1, row=2)

        ttk.Label(settings_frame, text='delta: ').grid(column=0, row=3)
        self.delta = self.get_entry(settings_frame, delta)
        self.delta.grid(column=1, row=3)

        ttk.Label(settings_frame, text='epsilon: ').grid(column=0, row=4)
        self.epsilon = self.get_entry(settings_frame, epsilon)
        self.epsilon.grid(column=1, row=4)

        ttk.Label(settings_frame, text='Early stopping').grid(column=0, row=5)
        self.early_stopping = ttk.Combobox(settings_frame, state = 'readonly', values=[True, False])
        self.early_stopping.current(0)
        self.early_stopping.grid(column=1, row=5)

        ttk.Button(frm, text='Ready', command=self.destroy_greeting).grid(column=0, row=5)

        self.frm = frm
        

        

    def destroy_greeting(self):
        early_stopping = True if self.early_stopping.get() == 'True' else False
        
        
        self.controller.set_parameters(float(self.alpha.get()), 
                                        float(self.beta.get()), 
                                        float(self.gamma.get()), 
                                        float(self.delta.get()), 
                                        float(self.epsilon.get()), 
                                        bool(self.early_stopping.get()))
        self.frm.destroy()
        self.controller.run()
        self.controller.make_results()

    def get_entry(self, frame, text) -> ttk.Entry:
        entry = ttk.Entry(frame)
        entry.insert(0, text)
        return entry


if __name__ == '__name__':
    root = tk.Tk()
    myapp = Greeting(root)
    myapp.mainloop()