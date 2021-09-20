#def square_root3():
#    print(1234567890)
#square_root3()
#print()


#def square_root2():
#    return 1234567890
#print(square_root2())
#print()


#def square_root4(number):
#    return number ** 0.5


#x = square_root4(36)
#print(x)
#print()
#print(square_root4(25))

def square_root(number):
    return number ** 0.5


def return_x():
    x = 25
    return x


print(return_x())
print()


def print_squares(number):
    print(number ** 2)


print(square_root(return_x()))
print()


def power_function(power, number):
    return number ** power


print(power_function(2, 10))
print()


def print_employer_message(employee):
    print(f'Hello {employee[0]} {employee[1]}.')
    print(f'Your salary is {employee[2]:.2f} EUR.')
    print(f'Youe are {employee[3]} years old.')
    print()


workers = [('Jack', 'Smith', 2500, 11), ('Mary', 'Brown', 3000, 25), ('John', 'Brown', 7000, 34)]
for person in workers:
    print_employer_message(person)


