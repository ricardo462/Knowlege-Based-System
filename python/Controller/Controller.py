from GUI.Greeting import Greeting
from GUI.Question import Question
class Controller:
    def __init__(self, model=None, master=None) -> None:
        self.model = model
        self.model.set_controller(self)
        self.root = master
        self.current_answer = None
        
    def make_greeting(self):
        Greeting(self.root, self).mainloop()

    def make_question(self, question):
        Question(self.root, question, self).mainloop()
        
        
    def receive_answer(self, answer):
        self.current_answer = answer

    def get_answer(self):
        return self.current_answer

    def run(self):
        self.model.run()