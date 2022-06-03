from model.Statement import Statement

class Action(Statement):
    def __init__(self, triplet, certain=0) -> None:
        super().__init__(triplet, certain)

    def __str__(self):
        return 'Action: ' + str(self.triplet) + f' with {self.certain} certain'