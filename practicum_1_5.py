tuple_a = (1, 2, 3, 5, 8)
print(tuple_a)
tuple_b = (8, 2, 5)
print(tuple_b)


tuple_a.insert(2, tuple_b)
tuple_a.extend(tuple_b)
print(tuple_a)
tuple_3 = tuple_a[0:2] + tuple_b + tuple_a[2:]
print(tuple_3)

#tuple_a = list(tuple_a)
#for x in tuple_b[::-1]:
#    tuple_a.insert(2, x)
#tuple_a = tuple(tuple_a)
#print(tuple_a)