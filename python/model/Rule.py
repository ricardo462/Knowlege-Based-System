class Rule:
    def __init__(self, identifier: str, premise, conclusion) -> None:
        self.identifier = identifier
        self.premise = premise
        self.conclusion = conclusion
    
    def __repr__(self) -> str:
        return self.identifier


    def __str__(self):
        return f'Rule {self.identifier}:\n\t{str(self.premise)} \n \t\t {str(self.conclusion)}' 
    
if __name__ == 'main':
    from model.Premise import Premise
    from model.Clause import Clause

    c1 = Clause('animal tiene pelo')
    c2 = Clause('animal tiene plumas')

    p = Premise(c1, c2)

    R1 = Rule('R1', p, (('animal es mamífero', 0.8), ('animal es ave', -1.0), ('animal es reptil', -1.0)))
    print(R1)