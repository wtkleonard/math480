# A hidden Markov model - a cooking family

# Consider a family with three members: mum, dad, and son.
# Each day, one of them will cook dinner. We model this as
# a Markov chain. (For example, mum cooks well and others 
# want her to continue cooking. Mum is lazy, so she urges
# others to cook when she is not cooking, etc...) Each of them
# has his/her favorite menu (modeled by a probability distribution).
# The output is the dishes made.

emission_symbols = ['steamed egg', 'steak', 'dumpling',
                    'pasta', 'baked chicken'] # I am hungry!

# transition matrix for cooker
A = matrix(RR, 3, [0.8, 0.05, 0.15,  # mum
                   0.4, 0.1, 0.4,    # dad does not like to cook
                   0.35, 0.05, 0.6]) # son cannot order dad

# favorite menus
B = matrix(RR, 3, 5, [0.3, 0.1, 0.2, 0.2, 0.2,   # mum can cook everything
                      0, 0.3, 0, 0.2, 0.5,       # dad has his perferences
                      0.4, 0.3, 0.1, 0.1, 0.1])  # son likes egg

# initial distribution
initial = [1, 0, 0]

# create model
model = hmm.DiscreteHiddenMarkovModel(A, B, initial, emission_symbols)
