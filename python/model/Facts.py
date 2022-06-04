from model.Hypothesis import Hypothesis
from model.Rule import Rule
from utils import min_modified, max_modified

class Facts:
    def __init__(self, beta, delta, epsilon, facts=[]) -> None:
        self.facts = facts
        self.beta = beta
        self.delta = delta
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
    
    """
    def add(self, fact:Hypothesis):
        # I didn't do an if else clause where wether the fact is in the list
        # beacause that implies that it has to do the same validation twice
        is_in = False
 
        for index, fact_ in enumerate(self.facts):
            if fact == fact_:
                self.facts[index].set_vc(max_modified([fact.certain, fact_.certain]))
                is_in = True
     
        if not is_in:
            self.facts.append(fact)
    """

    def add(self, fact:Hypothesis) -> None:
        if fact.triplet in self:
            for index, fact_ in enumerate(self.facts):
                if fact == fact_:
                    self.facts[index].set_vc(max_modified([fact.certain, fact_.certain])) 
        
        else:
            print('ingresando')
            self.facts.append(fact)

    def delta_premise(self, vc:float):
        return self.delta/vc

    def get_useful_fact(self, triplet:str):
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

    def prove_rule(self, rule:Rule):
        vc = self.get_vc_premise(rule)
        if vc:
            # checking the delta value
            if abs(vc) >= self.delta_premise(vc):
                conclusion = rule.prove(vc) 
                for action in conclusion:
                    # checking if the action can be considered as a rule
                    if abs(action) >= self.epsilon:
                        self.add(action)