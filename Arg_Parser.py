import argparse

root_dir = '/Users/parkerhicks/Documents/GitHub/Python/Thesis_Notebook/'


def ant_lymph_parser():
    parser = argparse.ArgumentParser(description='Set population paramters for antigens and lymphocytes.',
                                     add_help=True)
    req_args = parser.add_argument_group('Required Arguments')
    req_args.add_argument('-e', dest='epitope',
                          help='REQUIRED: Set the desired linear epitope for the antigen [Example: ACDEFGHIKLM].',
                          required=True)
    req_args.add_argument('-n', dest='pop_size',
                          help='REQUIRED: Set the desired B-cell population size [Example: 100].',
                          required=True)
    req_args.add_argument('-d', dest='division_rate',
                          help='REQUIRED: Set the division rate of the antigen [Example: 2].',
                          required=True)
    req_args.add_argument('-p', dest='pop_num',
                          help='REQUIRED: Set the number of lymphocyte populations.',
                          required=True)
    req_args.add_argument('-ex', dest='exchange_iter',
                          help='REQUIRED: Set the desired epitope for the antigen [Example: ACDEFGHIKLM].',
                          required=True)
    req_args.add_argument('-r', dest='response_time',
                          help='REQUIRED: Set the number of iterations of the immune response [Example: 10].',
                          required=True)
    return parser
