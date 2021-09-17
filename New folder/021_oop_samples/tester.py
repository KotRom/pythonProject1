import employee_lib as el

emp1 = el.Employee('Sam', 'Summers', 2000)
dev2 = el.Employee('Mary', 'Gold', 2500)

emp1.first = 'Jim'
print(emp1.first)
print(emp1.email)

print(emp1.__dict__)
emp1.fullname = 'Jack Green'
print(emp1.__dict__)

del emp1.fullname
print(emp1.__dict__)