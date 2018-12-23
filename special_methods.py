class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        return NotImplemented

    def __len__(self):
        return self.fullname().__len__()


emp_1 = Employee(first='Corey', last='Schafer', pay=50000)
emp_2 = Employee(first='Test', last='Employee', pay=60000)

# print(1 + 2)
# print('1' + '2')

# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))
# print(emp_1.__repr__())
# print(emp_1.__str__())
# print(int.__add__(1, 2))
# print(str.__add__('1', '2'))

# print(int.__add__(emp_1.pay, emp_2.pay))
# print(emp_1 + emp_2)

print(len(emp_1))