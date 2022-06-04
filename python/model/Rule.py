from typing import List
from model.Hypothesis import Hypothesis

class Rule:
    def __init__(self, identifier: str, premise, conclusion: List[Hypothesis]) -> None:
        self.identifier = identifier
        self.premise = premise
        self.conclusion = conclusion
    
    def __repr__(self) -> str:
        return self.identifier

    def __str__(self):
        return f'Rule {self.identifier}:\n\t{str(self.premise)} \n \t\t {str(self.conclusion)}'

    def __contains__(self, triplet):
        for action in self.conclusion:
            if triplet in action:
                return True
        return False

    def get_vc(self, hypothesis):
        for action in self.conclusion:
            if hypothesis == action[0]:
                return action[1]
        return None
    
    def prove(self, vc):
        conclusion = []
        for action in self.conclusion:
            conclusion.append((action.prove(vc)))

        return conclusion