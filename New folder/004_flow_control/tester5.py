def user_menu():
    user_choice = input('Please choose:\n1.Get data by ID code\n2.Check if ID is valid\n3.Exit\n-->')
    if user_choice == '1':
        condition = True
        while condition:
            try:
                user_id = input('Please enter ID: ')
                int(user_id)
                if len(user_id) != 11:
                    raise UserWarning
            except UserWarning:
                if len(user_id) < 11:
                    print('Code is too short')
                elif len(user_id) > 11:
                    print('Code is too long')
            except:
                print('Code you entered is not numeric')
            else:
                condition = False
                get_data_by_id(user_id)


    elif user_choice == '2':
        pass
    elif user_choice == '3':
        quit()
    else:
        print('Choice out of range')
        user_menu()

def get_data_by_id(idcode):
    gender_num = idcode[0]
    by_num = idcode[1:3]
    bm_num = idcode[3:5]
    bd_num = idcode[5:7]
    region_num = idcode[7:10]
    chk_num = idcode[10]

    if gender_num == '1':
        cent_id = '18'
        gend_id = 'Male'
    elif gender_num == '2':
        cent_id = '18'
        gend_id = 'Female'
    elif gender_num == '3':
        cent_id = '19'
        gend_id = 'Male'
    elif gender_num == '4':
        cent_id = '19'
        gend_id = 'Female'
    elif gender_num == '5':
        cent_id = '20'
        gend_id = 'Male'
    elif gender_num == '6':
        cent_id = '20'
        gend_id = 'Female'

    print(idcode)
    print('You are ' + gend_id)
    print('You were born in ' + bd_num + '.' + bm_num + '.' + cent_id + by_num)

    user_menu()

user_menu()