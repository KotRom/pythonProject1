numbers = [4, 5, 2, 8, 9]

for num in numbers:
    if num > 5:
        print('number is >5')
        print(num ** 2)
    elif num ==5:
        print(num ** 10)
print()
some_text = "Hello world"
for letter in some_text:
    print(letter.upper())
print()


counter = 0
for num1 in range(0, 10):
    for num2 in range(0, 10):
        for num3 in range(0, 10):
            for num4 in range(0, 10):
                print(num1, num2, num3, num4)
                counter +=1
print(counter)

for number in range(1, 100):
    if number % 2 == 0: # OSTATOK PRI DELWNII NA 2
        print(number, 'odd')
    else:
        print(number, 'even')
