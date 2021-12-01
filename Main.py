import random
import os
import sys
from Ant_Lymph import Antigen, Lymphocyte
from Bcell_Selection import Selection
from sklearn.preprocessing import OneHotEncoder
from Arg_Parser import *

args = ant_lymph_parser().parse_args(sys.argv[1:])


class Main:

    def __init__(self, ):
        self.iteration_counts = dict()

    def binding(self, a, l):
        """
        Simulates the initial binding of the antigen and lymphocyte.

        :arg a --> Antigen epitope
        :arg l --> B-cell paratope

        :return bind_time, bound = TRUE

        """
        bind_time = 0
        match_number = 0

        match_number = len(list(filter(lambda xy: xy[0] == xy[1], zip(a, l))))  # Identifies the index-specific match
        # integer

        pr_bind = match_number / len(a)  # calculates the probability of binding

        # Simulate the binding process of the antigen and lymphocyte
        while random.random() <= (1 - pr_bind):
            if match_number == 0:
                print("Pr(binding) = 0. Try again loser!")
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
        :arg a_div --> Antigen division rate

        :return Population dictionary

        """
        response_time_individual = 0
        response_time_population = 0

        # Run an agent-based game between each lymphocyte population and the antigen population
        for i in range(0, response_time):
            for pop in population_dict.values():

                # Runs a game where a random number between 0 and 1 is picked.
                for n in range(0, pop[1]):
                    draw = random.random()

                    # Removes 1 individual from the lymphocyte population (antigen wins)
                    if draw > pop[2]:
                        pop[1] -= 1
                        antigen_pop.n += a_div

                    # Removes 1 individual from the antigen population (lymphocyte wins)
                    elif draw <= pop[2]:
                        antigen_pop.n -= 1
                        pop[1] += 2
                    else:
                        print("Error: Draw exceeds 0-1 range.")
                    response_time_individual += 1

            # Delete "dead" lymphocyte populations
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
    res_time = int(args.response_time)
    antigen = Antigen(epitope=epitope, pop_num=1, n=1, division_rate=ant_div)
    lymph = Lymphocyte(paratope='', pop_num=pop_num, n=pop_size)

    for k in range(0, lymph.pop_num):
        paratope = lymph.gen_para(len(antigen.epitope))
        lymph.pops[k] = [paratope]

    selection = Selection()
    print("_________________________________________________________________")

    # Run B-cell clonal selection
    populations = selection.clonal_selection(exchange_iter=exchange_iter, antigen=antigen,
                                             lymphocyte=lymph)
    print("_________________________________________________________________")

    # Run the immune response for all populations
    response = Main()
    final_pops = response.immune_response(populations, antigen, response_time=res_time, a_div=ant_div)
    print(final_pops)
    print("Immune Response Completed")
    print("_________________________________________________________________")

################### For Large Dataset Collection ###################
# Save parameters and output as a list to be One Hot Encoded
dataset = list()
selection = Selection()
epitope = args.epitope
ant_div = int(args.division_rate)

# Initialize antigen population
antigen = Antigen(epitope=epitope, pop_num=1, n=1, division_rate=ant_div)

# Iterate through all desired parameter values
# Population Number
for i in range(100, 1000):
    # Population size
    for j in range(100, 1000):
        # Exchange iterations
        for k in range(10, 1000):
            # Immune response time
            for h in range(10, 1000):
                # Initialize the lymphocyte populations
                lymph = Lymphocyte(paratope='', pop_num=i, n=j)

                # B-cell clonal selection
                populations = selection.clonal_selection(exchange_iter=k, antigen=antigen,
                                                         lymphocyte=lymph)

                #  Immune response
                response = Main()
                final_pops = response.immune_response(populations, antigen, response_time=h, a_div=ant_div)

                # Save parameters and output to dataset list
                for value in final_pops.values():
                    dataset.append(value)

# One-hot-encode the parameters to save as a matrix
enc = OneHotEncoder(handle_unknown='ignore')

