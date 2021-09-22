import pandas as pd
import numpy as np
import os
import sys
import Arg_Parser
from Arg_Parser import *
from Ant_Lymph import lymph, antigen

args = bcell_selection_parser().parse_args(sys.argv[1:])

matrix = np.loadtxt(os.path.join(Arg_Parser.root_dir, "Resources/PAM_250.txt"))
matrix = np.array(matrix)

col_names = ("A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V")
row_names = col_names
pam = pd.DataFrame(matrix, columns=col_names, index=row_names)  # Creates a square matrix of substitution likelihoods.
col = pam["A"]


class Selection:

    def __init__(self):
        self.result_pop = dict()
        self.selection_dict = dict()
        self.likelihood = dict()

    def clonal_selection(self, exchange_iter):
        """
        Performs clonal selection on each B-cell population generated in Ant_Lymph.py. Each random paratope generated
        represents a population with a property n as the number of individuals in the population. This will become
        relevant in the immune response. Substitution likelihoods are calculated for each character of the paratope
        taken from the PAM 250 matrix. This will run for exchange_iter number of iterations.

        :param exchange_iter:
        :return: Population(s) with max affinity to the antigen epitope.
        """
        pop_n = lymph.pop_num
        ant = antigen.epitope

        aa_list = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
                   'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

        for i in range(0, pop_n):
            self.selection_dict[i] = lymph.paratope  # Creates a dictionary with each population as keys and the
            # paratopes as values

        for j in aa_list:
            self.likelihood[j] = dict()

        for key, value in self.selection_dict.items():
            para = value
            match_number = len(list(filter(lambda xy: xy[0] == xy[1], zip(ant, para))))  # Identifies the
            # index-specific match integer

            fitness = match_number / len(ant)
            self.selection_dict[key] = [lymph.paratope, self.likelihood, lymph.n,
                                        fitness]  # Each population will undergo
            # clonal selection as opposed to each individual because the likelihood of substitution would be the
            # same for each individual in the population.

        count = 0  # Track the amount of iterations until max-affinity
        for k in range(0, len(self.selection_dict)):  # Iterates through each population's paratope in selection_dict
            for pop in self.selection_dict.values():
                other_likelihood = dict()
                for aa in pop[0]:  # Iterates through each character of the paratope string
                    for row in row_names:  # Iterates through the PAM matrix to calculate likelihood of each amino
                        # acid in the paratope to substitute for another.
                        col = pam[aa]
                        # for l in range(0, 19):
                        value = col[row]
                        other_likelihood[row] = value
                    self.likelihood[aa] = other_likelihood
            print(self.likelihood)


example = Selection()
# col = pam["A"]
# print(col[row_names[0]])
print(example.clonal_selection(1))
