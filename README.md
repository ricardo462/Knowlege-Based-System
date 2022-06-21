# Knowlege-Based-System

The needed packages for this program are only the ones given by Python 3.

This is the implementation of a Knowlege Based System (KBS) with inverse chainning for the detection of an animal
that you are thinking of. The animals supported are: 

- Dog
- Bat
- Tiger
- Elephant
- Zebra
- Giraffe
- Turttle
- Cheetah 
- Seagull
- Ostrich
- Parrot

In order to discover what animal you are thinking about, the program uses the following rules:

- Rule R1:
        ['animal tiene pelo']
                 [Hypothesis: animal es mamífero with 0.8 certain, Hypothesis: animal es ave with -1.0 certain, Hypothesis: animal es reptil with -1.0 certain]  
- Rule R2:
        ['animal da leche']
                 [Hypothesis: animal es mamífero with 1.0 certain, Hypothesis: animal es ave with -1.0 certain, Hypothesis: animal es reptil with -1.0 certain]  
- Rule R3:
        ['animal pone huevos', 'animal tiene piel dura']
                 [Hypothesis: animal es mamífero with -1.0 certain, Hypothesis: animal es ave with -1.0 certain, Hypothesis: animal es reptil with 1.0 certain]  
- Rule R4:
        ['animal pone huevos', 'animal puede volar']
                 [Hypothesis: animal es ave with 1.0 certain, Hypothesis: animal es reptil with -1.0 certain]
- Rule R5:
        ['animal tiene plumas']
                 [Hypothesis: animal es mamífero with -1.0 certain, Hypothesis: animal es ave with 1.0 certain, Hypothesis: animal es reptil with -1.0 certain]  
- Rule R6:
        ['animal come carne']
                 [Hypothesis: animal es carnívoro with 1.0 certain]
- Rule R7:
        ['animal tiene garras']
                 [Hypothesis: animal es carnívoro with 0.8 certain]
- Rule R8:
        ['animal es mamífero', 'animal tiene pezuñas']
                 [Hypothesis: animal es ungulado with 1.0 certain]
- Rule R9:
        ['animal es mamífero', 'animal es rumiante']
                 [Hypothesis: animal es ungulado with 0.75 certain]
- Rule R10:
        ['animal vive con personas']
                 [Hypothesis: animal es doméstico with 0.9 certain]
- Rule R11:
        ['animal vive en el zoológico']
                 [Hypothesis: animal es doméstico with -0.8 certain]
- Rule R12:
        ['animal es mamífero', 'animal es carnívoro', 'animal tiene manchas oscuras']
                 [Hypothesis: animal es cheetah with 0.9 certain]
- Rule R13:
        ['animal es mamífero', 'animal es carnívoro', 'animal tiene rayas negras']
                 [Hypothesis: animal es tigre with 0.85 certain]
- Rule R14:
        ['animal es mamífero', 'animal es carnívoro', 'animal es doméstico']
                 [Hypothesis: animal es perro with 0.9 certain]
- Rule R15:
        ['animal es reptil', 'animal es doméstico']
                 [Hypothesis: animal es tortuga with 0.7 certain]
- Rule R16:
        ['animal es mamífero', 'animal es ungulado', 'animal tiene cuello largo']
                 [Hypothesis: animal es jirafa with 1.0 certain]
- Rule R17:
        ['animal es mamífero', 'animal es ungulado', 'animal tiene rayas negras']
                 [Hypothesis: animal es cebra with 0.95 certain]
- Rule R18:
        ['animal es mamífero', 'animal puede volar', 'animal es feo']
                 [Hypothesis: animal es murciélago with 0.9 certain]
- Rule R19:
        ['animal es ave', 'animal vuela bien']
                 [Hypothesis: animal gaviota with 0.9 certain]
- Rule R20:
        ['animal es ave', 'animal corre rápido']
                 [Hypothesis: animal es avestruz with 1.0 certain]
- Rule R21:
        ['animal es ave', 'animal es parlanchín']
                 [Hypothesis: animal es loro with 0.95 certain]
- Rule R22:
        ['animal es mamífero', 'animal es grande', 'animal es ungulado', 'animal tiene trompa']
                 [Hypothesis: animal es elefante with 0.9 certain]

To run the program you have to run the file "main.py", then a window is displayed, where you have to set the following parameters:

- $\alpha$: parameter to determine when a high-level hypothesis has been proven
satisfactorily, so that it is not necessary to test another hypothesis
(assuming that these are mutually exclusive hypotheses).

- $\beta$: parameter to determine when a fact (or its negation) has a degree of
enough certainty to be useful in an inference.

- $\gamma$: parameter to determine when a fact (or its negation) has a degree of
enough certainty to not require more effort to improve your grade
of certainty.

- $\delta$: parameter to determine when a premise has a degree of certainty
Enough to trigger a rule. $\delta(rule) \in [\beta , \beta/\epsilon]$.

- $\epsilon$: parameter to determine when a rule has a degree of certainty
enough to infer a given hypothesis (or intermediate conclusion),
assuming the premise is fully satisfied.

After setting the parameters, the system is going to ask you questions about the animal that you are thinking about. Finally,
after answering all the necessary questions, a final view with the conclusions is displayed. 