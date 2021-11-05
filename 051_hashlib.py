import hashlib
# hash - odnostoronne shifrivanie password
password = "HelloWorld"
hashed_pass = hashlib.md5(password.encode()).hexdigest()

user_input = input('Please enter password')

hashed_user_input = hashlib.md5(user_input.encode()).hexdigest()

if hashed_user_input == hashed_pass:
    print(hashed_user_input)
    print(hashed_pass)
    print('ok')
else:
    print(hashed_user_input)
    print(hashed_pass)
    print('error')

