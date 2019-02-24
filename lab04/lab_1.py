'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden & Sarah Griffioen (slg27)
@version Feb 23. 2019
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print(PC.show_approx())

#Below is the calculation for P(Cavity|Catch) done by hand.
'''
The approach below uses a joint probability distribution to find
the probabilities of having a cavity given that you already had a
catch. There are two probabilities that need to be calculated as 
part of the set for the probability distribution: the probability
of a cavity given a catch and the probability of not having a cavity
given a catch. These two probabilities are calculated first using the rules of
conditional probability. Then they are placed in the tuple, which represents 
the true and false conditions.

P(Cavity&&Catch) = (0.108 + 0.072)/(0.108 + 0.016 + 0.072 + 0.144)
                 = 0.18/0.34
                 = 0.529
P(~Cavity&&Catch) =
                  = (0.016 + 0.144)/(0.108 + 0.016 + 0.072 + 0.144)
                  = 0.16/0.34
                  = 0.471
P(Cavity|Catch) = <P(Cavity&&Catch),P(~Cavity&&Catch)>
                = <0.529, 0.471>
True = 0.529
False = 0.471
'''

#Below is the computed solution for P(Cavity|Catch).
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Coin1', 'Coin2'])
heads, tails = True, False
P[heads, heads] = 0.25;
P[heads, tails] = 0.25;
P[tails, heads] = 0.25;
P[tails, tails] = 0.25;

# Compute P(Coin1|Coin2=heads)  (see the text, page 493).
PC = enumerate_joint_ask('Coin1', {'Coin2': heads}, P)
print(PC.show_approx())

'''
The results from this function do confirm what we believe to be true
about the probabilities of flipping coins. Each coin is completely 
independent from the others when it is being flipped, so every single
coin will have a 0.5 chance of being heads and a 0.5 chance of being tails.
'''
