from Model.Ant_Lymph import Lymphocyte, lymph_test


class Selection:

    def __init__(self):
        self.result_pop = dict()
        self.selection_dict = dict()

    def clonal_selection(self, exchange_iter):
        pop_n == lymph_test.pop

        for i in range(0, pop_n):
            self.selection_dict[i] = lymph_test.paratope  # Creates a dictionary with each population as keys and the
            # paratopes as values

        # for pop in self.selection_dict:
