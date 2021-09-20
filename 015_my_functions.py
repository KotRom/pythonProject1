# import my_functions
#workers = [('Jack', 'Smith', 2500, 11), ('Mary', 'Brown', 3000, 25), ('John', 'Brown', 7000, 34)]
#for person in workers:
#    my_functions.print_employer_message(person)

from my_functions import print_employer_message, return_x # * - import all functions from file

import my_functions as mf

workers = [('Jack', 'Smith', 2500, 11), ('Mary', 'Brown', 3000, 25), ('John', 'Brown', 7000, 34)]

for person in workers:
    print_employer_message(person)
#    mf.print_employer_message(person)