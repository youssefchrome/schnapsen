import sys
from kb import KB, Boolean, Integer, Constant

# Define our propositional symbols
A0 = Boolean('A0')
A1 = Boolean('A1')
A2 = Boolean('A2')
A3 = Boolean('A3')
A4 = Boolean('A4')
A5 = Boolean('A5')
A6 = Boolean('A6')
A7 = Boolean('A7')
A8 = Boolean('A8')
A9 = Boolean('A9')
A10 = Boolean('A10')
A11 = Boolean('A11')
A12 = Boolean('A12')
A13 = Boolean('A13')
A14 = Boolean('A14')
A15 = Boolean('A15')
A16 = Boolean('A16')
A17 = Boolean('A17')
A18 = Boolean('A18')
A19 = Boolean('A19')
PA0 = Boolean('PA0')
PA1 = Boolean('PA1')
PA2 = Boolean('PA2')
PA3 = Boolean('PA3')
PA4 = Boolean('PA4')
PA5 = Boolean('PA5')
PA6 = Boolean('PA6')
PA7 = Boolean('PA7')
PA8 = Boolean('PA8')
PA9 = Boolean('PA9')
PA10 = Boolean('PA10')
PA11 = Boolean('PA11')
PA12 = Boolean('PA12')
PA13 = Boolean('PA13')
PA14 = Boolean('PA14')
PA15 = Boolean('PA15')
PA16 = Boolean('PA16')
PA17 = Boolean('PA17')
PA18 = Boolean('PA18')
PA19 = Boolean('PA19')

# Create a new knowledge base
kb = KB()

# GENERAL INFORMATION ABOUT THE CARDS
# This adds information which cards are Aces
kb.add_clause(A0)
kb.add_clause(A5)
kb.add_clause(A10)
kb.add_clause(A15)

# Add here whatever is needed for your strategy.
# DEFINITION OF THE STRATEGY
# Add clauses (This list is sufficient for this strategy)
kb.add_clause(~A0, PA0)
kb.add_clause(~A5, PA5)
kb.add_clause(~A10, PA10)
kb.add_clause(~A15, PA15)
kb.add_clause(~PA0, A0)
kb.add_clause(~PA5, A5)
kb.add_clause(~PA10, A10)
kb.add_clause(~PA15, A15)

# Add here other strategies
kb.add_clause(~A0)

# print all models of the knowledge base
for model in kb.models():
    print(model)

# print out whether the KB is satisfiable (if there are no models, it is not satisfiable)
print(kb.satisfiable())
