from model.Triplet import Triplet
class Clause(Triplet):
    def __init__(self, triplet) -> None:
        super().__init__(triplet)

    def __str__(self) -> str:
        return f'Clause: {self.triplet}'