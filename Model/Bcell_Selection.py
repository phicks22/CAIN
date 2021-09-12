import pandas as pd
import numpy as np
import os
import Arg_Parser
from Ant_Lymph import lymph_test

matrix = np.loadtxt(os.path.join(Arg_Parser.root_dir, "Resources/PAM_250.txt"))
matrix = np.array(matrix)


col_names = ("A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y",   "V")
row_names = col_names
pam = pd.DataFrame(matrix, columns=col_names, index=row_names)


class Selection:

    def __init__(self):
        self.result_pop = dict()
        self.selection_dict = dict()
        self.likelihood = dict()

    def clonal_selection(self, exchange_iter):
        pop_n = lymph_test.pop

        for i in range(0, pop_n):
            self.selection_dict[i] = lymph_test.paratope  # Creates a dictionary with each population as keys and the
            # paratopes as values

        aa_list = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
                   'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

        for i in aa_list:
            self.likelihood[i] = 0

        count = 0   # Track the amount of iterations until max-affinity
        # for pop in self.selection_dict.keys():



