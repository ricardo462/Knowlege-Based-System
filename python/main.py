if __name__ == '__main__':
    from Controller.Controller import Controller
    import tkinter as tk
    from tkinter import ttk
    
    root = tk.Tk()
    controller = Controller(master =root)
    controller.make_greeting()
