
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

class  Developer(Employes):

        def __init__(self, first, last, pay, prog_lang):

            #Employes.__init__(self, first, last, pay)
            super().__init__(first, last, pay)
            self.prog_lang = prog_lang

class Manager(Employes):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = []

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            print('employee already in list')

    def print_all_employees(self):
        for emp in self.employees:
            print(emp.fullname())

    def count_employes(self):
        print(len(self.employees())

emp1 = Employes('Roman', 'Kotenjov', 2000)
emp2 = Employes('Mary', 'Gold', 3000)
dev1 = Developer('Job', 'Mee', 5000, 'pHp')
print(dev1.__dict__)
print(dev1.raise_ammount)
man1 = Manager('Tom', 'Swee', 4000)
man1.add_employee(dev1)
man1.add_employee(emp1)
man1.add_employee(emp2)
print(man1.employees)
man1.print_all_employees()