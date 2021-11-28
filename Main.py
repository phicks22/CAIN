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

    def immune_response(self, population_dict, antigen_pop, response_time, a_div):
        """
        Simulates immune response games between the antigen and lymphocyte populations.

        :arg population_dict --> Post-selection dictionary from B-cell selection algorithm
        :arg antigen_pop --> Dictionary for the single antigen population
        :arg response_time --> Number of iterations allowed for the immune response games

        :return: Population dictionary
        """
        response_time_individual = 0
        response_time_population = 0

        # Run an agent-based game between each lymphocyte population and the antigen population
        for i in range(0, response_time):
            for pop in population_dict.values():
                for n in range(0, pop[1]):    # Runs a game where a random number between 0 and 1 is picked.
                    draw = random.random()
                    if draw > pop[2]:  # Removes 1 individual from the lymphocyte population (antigen wins)
                        pop[1] -= 1
                        antigen_pop.n += a_div
                    elif draw <= pop[2]:    # Removes 1 individual from the antigen population (lymphocyte wins)
                        antigen_pop.n -= 1
                        pop[1] += 2
                    else:
                        print("Error: Draw exceeds 0-1 range.")
                    response_time_individual += 1
                  # Deletes "dead" lymphocyte populations
            for key in list(population_dict.keys()):
                n = population_dict.get(key)[1]
                if n <= 0:
                    del population_dict[key]
                response_time_population += 1
        return population_dict


if __name__ == '__main__':

    pop_size = int(args.pop_size)
    pop_num = int(args.pop_num)
    epitope = args.epitope
    ant_div = int(args.division_rate)
    exchange_iter = int(args.exchange_iter)
    antigen = Antigen(epitope=epitope, pop_num=1, n=1, division_rate=ant_div)
    lymph = Lymphocyte(paratope='', pop_num=pop_num, n=pop_size)

    for k in range(0, lymph.pop_num):
        paratope = lymph.gen_para(len(antigen.epitope))
        lymph.pops[k] = [paratope]

    selection = Selection()
    print("_________________________________________________________________")
    populations = selection.clonal_selection(exchange_iter=exchange_iter, antigen=antigen,
                                             lymphocyte=lymph)  # Selection dictionary
    print("_________________________________________________________________")

    response = Main()
    final_pops = response.immune_response(populations, antigen, response_time=5, a_div=ant_div)
    print(final_pops)
    print("Immune Response Completed")
    print("_________________________________________________________________")

