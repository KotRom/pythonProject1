import hashlib
# hash - odnostoronne shifrivanie password (podborka hash)
password = "HelloWorld"
hashed_pass = hashlib.md5(password.encode()).hexdigest()[0:6]

x = 0
while True:
    pw = password + f'{x}'
    hashed_pw = hashlib.md5(pw.encode()).hexdigest()[0:6]
    if hashed_pass == hashed_pw:
        print(pw)
        print(hashed_pw)
        print(hashed_pass)
    x += 1
