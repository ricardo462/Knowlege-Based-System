from typing import List

from model.Hypothesis import Hypothesis
from model.Facts import Facts
from model.Rules import Rules
from utils import *

class AEI:
    def __init__(self, alpha, beta, gamma, delta, epsilon, early_stopping, rules: Rules, high_level_hypotheses: List[str]) -> None:
        ### Global variables ###
        self.rules = rules 
        self.facts = Facts(alpha, beta, gamma, delta, epsilon, early_stopping, high_level_hypotheses)
        self.high_level_hypotheses = high_level_hypotheses
        
        ### Controller ###
        self.controller = None

    def AEI_(self, triplet, facts:Facts, rules:Rules):
        # checking rules recursively
        relevant_rules = self.rules.get_relevant_rules(triplet)

        for rule in relevant_rules:
            facts.prove_rule(rule)

        for rule in relevant_rules:
            for action in rule.premise:
                if facts.improvable(action):
                    self.AEI_(action, self.facts, self.rules)

        # asking to the user if the hypothesis can not be proven
        if relevant_rules == [] and triplet not in facts:
            certain = self.ask(f'Certain for {triplet}? ')
            facts.add(Hypothesis(triplet, certain))

    def run(self):
        for triplet in self.high_level_hypotheses:
            self.AEI_(triplet, self.facts, self.rules)
            self.AEI_(triplet, self.facts, self.rules)
            self.AEI_(triplet, self.facts, self.rules)
            
            conclusive_hypotheses = self.facts.get_conclusive_high_level_premise()

            if conclusive_hypotheses:
                return conclusive_hypotheses
        return self.facts.get_high_level_facts()

    def ask(self, question):
        self.controller.make_question(question)

        answer = self.controller.get_answer()
        
        while answer == None:
            answer = self.controller.get_answer()

        return answer
        

    def set_controller(self, controller):
        self.controller = controller

    def reset(self):
        self.facts.reset()

    def set_parameters(self, alpha, beta, gamma, delta, epsilon, early_stopping):
        self.facts.set_parameters(alpha, beta, gamma, delta, epsilon, early_stopping)

    def get_parameters(self):
        return self.facts.get_parameters()