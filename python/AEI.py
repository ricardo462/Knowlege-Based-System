import json

from model.Rule import Rule
from model.Hypothesis import Hypothesis
from model.Facts import Facts
from utils import *

PARAMETERS_PAHT = 'python/parameters.json'


with open(PARAMETERS_PAHT) as json_file:
    data = json.load(json_file)

epsilon = data['epsilon']
beta = data['beta']

##### Rules #####
pelo = 'animal tiene pelo'
leche = 'animal da leche'
huevos = 'animal pone huevos'
piel_dura = 'animal tiene piel dura'
volar = 'animal puede volar'
plumas = 'animal tiene plumas'
carne = 'animal come carne'
garras = 'animal tiene garras'
mamifero = 'animal es mamífero'
pezunas = 'animal tiene pezuñas'
rumiante = 'animal es rumiante'
personas = 'animal vive con personas'
zoologico = 'animal vive en el zoológico'
carnivoro = 'animal es carnívoro'
manchas = 'animal tiene manchas oscuras'
domestico = 'animal es doméstico'
ungulado = 'animal es ungulado'
cuello_largo = 'animal tiene cuello largo'
rayas_negras = 'animal tiene rayas negras'
feo = 'animal es feo'
ave = 'animal es ave'
vuela_bien = 'animal vuela bien'
corre_rapido = 'animal corre rápido'
parlanchin = 'animal es parlanchín'
grande = 'animal es grande'
trompa = 'animal tiene trompa'
reptil = 'animal es reptil'


cheetah = 'animal es cheetah'
tigre = 'animal es tigre'
perro = 'animal es perro'
tortuga = 'animal es tortuga'
jirafa = 'animal es jirafa'
cebra = 'animal es cebra'
murcielago = 'animal es murciélago'
gaviota = 'animal gaviota'
avestruz = 'animal es avestruz'
loro = 'animal es loro'
elefante = 'animal es elefante'



R1 = Rule('R1', [pelo], 
                [Hypothesis(mamifero, 0.8), Hypothesis(ave, -1.0), Hypothesis(reptil, -1.0)])

R2 = Rule('R2', [leche], 
                [Hypothesis(mamifero, 1.0), Hypothesis(ave, -1.0), Hypothesis(reptil, -1.0)])

R3 = Rule('R3', [huevos, piel_dura], 
                [Hypothesis(mamifero, -1.0), Hypothesis(ave, -1.0), Hypothesis(reptil, 1.0)])

R4 = Rule('R4', [huevos, volar], 
                [Hypothesis(ave, 1.0), Hypothesis(reptil, -1.0)])

R5 = Rule('R5', [plumas], 
                [Hypothesis(mamifero, -1.0), Hypothesis(ave, 1.0), Hypothesis(reptil, -1.0)])

R6 = Rule('R6', [carne], 
                [Hypothesis(carnivoro, 1.0)])

R7 = Rule('R7', [garras], 
                [Hypothesis(carnivoro, 0.8)])

R8 = Rule('R8', [mamifero, pezunas],
                [Hypothesis(ungulado, 1.0)])

R9 = Rule('R9', [mamifero, rumiante], 
                [Hypothesis(ungulado, 0.75)])

R10 = Rule('R10', [personas],
                [Hypothesis(domestico, 0.9)])

R11 = Rule('R11', [zoologico], 
                [Hypothesis(domestico, -0.8)])

R12 = Rule('R12', [mamifero, carnivoro, manchas], 
                [Hypothesis(cheetah, 0.9)])

R13 = Rule('R13', [mamifero, carnivoro, rayas_negras], 
                [Hypothesis(tigre, 0.85)])

R14 = Rule('R14', [mamifero, carnivoro, domestico], 
                [Hypothesis(perro, 0.9)])

R15 = Rule('R15', [reptil, domestico], 
                [Hypothesis(tortuga, 0.7)])

R16 = Rule('R16', [mamifero, ungulado, cuello_largo], 
                [Hypothesis(jirafa, 1.0)])

R17 = Rule('R17', [mamifero, ungulado, rayas_negras], 
                [Hypothesis(cebra, 0.95)])

R18 = Rule('R18', [mamifero, volar, feo], 
                [Hypothesis(murcielago, 0.9)])

R19 = Rule('R19', [ave, vuela_bien],
                [Hypothesis(gaviota, 0.9)])

R20 = Rule('R20', [ave, corre_rapido], 
                [Hypothesis(avestruz, 1.0)])

R21 = Rule('R21', [ave, parlanchin], 
                [Hypothesis(loro, 0.95)])

R22 = Rule('R22', [mamifero, grande, ungulado, trompa],
                [Hypothesis(elefante, 0.9)])


rules = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22]
hypotheses = [Hypothesis(perro, 0.0), 
                Hypothesis(murcielago, 0.0),
                Hypothesis(tigre, 0.0), 
                Hypothesis(elefante, 0.0), 
                Hypothesis(cebra, 0.0), 
                Hypothesis(jirafa, 0.0), 
                Hypothesis(tortuga, 0.0), 
                Hypothesis(cheetah, 0.0), 
                Hypothesis(gaviota, 0.0), 
                Hypothesis(avestruz, 0.0), 
                Hypothesis(loro, 0.0)]

to_check = [perro] 
facts = Facts(beta)



def check_fact_base(rule, facts):
    premise = rule.premise
    VC = []
    for clause in premise:
        fact = facts.get_useful_fact(clause, facts)
        if fact:
            VC.append(fact.certain)
        else:
            VC.append(None)
            break
    if None not in VC:
        return min_modified(VC)

    return None


def question_rule_base():
    pass

def ask_user():
    pass


def AEI(hypothesis, facts, rules, current_rule=None):
    if current_rule:
        vc = check_fact_base(current_rule, facts)
        if vc:
            facts.append([hypothesis, vc])
            return

    relevant_rules = get_relevant_rules(hypothesis, rules)
    # asks to the user if an hypothesis can not be proved
    if relevant_rules == []:
        vc = float(input(f'Certain for {hypothesis}: '))
        # Checking if the vc of the action is greater than epsilon
        for action in current_rule.conclusion:
            vc_rule = action[1]
            if vc_rule >= epsilon:
                facts.append((hypothesis, vc * vc_rule))

    # Hypotheses are demonstrated recursively
    for rule in relevant_rules:
        premise = rule.premise        
        for clause in premise:
            AEI(clause, facts, rules, current_rule=rule)

    vc = check_fact_base(current_rule, facts)

#AEI(perro, facts, rules)
#print(facts)

facts.add(Hypothesis(pelo, 1))
facts.prove_rule(R1)
print(facts)