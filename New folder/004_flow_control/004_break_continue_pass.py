while True:
    user_input = input('Please choose:\n1:Print\n0:Exit')
    if user_input == '1':
        print('All is good')
        continue
    elif user_input == '0':
        break
    else:
        pass
    print('test')
print('You have exited while loop.')

# for letter in 'Python':     # First Example
#    if letter == 'h':
#       continue
#    print('Current Letter :', letter)
#
# var = 10                    # Second Example
# while var > 0:
#    var = var -1
#    if var == 5:
#       continue
#    print('Current variable value :', var)
# print("Good bye!")
#
