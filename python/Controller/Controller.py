from GUI.Greeting import Greeting
from GUI.Question import Question
class Controller:
    def __init__(self, model=None, master=None) -> None:
        self.model = model
        self.root = master
        
    def make_greeting(self):
        Greeting(self.root, self).mainloop()

    def make_question(self, question):
        q = Question(self.root, question)
        q.mainloop()
    
    def ask(self):
        self.make_question('tas bien?')