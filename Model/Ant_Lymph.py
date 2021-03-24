import random


class Antigen:

    def __init__(self, epitope, pop, n):
        self.epitope = epitope  # Stores the aa sequence of the epitope
        self.pop = dict()  # Dictionary that stores each antigen in the population
        self.n = n  # The number of individuals in the population


ant1 = Antigen('ACDEFGHIK', 1, 1)  # Instance of object "Antigen()"


class Lymphocyte():

    def __init__(self, paratope, pop, n):
        self.paratope = ''
        self.pop = dict()
        self.n = n

    def gen_para(self, len_epitope):
        """
        Randomly generates a paratope of the same length as the antigen epitope.

        Args: length

        Returns: paratope as a string

        """
        aa_list = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
                   'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']  # List of all possible amino acids
        for i in range(len_epitope):
            self.paratope += (random.choice(aa_list))

        return self.paratope


lymph1 = Lymphocyte('', 1, 1)  # Instance of object "Lymphocyte()"

print(lymph1.gen_para(len(ant1.epitope)))
