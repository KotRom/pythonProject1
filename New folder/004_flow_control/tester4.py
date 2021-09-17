
try:
    user_id = int(input('Please enter your id: '))
    if len(user_id) != 11:
        raise UserWarning
except TypeError:
    print('ERROR')
except UserWarning:
    print('Not 11 digits long')
except:
    print('The code you entered is not numeric')
else:
    print(user_id)
finally:
    print('Program stopped working')