while True:
    try:
        user_input = input('Please enter your ID: ')
        int(user_input)
        if len(user_input) != 11:
            raise UserWarning
    except ValueError:
        print('Code you entered is not numberic')
        continue
    except UserWarning:
        if len(user_input) > 11:
            print('code is too long')
        elif len(user_input) < 11:
            print('code is too short')
            continue
    else:
        print(user_input)
        break
    finally:
        print('good bye')