import json

from numpy import append
from model.Clause import Clause
from model.Action import Action
from model.Rule import Rule
from utils import *

PARAMETERS_PAHT = 'python/parameters.json'


with open(PARAMETERS_PAHT) as json_file:
    data = json.load(json_file)

epsilon = data['epsilon']
beta = data['beta']

###### Clauses #######
c_pelo = Clause('animal tiene pelo')
c_leche = Clause('animal da leche')
c_huevos = Clause('animal pone huevos')
c_piel_dura = Clause('animal tiene piel dura')
c_volar = Clause('animal puede volar')
c_plumas = Clause('animal tiene plumas')
c_carne = Clause('animal come carne')
c_garras = Clause('animal tiene garras')
c_mamifero = Clause('animal es mamífero')
c_pezunas = Clause('animal tiene pezuñas')
c_rumiante = Clause('animal es rumiante')
c_personas = Clause('animal vive con personas')
c_zoologico = Clause('animal vive en el zoológico')
c_carnivoro = Clause('animal es carnívoro')
c_manchas = Clause('animal tiene manchas oscuras')
c_domestico = Clause('animal es doméstico')
c_ungulado = Clause('animal es ungulado')
c_cuello_largo = Clause('animal tiene cuello largo')
c_rayas_negras = Clause('animal tiene rayas negras')
c_feo = Clause('animal es feo')
c_ave = Clause('animal es ave')
c_vuela_bien = Clause('animal vuela bien')
c_corre_rapido = Clause('animal corre rápido')
c_parlanchin = Clause('animal es parlanchín')
c_grande = Clause('animal es grande')
c_trompa = Clause('animal tiene trompa')
c_reptil = Clause('reptil')



###### Actions ######
a_mamifero = Action('animal es ')





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
                [(mamifero, 0.8), (ave, -1.0), (reptil, -1.0)])

R2 = Rule('R2', [leche], 
                [(mamifero, 1.0), (ave, -1.0), (reptil, -1.0)])

R3 = Rule('R3', [huevos, piel_dura], 
                [(mamifero, -1.0), (ave, -1.0), (reptil, 1.0)])

R4 = Rule('R4', [huevos, volar], 
                [(ave, 1.0), (reptil, -1.0)])

R5 = Rule('R5', [plumas], 
                [(mamifero, -1.0), (ave, 1.0), (reptil, -1.0)])

R6 = Rule('R6', [carne], 
                [(carnivoro, 1.0)])

R7 = Rule('R7', [garras], 
                [(carnivoro, 0.8)])

R8 = Rule('R8', [mamifero, pezunas],
                [(ungulado, 1.0)])

R9 = Rule('R9', [mamifero, rumiante], 
                [(ungulado, 0.75)])

R10 = Rule('R10', [personas],
                [(domestico, 0.9)])

R11 = Rule('R11', [zoologico], 
                [(domestico, -0.8)])

R12 = Rule('R12', [mamifero, carnivoro, manchas], 
                [(cheetah, 0.9)])

R13 = Rule('R13', [mamifero, carnivoro, rayas_negras], 
                [(tigre, 0.85)])

R14 = Rule('R14', [mamifero, carnivoro, domestico], 
                [(perro, 0.9)])

R15 = Rule('R15', [reptil, domestico], 
                [(tortuga, 0.7)])

R16 = Rule('R16', [mamifero, ungulado, cuello_largo], 
                [(jirafa, 1.0)])

R17 = Rule('R17', [mamifero, ungulado, rayas_negras], 
                [(cebra, 0.95)])

R18 = Rule('R18', [mamifero, volar, feo], 
                [(murcielago, 0.9)])

R19 = Rule('R19', [ave, vuela_bien],
            [(gaviota, 0.9)])

R20 = Rule('R20', [ave, corre_rapido], 
                [(avestruz, 1.0)])

R21 = Rule('R21', [ave, parlanchin], 
                [(loro, 0.95)])

R22 = Rule('R22', [mamifero, grande, ungulado, trompa],
                [(elefante, 0.9)])


rules = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22]
hypotheses = [(perro, 0.0), 
                (murcielago, 0.0),
                (tigre, 0.0), 
                (elefante, 0.0), 
                (cebra, 0.0), 
                (jirafa, 0.0), 
                (tortuga, 0.0), 
                (cheetah, 0.0), 
                (gaviota, 0.0), 
                (avestruz, 0.0), 
                (loro, 0.0)]

to_check = [perro] 
facts = []


def check(hypothesis, facts):
    for fact in facts:
        if hypothesis == fact[0] and abs(fact[1]) >= data['alpha']:
            return fact[1]

    return False


def get_hypothesis_in_facts(hypothesis, facts):
    for fact in facts:
        if hypothesis == fact[0] and abs(fact[1]) > beta:
            return hypothesis
    return None

def prove_rule(rule, facts):
    premise = rule.premise
    VC = []
    for clause in premise:
        fact = get_hypothesis_in_facts(clause, facts)
        if fact:
            VC.append(fact[1])
        else:
            VC.append(None)
            break
    if None not in VC:
        return min_modified(VC)

    return None
          
            

def fact_base(hypothesis, facts, rules):
    relevant_rules = get_relevant_rules(hypothesis, rules)
    VC = []
    for relevant_rule in relevant_rules:
        vc = prove_rule(relevant_rule, facts)
        if vc: 
            VC.append(vc)
    # aquí discriminar 


def demonstrate_hypothesis(hypothesis, facts, rules, current_rule=None):
    #print(f'Checking {hypothesis}')
    relevant_rules = get_relevant_rules(hypothesis, rules)
    # Ground cases

    # returns the certain if an hypothsis can be proved
    certain = check(hypothesis, facts)
    if certain:
        return  certain

    # asks to the user if an hypothesis can not be proved
    if relevant_rules == []:
        vc = float(input(f'Certain for {hypothesis}'))
        # Checking if the vc of the action is greater than epsilon
        for action in current_rule.conclusion:
            vc_rule = action[1]
            if vc_rule >= epsilon:
                facts.append((hypothesis, vc * vc_rule))

    # Hypotheses are demonstrated recursively
    for rule in relevant_rules:
        premise = rule.premise        
        for clause in premise:
            demonstrate_hypothesis(clause, facts, rules, current_rule=rule)

    # Demonstrate the hypothesis if it can be proved
    prove_rule(rule)

def AEI(hypothesis, facts, rules, current_rule=None):
    # Checking the base of rules
    relevant_rules = get_relevant_rules(hypothesis, rules)

    # asks to the user if an hypothesis can not be proved
    if relevant_rules == []:
        vc = float(input(f'Certain for {hypothesis}'))
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
    return prove_rule(relevant_rules[0], facts)



demonstrate_hypothesis(perro, facts, rules)
#print(facts)
