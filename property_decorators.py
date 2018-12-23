
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None
        self.last = None


emp_1 = Employee('Corey', 'Schafer', 50000)

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

print('*'*25)
# emp_1.first = 'Jim'
emp_1.fullname = 'Jim Smith'


print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

print('*'*25)
del emp_1.fullname
print(emp_1.__dict__)
