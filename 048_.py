class Employee:
    raise_amount = 1.05
    number_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.number_of_employees += 1

    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@company.com'

    @property #attribut
    def fullname(self):
        return f'{self.first} {self.last}'

    def pay_raise(self):
        self.pay = self.pay * self.raise_amount


emp1 = Employee('Roman', 'Kotenjov', 2000)
emp2 = Employee('Mary', 'Gold', 3000)
print(emp1.email)
print(emp1.fullname)
