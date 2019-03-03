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

# From AIMA code (probability.py) - Fig. 14.2 - cancer example
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2})
    ])

# Compute P(Cancer | positive results on both tests).
print("\nP(Cancer | positive results on both tests)")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

# Compute P(Cancer | a positive result on test 1, but a negative result on test 2).
print("\nP(Cancer | a positive result on test 1, but a negative result on test 2)")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

'''
The results make sense. The probability of having cancer itself is quite low to start
out with (0.01 chance), so it would make sense that both of the probabilities that are
being calculated here that test if someone has cancer or not would turn out to be
false the majority of the time. In the first problem, both tests return true positives,
meaning that the person actually does have cancer. There is a 0.9 chance on both tests
that they will produce true positives, so the probability that someone actually has
cancer with both tests returning positive (0.17) will be higher than if one test gives
a true positive and the other gives a false positive (0.00565). Note that both numbers are
still quite low since the probability of getting cancer in general is low. One failed test
makes it 0.16435 less likely to have cancer from the probabilities computed (0.17-0.00565).
'''