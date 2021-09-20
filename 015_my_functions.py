import my_functions

workers = [('Jack', 'Smith', 2500, 11), ('Mary', 'Brown', 3000, 25), ('John', 'Brown', 7000, 34)]

for person in workers:
    my_functions.print_employer_message(person)