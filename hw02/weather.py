'''
This module implements the Bayesian network.
It's taken from the AIMA Python code.

@author: slg27
@date: March 8, 2019
'''

from probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - weather example
weather = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy', {T: 0.1, F: 0.5}),
    ('Rain', 'Cloudy', {T: 0.8, F: 0.2}),
    ('Wet Grass', 'Sprinkler Rain', {(T, T): 0.99, (T, F): 0.9, (F, T): 0.9, (F, F): 0.0})
    ])

# Compute P(Cloudy).
print(enumeration_ask('Cloudy', dict(), weather).show_approx())

# Compute P(Sprinkler | cloudy).
print(enumeration_ask('Sprinkler', dict(Cloudy=T), weather).show_approx())

# Compute P(Cloudy | the sprinkler is running and it’s not raining).
print(enumeration_ask('Cloudy', dict(Sprinkler=T, Rain=F), weather).show_approx())

# Compute P(Wet Grass | it’s cloudy, the sprinkler is running and it’s raining).
print(enumeration_ask('Wet Grass', dict(Cloudy=T, Sprinkler=T, Rain=T), weather).show_approx())

# Compute P(Cloudy | the grass is not wet).
print(enumeration_ask('Cloudy', dict(WetGrass=F), weather).show_approx())
