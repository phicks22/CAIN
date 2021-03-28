import random
from Model.Ant_Lymph import Antigen
from Model.Ant_Lymph import Lymphocyte

# Calling instances of both Ant_Lymph classes
ant1 = Antigen('ACDEFGHIKLM', 1, 1)
lymph1 = Lymphocyte('', 1, 1)
lymph2 = lymph1.gen_para(len(ant1.epitope))


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
        count = 0

        print(ant1.epitope)
        print(lymph1.paratope)

        #for i in a, l:
         #   if a[i] == l[i]:
          #      count += 1
           #     if count == 0:
            #        return print("No probability of binding.")

        #for l1, l2 in zip(a, l):
         ##      count += 1  # amount of matching amino acids in zip(a, l)
           ##        return print("No probability of binding")

        count = len(list(filter(lambda xy: xy[0] == xy[1], zip(a, l))))


        pr_bind = count / len(a)

        while random.random() <= (1 - pr_bind):
            if count == 0:
                break
            bind_time += 1
        self.iteration_counts['init_bind'] = bind_time

        return self.iteration_counts  # Holds the time it takes for antigen/lymphocyte binding


example = Main()

print(example.binding(ant1.epitope, lymph1.paratope))
