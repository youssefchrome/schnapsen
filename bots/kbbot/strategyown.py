import kb, sys
from kb import KB, Boolean, Integer, Constant

# Define our propositional symbols
J0 = Boolean('j0')
J1 = Boolean('j1')
J2 = Boolean('j2')
J3 = Boolean('j3')
J4 = Boolean('j4')
J5 = Boolean('j5')
J6 = Boolean('j6')
J7 = Boolean('j7')
J8 = Boolean('j8')
J9 = Boolean('j9')
J10 = Boolean('j10')
J11 = Boolean('j11')
J12 = Boolean('j12')
J13 = Boolean('j13')
J14 = Boolean('j14')
J15 = Boolean('j15')
J16 = Boolean('j16')
J17 = Boolean('j17')
J18 = Boolean('j18')
J19 = Boolean('j19')
PJ0 = Boolean('pj0')
PJ1 = Boolean('pj1')
PJ2 = Boolean('pj2')
PJ3 = Boolean('pj3')
PJ4 = Boolean('pj4')
PJ5 = Boolean('pj5')
PJ6 = Boolean('pj6')
PJ7 = Boolean('pj7')
PJ8 = Boolean('pj8')
PJ9 = Boolean('pj9')
PJ10 = Boolean('pj10')
PJ11 = Boolean('pj11')
PJ12 = Boolean('pj12')
PJ13 = Boolean('pj13')
PJ14 = Boolean('pj14')
PJ15 = Boolean('pj15')
PJ16 = Boolean('pj16')
PJ17 = Boolean('pj17')
PJ18 = Boolean('pj18')
PJ19 = Boolean('pj19')

Q0 = Boolean('Q0')
Q1 = Boolean('Q1')
Q2 = Boolean('Q2')
Q3 = Boolean('Q3')
Q4 = Boolean('Q4')
Q5 = Boolean('Q5')
Q6 = Boolean('Q6')
Q7 = Boolean('Q7')
Q8 = Boolean('Q8')
Q9 = Boolean('Q9')
Q10 = Boolean('Q10')
Q11 = Boolean('Q11')
Q12 = Boolean('Q12')
Q13 = Boolean('Q13')
Q14 = Boolean('Q14')
Q15 = Boolean('Q15')
Q16 = Boolean('Q16')
Q17 = Boolean('Q17')
Q18 = Boolean('Q18')
Q19 = Boolean('Q19')
PQ0 = Boolean('PQ0')
PQ1 = Boolean('PQ1')
PQ2 = Boolean('PQ2')
PQ3 = Boolean('PQ3')
PQ4 = Boolean('PQ4')
PQ5 = Boolean('PQ5')
PQ6 = Boolean('PQ6')
PQ7 = Boolean('PQ7')
PQ8 = Boolean('PQ8')
PQ9 = Boolean('PQ9')
PQ10 = Boolean('PQ10')
PQ11 = Boolean('PQ11')
PQ12 = Boolean('PQ12')
PQ13 = Boolean('PQ13')
PQ14 = Boolean('PQ14')
PQ15 = Boolean('PQ15')
PQ16 = Boolean('PQ16')
PQ17 = Boolean('PQ17')
PQ18 = Boolean('PQ18')
PQ19 = Boolean('PQ19')

K0 = Boolean('K0')
K1 = Boolean('K1')
K2 = Boolean('K2')
K3 = Boolean('K3')
K4 = Boolean('K4')
K5 = Boolean('K5')
K6 = Boolean('K6')
K7 = Boolean('K7')
K8 = Boolean('K8')
K9 = Boolean('K9')
K10 = Boolean('K10')
K11 = Boolean('K11')
K12 = Boolean('K12')
K13 = Boolean('K13')
K14 = Boolean('K14')
K15 = Boolean('K15')
K16 = Boolean('K16')
K17 = Boolean('K17')
K18 = Boolean('K18')
K19 = Boolean('K19')
PK0 = Boolean('PK0')
PK1 = Boolean('PK1')
PK2 = Boolean('PK2')
PK3 = Boolean('PK3')
PK4 = Boolean('PK4')
PK5 = Boolean('PK5')
PK6 = Boolean('PK6')
PK7 = Boolean('PK7')
PK8 = Boolean('PK8')
PK9 = Boolean('PK9')
PK10 = Boolean('PK10')
PK11 = Boolean('PK11')
PK12 = Boolean('PK12')
PK13 = Boolean('PK13')
PK14 = Boolean('PK14')
PK15 = Boolean('PK15')
PK16 = Boolean('PK16')
PK17 = Boolean('PK17')
PK18 = Boolean('PK18')
PK19 = Boolean('PK19')

