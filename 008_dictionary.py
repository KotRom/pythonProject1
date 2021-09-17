x = 5
student = {'name': 'john', 'age': 32, 'courses': ['Math', 'Art', 'Programming'], 1: 'int key', 8.2: 'float key', x: 'variable', 'var_key': x, 8: 'int key', 'dict_key': {'one': 1, 'two': 2}}

#student.update('name': 'Mary', 'age': 25, 'phone': '333-444-555')
print(student)
print()
poped_item = student.pop('courses')
print(poped_item)
print()
print(student.keys())
print()
print(type(student.keys()))
print()
print(student.values())
print(student.items())

for key in student.keys():
    print(key)
for x in student.values():
    print(x)