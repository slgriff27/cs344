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

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# Compute P(Burglary | John and Mary both call).
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# See the explanation of the algorithms in AIMA Section 14.4.

###################################################################################################

# Compute P(Alarm | burglary and no earthquake).
# This problem did not take much computation since it was hard coded in the table itself.
print("\nP(Alarm | burglary and no earthquake)")
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# Compute P(John calling | burglary and no earthquake).
# This problem shows that John could or could not call if the alarm goes off, but the alarm may or may not go off even though there was a burglary and no earthquake.
print("\nP(John calling | burglary and no earthquake)")
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# Compute P(Burglary| alarm).
# This problem shows that an alarm doesn't just mean that a burglary happened; there could also be an earthquake or something totally unplanned.
print("\nP(Burglary| alarm)")
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())

# Compute P(Burglary| John and Mary both call).
# This problem shows that even if John and Mary call, it doesn't necessarily mean that there was a burglary.
print("\nP(Burglary| John and Mary both call)")
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
