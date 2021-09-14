import os
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
        self.pop = dict()
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
        for i in self.pop_num:
            for j in range(len_epitope):
                self.paratope += (random.choice(aa_list))
                self.pop[i] = self.paratope

        return self.pop


ant_test = Antigen(epitope=args.epitope, pop_num=args.pop_num, n=args.pop_size, division_rate=args.division_rate)
lymph_test = Lymphocyte(paratope='', pop_num=1, n=1)

lymph_test_gen_para = lymph_test.gen_para(len(ant_test.epitope))


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