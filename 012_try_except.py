try:
    user_input = input('Please enter your ID: ')
    int(user_input)
except:
    print('error')
else:
    print(user_input)

print('Hello world')