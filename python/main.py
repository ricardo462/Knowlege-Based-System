import json
from model.Clause import Clause
from model.Action import Action
from model.Rule import Rule

PARAMETERS_PAHT = 'python/parameters.json'


with open(PARAMETERS_PAHT) as json_file:
    data = json.load(json_file)


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



R1 = Rule('R1', (pelo), 
                [(mamifero, 0.8), (ave, -1.0), (reptil, -1.0)])

R2 = Rule('R2', (leche), 
                [(mamifero, 1.0), (ave, -1.0), (reptil, -1.0)])

R3 = Rule('R3', (huevos, piel_dura), 
                [(mamifero, -1.0), (ave, -1.0), (reptil, 1.0)])

R4 = Rule('R4', (huevos, volar), 
                [(ave, 1.0), (reptil, -1.0)])

R5 = Rule('R5', (plumas), 
                [(mamifero, -1.0), (ave, 1.0), (reptil, -1.0)])

R6 = Rule('R6', (carne), 
                [(carnivoro, 1.0)])

R7 = Rule('R7', (garras), 
                [(carnivoro, 0.8)])

R8 = Rule('R8', (mamifero, pezunas),
                [(ungulado, 1.0)])

R9 = Rule('R9', (mamifero, rumiante), 
                [(ungulado, 0.75)])

R10 = Rule('R10', (personas),
                [(domestico, 0.9)])

R11 = Rule('R11', (zoologico), 
                [(domestico, -0.8)])

R12 = Rule('R12', (mamifero, carnivoro, manchas), 
                [(cheetah, 0.9)])

R13 = Rule('R13', (mamifero, carnivoro, rayas_negras), 
                [(tigre, 0.85)])

R14 = Rule('R14', (mamifero, carnivoro, domestico), 
                [(perro, 0.9)])

R15 = Rule('R15', (reptil, domestico), 
                [(tortuga, 0.7)])

R16 = Rule('R16', (mamifero, ungulado, cuello_largo), 
                [(jirafa, 1.0)])

R17 = Rule('R17', (mamifero, ungulado, rayas_negras), 
                [(cebra, 0.95)])

R18 = Rule('R18', (mamifero, volar, feo), 
                [(murcielago, 0.9)])

R19 = Rule('R19', (ave, vuela_bien),
            [(gaviota, 0.9)])

R20 = Rule('R20', (ave, corre_rapido), 
                [(avestruz, 1.0)])

R21 = Rule('R21', (ave, parlanchin), 
                [(loro, 0.95)])

R22 = Rule('R22', (mamifero, grande, ungulado, trompa),
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

# Returns all the relevant rules that can prove an hypothesis
def get_relevant_rules(rules, hypothesis):
    relevant_rules = []
    for rule in rules:
        for conclusion in rule.conclusion:
            if hypothesis in conclusion:
                relevant_rules.append(rule)
    return relevant_rules

print(get_relevant_rules(rules, mamifero))
