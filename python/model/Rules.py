from typing import List
from model.Rule import Rule

class Rules:
    def __init__(self, *args:Rule) -> None:
        self.rules = list(args)

    def __str__(self):
        text = ''
        for rule in self.rules:
            text += f'{str(rule)}\n'
        return text

    def get_relevant_rules(self, triplet:str) -> List[Rule]:
        relevant_rules = []
        for rule in self.rules:
            if triplet in rule:
                relevant_rules.append(rule)

        return relevant_rules




