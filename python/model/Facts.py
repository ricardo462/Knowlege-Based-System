from typing import List
from model.Hypothesis import Hypothesis
from model.Rule import Rule
from utils import min_modified, max_modified

class Facts:
    def __init__(self, alpha, beta, gamma, delta, epsilon, early_stopping, high_level_hypotheses=None, facts=[]) -> None:
        self.facts = facts
        self.high_level_hypotheses = high_level_hypotheses
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.epsilon = epsilon
        self.early_stopping = early_stopping

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

    def add(self, fact:Hypothesis) -> None:
        if fact.triplet in self:
            for index, fact_ in enumerate(self.facts):
                if fact == fact_:
                    self.facts[index].set_vc(max_modified([fact.certain, fact_.certain])) 
        
        else:
            self.facts.append(fact)

    def delta_premise(self, vc:float):
        return self.delta/vc

    def get_useful_fact(self, triplet:str):
        for fact in self.facts:
            if triplet in self and abs(fact) > self.beta:
                return fact
        return None

    # Esto se puede hacer más bonito, pero debería funcionar
    def get_vc_hypothesis(self, triplet):
        if triplet in self:
            for fact in self.facts:
                if triplet == fact.triplet:
                    return fact.certain
        else:
            return 0.0

    #esto retorna el mínimo vc de las clausulas para comprobar una regla
    def get_vc_premise(self, rule):
        premise = rule.premise
        VC = []
        for clause in premise:
            vc = self.get_vc_hypothesis(clause)
            if vc != 0.0:
                VC.append(vc)
            else:
                return None

        return min_modified(VC)

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

    def get_high_level_facts(self) -> List[Hypothesis]:
        high_level_facts = []
        
        for high_level_hypothesis in self.high_level_hypotheses:
            if high_level_hypothesis in self:
                high_level_facts.append((high_level_hypothesis, 
                round(self.get_vc_hypothesis(high_level_hypothesis), 2)))

        return high_level_facts

    
    
    def get_conclusive_high_level_premise(self) -> Hypothesis:
        high_level_facts = self.get_high_level_facts()
        conclusive_premises = []
        for fact in high_level_facts:
            if fact[1] >= self.alpha:
                conclusive_premises.append(fact)

        return conclusive_premises

    def reset(self):
        self.facts = []


    def set_parameters(self, alpha, beta, gamma, delta, epsilon, early_stopping):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.epsilon = epsilon
        self.early_stopping = early_stopping

    def get_parameters(self):
        return [self.alpha, self.beta, self.gamma, self.delta, self.epsilon]

    def improvable(self, hypothesis) -> bool: 
        if self.get_vc_hypothesis(hypothesis) < self.gamma:
            return True
        return False