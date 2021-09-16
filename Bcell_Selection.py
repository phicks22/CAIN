import pandas as pd
import numpy as np
import os
import sys
import Arg_Parser
from Arg_Parser import *
from Ant_Lymph import lymph_test, ant_test

matrix = np.loadtxt(os.path.join(Arg_Parser.root_dir, "Resources/PAM_250.txt"))
matrix = np.array(matrix)

col_names = ("A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V")
row_names = col_names
pam = pd.DataFrame(matrix, columns=col_names, index=row_names)
print(pam)


class Selection:

    def __init__(self):
        self.result_pop = dict()
        self.selection_dict = dict()
        self.likelihood = dict()

    def clonal_selection(self, exchange_iter):
        pop_n = lymph_test.pop
        ant = ant_test.epitope

        aa_list = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
                   'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

        for i in range(0, pop_n):
            self.selection_dict[i] = lymph_test.paratope  # Creates a dictionary with each population as keys and the
            # paratopes as values

        for j in aa_list:
            self.likelihood[j] = 0

            for key in self.selection_dict.keys():
                # fitness =
                self.selection_dict[key] = [self.likelihood, lymph_test.n, fitness]  # Each population will undergo clonal
                # selection as opposed to each individual because the likelihood of substitution would be the same for
                # each individual in the population.

        count = 0  # Track the amount of iterations until max-affinity
        for pop in self.selection_dict.keys():  # Iterates through each population's paratope in selection_dict
            for i in self.selection_dict[pop]:  # Iterates through each character of the paratope string
                for col in pam[:, col]:  # Iterates through the PAM matrix to calculate likelihood of each amino acid
                    # in the paratope to substitute for another.
                    self.likelihood[col] = pam[i, col]
