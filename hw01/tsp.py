"""
This implements a local-search version of a TSP problem for AIMA-Python.
Based on kvlinden's queens.py.

Solution: Simulated annealing does better than hill-climbing most of the time
(sometimes, they come up with the same answers). Simulated annealing works
better because it is willing to try an action that is "bad" for the sake of
finding a better path afterwards. However, hill-climbing will only choose the
best option in front of it at the moment and will never choose a "bad" city to
go to even if that one is better in the end.

@authors: Sarah Griffioen (slg27) & Lydia Holtrop (ljh27)
"""
from tools.aima.search import Problem, hill_climbing, simulated_annealing, exp_schedule
from random import randrange


class TSP(Problem):
    """An implementation of a TSP problem for local search.

    State representation: 
        [c1, c2, ..., cn] gives the order in which the cities are visited.
    Move/action representation:
        [num1, num2]: Swap the positions (within the list) of the cities at the given indexes.
    """

    def __init__(self, distances, initial):
        self.distances = distances
        self.initial = initial

    def actions(self, state):
        """This method generates two random integers to be used as indexes in a move.
        """
        num_cities = len(state) - 1 #minus 1 because start and end in same city
        actions = []
        for i in range(6):
            num1 = randrange(1, num_cities)
            num2 = randrange(1, num_cities)
            action = [num1, num2]
            actions.append(action)
        return actions

    def result(self, state, move):
        """Makes the given move (swaps the positions of the cities at the given
        indexes) on a copy of the given state."""
        new_state = state[:]
        new_state[move[0]], new_state[move[1]] = new_state[move[1]], new_state[move[0]]
        return new_state

    def value(self, state):
        """This method computes the total distance traveled in the given state by adding
        up the distance of each segment, then multiplying it by -1 to more semantically
        reflect that greater distance is less ideal.
        """
        num_visits = len(state)
        value = 0

        for i in range(1, num_visits):
            try:
                value += distances[(state[i-1], state[i])]
            except KeyError:
                value += distances[(state[i], state[i - 1])]

        value = -1 * value

        return value


if __name__ == '__main__':

    # Initialize a path and a dictionary of distances between cities
    initial_path = ['a', 'b', 'c', 'd', 'e', 'a']
    distances = {('a', 'b'): 1, ('a', 'c'): 3, ('a', 'd'): 2, ('a', 'e'): 4, ('b', 'c'): 3, ('b', 'd'): 2, ('b', 'e'): 1, ('c', 'd'): 8, ('c', 'e'): 3, ('d', 'e'): 5}

    # Initialize the TSP problem
    p = TSP(distances, initial_path)

    # Solve the problem using hill climbing.
    hill_solution = hill_climbing(p)
    print('Hill-climbing:')
    print('\tSolution: ' + str(hill_solution))
    print('\tDistance:    ' + str(-p.value(hill_solution)))

    # Solve the problem using simulated annealing.
    annealing_solution = simulated_annealing(
        p,
        exp_schedule(k=20, lam=0.005, limit=10000)
    )
    print('Simulated annealing:')
    print('\tSolution: ' + str(annealing_solution))
    print('\tDistance:    ' + str(-p.value(annealing_solution)))

    if (p.value(hill_solution) > p.value(annealing_solution)):
        print("\nHill-climbing did better than simulated annealing.")
    elif (p.value(annealing_solution) > p.value(hill_solution)):
        print("\nSimulated annealing did better than hill-climbing.")
    else:
        print("\nThe two algorithms came up with the same solution.")
