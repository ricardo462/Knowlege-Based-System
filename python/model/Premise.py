class Premise:
    def __init__(self, *args) -> None:
        self.premise = args

    def __str__(self) -> str:
        text = ''
        for clause in self.premise:
            text += f'\n\t{str(clause)}'
        return f'Premise: {text}'

if __name__ == '__main__':
    from model.Clause import Clause

    c1 = Clause('animal tiene pelo')
    c2 = Clause('animal tiene plumas')

    p = Premise(c1, c2)
    print(p)