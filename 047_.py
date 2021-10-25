class Employes:
    raise_ammount = 1.05
    number_of_employes = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first.lower() + '.' + self.last.lower() + '@company.com'
        Employes.number_of_employes += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def pay_raise(self):
        self.pay = self.pay * self.raise_ammount

    def __str__(self):
        return f'{self.fullname()}, salary: {self.pay}, email: {self.email}'

    def __repr__(self):
        return f'{self.__dict__}'

    def __add__(self, other):
        return f'Sum of salary is: {self.pay + other.pay}'
    
    def __len__(self):
        return len(self.fullname()) - 1 #dlinna last i first

emp1 = Employes('Roman', 'Kotenjov', 2000)
emp2 = Employes('Mary', 'Gold', 3000)
print(emp1)
print(emp2.__repr__())
print()
print(emp1 + emp2)
print(emp1.__add__(emp2))
print()
print(len(emp1))
print(emp1.__len__())
