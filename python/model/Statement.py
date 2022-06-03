class Statement:
    def __init__(self, triplet, certain=0) -> None:
        self.triplet = triplet
        self.certain = certain

    def __str__(self):
        return 'Statement: ' + str(self.triplet) + f' with {self.certain} certain'