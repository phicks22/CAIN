import random
import os
import sys
from Ant_Lymph import Antigen, Lymphocyte
from Bcell_Selection import Selection
from Arg_Parser import *

args = ant_lymph_parser().parse_args(sys.argv[1:])


# Calling instances of both Ant_Lymph classes
# ant1 = Antigen('ACDEFGHIKLM', 1, 1)
# lymph1 = Lymphocyte('', 1, 1)
# lymph2 = lymph1.gen_para(len(ant1.epitope))


class Main:

    def __init__(self, ):
        self.iteration_counts = dict()

    def binding(self, a, l):
        """
        Simulates the initial binding of the antigen and lymphocyte.

        Args: a, l

        Returns: bind_time, bound = TRUE


        """
        bind_time = 0
        match_number = 0

        match_number = len(list(filter(lambda xy: xy[0] == xy[1], zip(a, l))))  # Identifies the index-specific match
        # integer

        pr_bind = match_number / len(a)  # calculates the probability of binding

        while random.random() <= (1 - pr_bind):  # Simulates the binding process of the antigen and lymphocyte
            if match_number == 0:  # If there's no probability of binding
                print("Pr(binding) = 0. Try again nerd!")
                break
            bind_time += 1
        self.iteration_counts['init_bind'] = bind_time

        return self.iteration_counts  # Holds the time it takes for antigen/lymphocyte binding

    def immune_response(self, population_dict, antigen_pop, response_time):
        """
        Simulates immune response games between the antigen and lymphocyte populations.


        :return:
        """
        response_time_individual = 0
        response_time_population = 0

        # Run an agent-based game between each lymphocyte population and the antigen population
        for i in range(0, response_time):
            for pop in population_dict.keys():
                if pop[1] <= 0:  # Deletes "dead" lymphocyte populations
                    del population_dict[pop]
                for n in pop[1]:    # Runs a game where a random number between 0 and 1 is picked.
                    draw = random.random()
                    if draw > pop[2]:  # Removes 1 individual from the lymphocyte population (antigen wins)
                        n -= 1
                    elif draw <= pop[2]:    # Removes 1 individual from the antigen population (lymphocyte wins)
                        antigen_pop[0][1] -= 1
                    else:
                        print("Error: Draw exceeds 0-1 range.")
                    response_time_individual += 1
                response_time_population += 1


if __name__ == '__main__':

    antigen = Antigen(epitope=args.epitope, pop_num=1, n=1, division_rate=1)
    lymph = Lymphocyte(paratope='', pop_num=4, n=1)

    for k in range(0, lymph.pop_num):
        paratope = lymph.gen_para(len(antigen.epitope))
        lymph.pops[k] = [paratope]

    selection = Selection()
    populations = selection.clonal_selection(exchange_iter=10, antigen=antigen,
                                             lymphocyte=lymph)  # Selection dictionary
