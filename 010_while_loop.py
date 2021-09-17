# while True:
#    print("I cann't stop")

#print("Hello world")

#condition = 0
#while condition < 100:
#    print(condition)
#    condition += 1

condition = True
while condition:
    user_input = input('Please enter ID: ')
    if len(user_input) != 11:
        print("Wrong ID entered")
    else:
        condition2 = True
        while condition2:
            print(user_input)
            user_input2 = input("Please enter name or 'x' for exit: ")
            if user_input2 == '':
                print("Error")
            elif user_input2 == 'x':
                condition = False
                condition2 = False
            else:
                print(user_input2)
                condition2 = False
            condition = False