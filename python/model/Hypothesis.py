class Hypothesis:
    def __init__(self, triplet, certain=0) -> None:
        self.triplet = triplet
        self.certain = float(certain)

    def __str__(self):
        return 'Hypothesis: ' + str(self.triplet) + f' with {self.certain} certain'

    def __repr__(self):
        return 'Hypothesis: ' + str(self.triplet) + f' with {self.certain} certain'

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Hypothesis):
            return __o.triplet == self.triplet and __o.certain == self.certain
        
        return False

    def __contains__(self, item):
        if item == self.triplet:
            return True
        return False

    def __abs__(self):
        return abs(self.certain)

    def prove(self, vc):
        return Hypothesis(self.triplet, vc * self.certain)

    def set_vc(self, vc):
        self.certain = vc