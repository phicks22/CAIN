import random
from Model.Ant_Lymph import ant_test, lymph_test

# Calling instances of both Ant_Lymph classes
#ant1 = Antigen('ACDEFGHIKLM', 1, 1)
#lymph1 = Lymphocyte('', 1, 1)
#lymph2 = lymph1.gen_para(len(ant1.epitope))


class Main:

    def __init__(self):
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
                break
            bind_time += 1
        self.iteration_counts['init_bind'] = bind_time

        return self.iteration_counts  # Holds the time it takes for antigen/lymphocyte binding


    def immune_response(self):
        """
        Simulates immune response games between the antigen and lymphocyte populations.


        :return:
        """
        response_time = 0

        #for pop in lymph_test.result_pop:



example = Main()

print(example.binding(ant_test.epitope, lymph_test.paratope))
