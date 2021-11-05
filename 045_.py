import datetime

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
    @classmethod
    def set_pay_raise(cls, ammount):
        cls.raise_ammount = ammount
        
    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split("-")
        return cls(first, last, int(pay))
    @classmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True




emp1 = Employes('Roman', 'Kotenjov', 2000)
emp2 = Employes('Mary', 'Gold', 3000)
print(emp1.pay)
print(emp1.email)
print()
print(emp1.fullname())
print()
print(emp1.pay)
emp1.pay_raise()
print(emp1.pay)
print(emp1.__dict__)
Employes.pay_raise(emp2)
print(emp2.pay)
print(emp2.__dict__)
emp1.raise_ammount = 1.08
print(emp1.__dict__)

print(emp1.number_of_employes)

Employes.set_pay_raise(1.1)
print(emp2.raise_ammount)
print(emp2.__dict__)
emp2.raise_ammount = 1.2
print(emp2.__dict__)

emp3_string = 'Bob-Big-3400'
emp3 = Employes.from_string(emp3_string)
print(emp3.__dict__)
print(emp1.number_of_employes)

today = datetime.date.today()
print(today)
print(today.weekday())



#some_list = [2, 3, 6, 1]
#some_list.sort()
#print(some_list)
#print(some_list[3])