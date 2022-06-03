from Statement import Statement
class Hypothesis(Statement):
    def __init__(self, hypothesis, certain=0) -> None:
        super().__init__(hypothesis, certain)

    def __str__(self):
        return 'Hypothesis: ' + str(self.triplet) + f' with {self.certain} certain'