import random
from Model.Ant_Lymph import ant1, lymph1


class Main:

    def __init__(self):
        self = self
        self.iteration_counts = dict()

    def binding(self, a, l):
        """
        Simulates the initial binding of the antigen and lymphocyte.

        Args: a, l

        Returns: bind_time, bound = TRUE


        """
        bind_time = 0
        count = 0

        for l1, l2 in zip(a, l):
            if l1 == l2:
                count += 1

        pr_bind = count / len(a)

        #         pr_bind = SequenceMatcher(None, a, l).ratio() #Maybe use for conformational epitopes?

        while random.random() <= (1 - pr_bind):
            bind_time += 1
        self.iteration_counts['init_bind'] = bind_time

        return self.iteration_counts  # Holds the time it takes for antigen/lymphocyte binding


example = Main()

print(example.binding(ant1.epitope, lymph1.paratope))
