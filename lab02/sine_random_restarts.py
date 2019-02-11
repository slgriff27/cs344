"""
    This module implements local search on a simple sine function variant.
    The function is a linear function  with a single, discontinuous max value
    (see the abs function variant in graphs.py).
    
    @author: kvlinden
    @version 6feb2013
    """
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math
import time


class SineVariant(Problem):
    """
        State: x value for the sine function variant f(x)
        Move: a new x value delta steps from the current x (in both directions)
        """
    
    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta
    
    def actions(self, state):
        return [state + self.delta, state - self.delta]
    
    def result(self, stateIgnored, x):
        return x
    
    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':
    hill_record_x = 0
    hill_record_val = 0
    sim_record_x = 0
    sim_record_val = 0
    
    # choose a random number of times to restart
    attempts = randrange(1, 47)
    print('Number of random restarts: ' + str(attempts))
    for i in range(attempts):
        
        # Formulate a problem with a 2D hill function and a single maximum value.
        maximum = 30
        initial = randrange(0, maximum)
        p = SineVariant(initial, maximum, delta=1.0)
        
        # Solve the problem using hill-climbing.
        start_time = time.time()
        hill_solution = hill_climbing(p)
        end = time.time()
        if hill_record_val < p.value(hill_solution):
            hill_record_val = p.value(hill_solution)
            hill_record_x = hill_solution
    
        # Solve the problem using simulated annealing.
        start_time = time.time()
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
            )
        end = time.time()
        if sim_record_val < p.value(annealing_solution):
            sim_record_val = p.value(annealing_solution)
            sim_record_x = annealing_solution

    print('Hill-climbing solution x: ' + str(hill_record_x)
      + '\tvalue: ' + str(hill_record_val)
      )
    print('My program took', end - start_time, 'to run')
    
    print('Simulated annealing solution x: ' + str(sim_record_x)
          + '\tvalue: ' + str(sim_record_val)
          )
    print('My program took', end - start_time, 'to run')
