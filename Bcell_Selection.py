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
        ant = antigen.epitope

        aa_list = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
                   'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

        self.selection_dict = lymph.pops  # Creates a dictionary with each population as keys and the
        # paratopes as values

        for item in aa_list:
            self.likelihood[item] = 0

        for aa in self.likelihood.keys():
            other_likelihood = dict()
            for row in row_names:
                col = pam[aa]  # Calls the df column for the amino acid
                value = col[row]  # Calls the value for the column and row
                other_likelihood[row] = value
            self.likelihood[aa] = other_likelihood

        for key, value in self.selection_dict.items():
            para = value
            match_number = len(list(filter(lambda xy: xy[0] == xy[1], zip(ant, para))))  # Identifies the
            # index-specific match integer

            fitness = match_number / len(ant)
            value.append(lymph.n)
            value.append(fitness)
            # Each population will undergo clonal selection as opposed to each individual because the likelihood of
            # substitution would be the same for each individual in the population.

        ############# Selection Process #############
        for i in range(0, exchange_iter):
            for item in self.selection_dict.values():
                product = ''
                for a in item[0]:
                    v = list(self.likelihood[a].values())
                    k = list(self.likelihood[a].keys())
                    v.remove(v[k.index(a)])
                    k.remove(a)
                    max1 = max(v)
                    if max1 > 0:
                        product += k[v.index(max1)]
                    else:
                        product += a

                print(item[0], "----->", product)
                item[0] = product

        return self.selection_dict


example = Selection()
print(example.clonal_selection(1))
