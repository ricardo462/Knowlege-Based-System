from model.Hypothesis import Hypothesis
from utils import min_modified

class Facts:
    def __init__(self, beta, epsilon, facts=[]) -> None:
        self.facts = facts
        self.beta = beta
        self.epsilon = epsilon

    def __contains__(self, triplet):
        for fact in self.facts:
            if triplet in fact:
                return True
        return False

    def __str__(self) -> str:
        text = 'Facts: '
        for fact in self.facts:
            text += f'\n\t{str(fact)}'
        return text

    def add(self, fact:Hypothesis):
        self.facts.append(fact)

    def get_useful_fact(self, triplet):
        for fact in self.facts:
            if triplet in self and abs(fact) > self.beta:
                return fact
        return None

    #esto retorna el mínimo vc de las clausulas para comprobar una regla
    def get_vc_premise(self, rule):
        premise = rule.premise
        VC = []
        for clause in premise:
            fact = self.get_useful_fact(clause)
            if fact:
                VC.append(fact.certain)
            else:
                VC.append(None)
                break
        if None not in VC:
            return min_modified(VC)

        return None

    def prove_rule(self, rule):
        vc = self.get_vc_premise(rule)
        if vc:
            conclusion = rule.prove(vc) 
            for action in conclusion:
                if abs(action) >= self.epsilon:
                    self.add(action)
        return None