id_code = '37912150240'
chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
result = 0
counter = 0
for num in chk1:
    result = result + int(id_code[counter]) * num
    counter += 1
if result % 11 == int(id_code[-1]):
    print(id_code, "Code is valid")
else:
    result = 0
    counter = 0
    for num in chk2:
        result = result + int(id_code[counter]) * num
        counter += 1
    if result % 11 == int(id_code[10]):
        print("ID is valid")
    else:
        print("ID NOT VALID")
