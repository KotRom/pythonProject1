# 'r' read
# 'a' append tol'ko dlja dobavlenija dannyh v konec faila
# 'w' write
# 'x' create sozdajot fail, esli ego ne suwestvuet
# 'r+' read and write

#with open('loren_text.txt', 'r', encoding='UTF8') as file:
#    data = file.read()
#print(file.closed)

#with open('write_text.txt', 'w', encoding='UTF8') as file: #write - udaljaet soderzhimoe faila pri otkrytii


#with open('write_text.txt', 'r+', encoding='UTF8') as file:
#    data = file.read()
#    print(data)
#    file.write('Hello WWWord\n')
#    file.write('Hello people\n')
#user_text = input('please enter some text: ')

user_list = ['john', 'mike', 'anna']
with open('write_text.txt', 'w', encoding='UTF8') as file:
    #file.write(user_text)
    for person in user_list:
        file.write(f'Hello {person}!')
        file.seek(0)