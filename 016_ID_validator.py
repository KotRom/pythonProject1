def enter_id():
    while True:
        try:
            user_input = input('Please enter your ID: ')
            int(user_input)
            if len(user_input) != 11:
                raise UserWarning
        except ValueError:
            print('Code you entered is not numeric')
            continue
        except UserWarning:
            if len(user_input) > 11:
                print('code is too long')
            elif len(user_input) < 11:
                print('code is too short')
                continue
        else:
            print(f'Your ID {user_input} lengnt is OK!\n')
            return main(user_input)


def validate_id(id_code):
    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    result = 0
    counter = 0
    for num in chk1:
        result = result + int(id_code[counter]) * num
        counter += 1
    if result % 11 == int(id_code[-1]):
        print(id_code, "ID is valid\n")
    else:
        result = 0
        counter = 0
        for num in chk2:
            result = result + int(id_code[counter]) * num
            counter += 1
        if result % 11 == int(id_code[10]):
            print(id_code, "ID is valid\n")
        else:
            print(id_code, "ID NOT VALID\n")
    main(id_code)


def main(id_code):
    while True:
        user_choice = input('Please enter:\n'
                            '1. Get ID data\n'
                            '2. Validate\n'
                            '3. Input ID\n'
                            '4. Exit\n'
                            '-->')
        if user_choice == '1':
            pass
        elif user_choice == '2':
            validate_id(id_code)
        elif user_choice == '3':
            enter_id()
        elif user_choice == '4':
            break
        else:
            print('Choice is not in range\n')


main('sdxdsxdsxds')