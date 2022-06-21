from GUI.Greeting import Greeting
from GUI.Question import Question
from GUI.Result import Result
import tkinter as tk

class Controller:
    def __init__(self, model, master, images) -> None:
        self.model = model
        self.model.set_controller(self)
        self.root = master
        self.images = images
        self.current_answer = None
        self.results = None
        
    def make_greeting(self, alpha, beta, gamma, delta, epsilon):
        Greeting(self.root, self, alpha, beta, gamma, delta, epsilon).mainloop()

    def make_question(self, question):
        Question(self.root, question, self).mainloop()

    def make_results(self):
        for result in self.results:
            Result(self.root, result, self.images[result[0]], self)
        
    def receive_answer(self, answer):
        self.current_answer = answer

    def get_answer(self):
        return self.current_answer

    def run(self):
        self.results = self.model.run()

    def try_again(self):
        self.model.reset()
        self.root.destroy()
        self.root = tk.Tk()
        self.make_greeting(*self.model.get_parameters())

    def set_parameters(self, alpha, beta, gamma, delta, epsilon, early_stopping):
        self.model.set_parameters(alpha, beta, gamma, delta, epsilon, early_stopping)