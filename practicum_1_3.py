a = float(input('Input triangle side "a": '))
b = float(input('Input triangle side "b": '))
c = float(input('Input triangle side "c": '))
c_2 = c ** 2
ab_2 = (a ** 2) + (b ** 2)
chk = c_2 / ab_2
print()
print('--------------------------------------------')
if chk == 1:
    print('Trianle is prjamougolnyj')
else:
    print('Trianle is NOT prjamo1ugolnyj')