from model.Facts import Facts
class HightLevelFacts_(Facts):
    def __init__(self, facts) -> None:
        super().__init__(None, None, None, None, facts)