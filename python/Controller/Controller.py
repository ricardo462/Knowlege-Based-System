from GUI.Greeting import Greeting
from GUI.Question import Question
from GUI.Result import Result

class Controller:
    def __init__(self, model, master, images) -> None:
        self.model = model
        self.model.set_controller(self)
        self.root = master
        self.images = images
        self.current_answer = None
        self.results = None
        
    def make_greeting(self):
        Greeting(self.root, self).mainloop()

    def make_question(self, question):
        Question(self.root, question, self).mainloop()

    def make_results(self):
        for result in self.results:
            Result(self.root, result, self.images[result[0]])
        
    def receive_answer(self, answer):
        self.current_answer = answer

    def get_answer(self):
        return self.current_answer

    def run(self):
        self.results = self.model.run()