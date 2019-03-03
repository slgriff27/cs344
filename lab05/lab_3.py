'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden, slg27
@version Jan 2, 2013
@date: 03/01/19
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - happiness example
happiness = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])

# Compute P(Raise | Sunny).
print("\nP(Raise | Sunny)")
print(enumeration_ask('Raise', dict(Sunny=T), happiness).show_approx())

# Compute P(Raise | Happy and Sunny).
print("\nP(Raise | Happy and Sunny)")
print(enumeration_ask('Raise', dict(Sunny=T, Happy=T), happiness).show_approx())

'''
The results make sense. The probability that you got a raise if it is sunny outside
is very low since these two conditions presumably have no affect on each other (they
are independent). That is why it will be false almost 100% of the time. The second
probability is that you got a raise if it is sunny outside and if you are happy. This
is like the last one in that it is highly unlikely that just because you are happy and
it is sunny that you got a raise. Again, the raise and the sunny condition should be
independent of one another, but the probability that you got a raise is a little bit 
higher if you are happy. However you could be happy about a lot of different things, 
including it being sunny outside. That is why the probability of getting a raise is
slightly higher in this instance than it is in the previous example.
'''

# Compute P(Raise | Happy).
print("\nP(Raise | Happy)")
print(enumeration_ask('Raise', dict(Happy=T), happiness).show_approx())

# Compute P(Raise | Happy and not Sunny).
print("\nP(Raise | Happy and not Sunny)")
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happiness).show_approx())

'''
The results make sense. The first probability is that you got a raise if you are
happy, which is highly unlikely. The probability that you got a raise is a little bit 
higher if you are happy. You don't necessarily have the sunny condition adding to the
probability of happiness, so it is more likely that the happiness is due to the raise
than it was in the previous example when it could have been a raise, sunny, or anything
else. That is why the probability of getting a raise is slightly higher in this instance
than it is in the previous example. The second probability is that you got a raise when
you were happy and when it was not sunny outside. This is the most likely problem to
result in a raise. If you are happy, and if it is for sure not because it is sunny since
it is not sunny, then you have a much higher probability of getting a raise because you 
have eliminated one of the causes of happiness, giving the "raise" cause more weight.
'''