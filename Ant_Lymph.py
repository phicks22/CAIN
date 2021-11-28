import random
import sys
import unittest
from Arg_Parser import *
args = ant_lymph_parser().parse_args(sys.argv[1:])


class Antigen:

    def __init__(self, epitope, n, division_rate, pop_num):
        self.epitope = epitope  # Stores the aa sequence of the epitope
        self.pop_num = pop_num
        self.pop = dict()  # Dictionary that stores each antigen in the population
        self.n = n  # The number of individuals in the population
        self.divide_a = division_rate  # The division rate of the antigen


class Lymphocyte:

    def __init__(self, paratope, pop_num, n):
        self.paratope = paratope
        self.pop_num = pop_num
        self.pops = dict()
        self.n = n
        self.divide_l = 1

    # TODO Identify cell division rates

    def gen_para(self, len_epitope):
        """
        Randomly generates population of randomly generated paratopes of the same length as the antigen epitope.

        Args: length

        Returns: population dictionary of paratopes

        """
        aa_list = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
                   'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']  # List of all possible amino acids
        paratope = ''
        for i in range(len_epitope):
            paratope += (random.choice(aa_list))

        return paratope


class TestCases(unittest.TestCase):

    def len_epitope_equals_len_paratope(self, paratope, epitope):
        """
        Tests if the length of the epitope is equal to the length of the paratope

        Args: paratope, epitope

        Returns: string
        """
        len_a = len(paratope)
        len_l = len(epitope)
        self.assertEqual(len_a, len_l, msg="len(a) != len(l)")

        if len_a == len_l:
            print("All good")
