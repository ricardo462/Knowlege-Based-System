class Hypothesis:
    def __init__(self, triplet, certain=0) -> None:
        self.triplet = triplet
        self.certain = certain

    def __str__(self):
        return 'Hypothesis: ' + str(self.triplet) + f' with {self.certain} certain'

    def __contains__(self, item):
        if item == self.triplet:
            return True
        return False

    def __abs__(self):
        return abs(self.certain)

    def prove(self, vc):
        return Hypothesis(self.triplet, vc * self.certain)