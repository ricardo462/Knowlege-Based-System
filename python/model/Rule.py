class Rule:
    def __init__(self, identifier: str, premise, conclusion) -> None:
        self.identifier = identifier
        self.premise = premise
        self.conclusion = conclusion


    def __str__(self):
        return f'Rule {self.identifier}:\n\t{str(self.premise)} \n \t\t {str(self.conclusion)}' 
    

from Premise import Premise
from Clause import Clause

c1 = Clause('animal tiene pelo')
c2 = Clause('animal tiene plumas')

p = Premise(c1, c2)

R1 = Rule('R1', p, (('animal es mamífero', 0.8), ('animal es ave', -1.0), ('animal es reptil', -1.0)))
print(R1)