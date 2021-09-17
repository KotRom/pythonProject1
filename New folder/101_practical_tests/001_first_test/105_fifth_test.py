tupple_1 = (1, 2, 3, 5, 8)
tupple_2 = (8, 2, 5)

tupple_1 = list(tupple_1)
for x in tupple_2[::-1]:
    tupple_1.insert(2, x)

tupple_1 = tuple(tupple_1)
print(tupple_1)