C0 = Boolean('C0')
C1 = Boolean('C1')
C2 = Boolean('C2')
C3 = Boolean('C3')
C4 = Boolean('C4')
C5 = Boolean('C5')
C6 = Boolean('C6')
C7 = Boolean('C7')
C8 = Boolean('C8')
C9 = Boolean('C9')
C10 = Boolean('C10')
C11 = Boolean('C11')
C12 = Boolean('C12')
C13 = Boolean('C13')
C14 = Boolean('C14')
C15 = Boolean('C15')
C16 = Boolean('C16')
C17 = Boolean('C17')
C18 = Boolean('C18')
C19 = Boolean('C19')
PC0 = Boolean('PC0')
PC1 = Boolean('PC1')
PC2 = Boolean('PC2')
PC3 = Boolean('PC3')
PC4 = Boolean('PC4')
PC5 = Boolean('PC5')
PC6 = Boolean('PC6')
PC7 = Boolean('PC7')
PC8 = Boolean('PC8')
PC9 = Boolean('PC9')
PC10 = Boolean('PC10')
PC11 = Boolean('PC11')
PC12 = Boolean('PC12')
PC13 = Boolean('PC13')
PC14 = Boolean('PC14')
PC15 = Boolean('PC15')
PC16 = Boolean('PC16')
PC17 = Boolean('PC17')
PC18 = Boolean('PC18')
PC19 = Boolean('PC19')




# Create a new knowledge base
kb = KB()

# GENERAL INFORMATION ABOUT THE CARDS

kb.add_clause(J4)
kb.add_clause(J9)
kb.add_clause(J14)
kb.add_clause(J19)
kb.add_clause(Q3)
kb.add_clause(Q8)
kb.add_clause(Q13)
kb.add_clause(Q18)
kb.add_clause(K2)
kb.add_clause(K7)
kb.add_clause(K12)
kb.add_clause(K17)
# Add here whatever is needed for your strategy.

# DEFINITION OF THE STRATEGY
# Add clauses (This list is sufficient for this strategy)
# PC is the strategy to play cheap cards  first.
kb.add_clause(~J4,C4)
kb.add_clause(~J9,C9)
kb.add_clause(~J14,C14)
kb.add_clause(~J19,C19)

kb.add_clause(~Q3,C3)
kb.add_clause(~Q8,C8)
kb.add_clause(~Q13,C13)
kb.add_clause(~Q18,C18)

kb.add_clause(~K2,C2)
kb.add_clause(~K7,C7)
kb.add_clause(~K12,C12)
kb.add_clause(~K17,C17)

kb.add_clause(~C2, PC2)
kb.add_clause(~C3, PC3)
kb.add_clause(~C4, PC4)
kb.add_clause(~C7, PC7)
kb.add_clause(~C8, PC8)
kb.add_clause(~C9, PC9)
kb.add_clause(~C12, PC12)
kb.add_clause(~C13, PC13)
kb.add_clause(~C14, PC14)
kb.add_clause(~C17, PC17)
kb.add_clause(~C18, PC18)
kb.add_clause(~C19, PC19)

kb.add_clause(~PC2, C2)
kb.add_clause(~PC3, C3)
kb.add_clause(~PC4, C4)
kb.add_clause(~PC7, C7)
kb.add_clause(~PC8, C8)
kb.add_clause(~PC9, C9)
kb.add_clause(~PC12, C12)
kb.add_clause(~PC13, C13)
kb.add_clause(~PC14, C14)
kb.add_clause(~PC17, C17)
kb.add_clause(~PC18, C18)
kb.add_clause(~PC19, C19)







# print all models of the knowledge base
for model in kb.models():
    print(model)

# print out whether the KB is satisfiable (if there are no models, it is not satisfiable)
print(kb.satisfiable())