class Hypothesis:
    def __init__(self, hypothesis, certain=0) -> None:
        self.hypthesis = hypothesis
        self.certain = certain

    def __str__(self):
        return 'Hypothesis: ' + str(self.hypthesis) + f' with {self.certain} certain'