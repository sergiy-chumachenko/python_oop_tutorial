
class Point(object):
    def __init__(self, x):
        self.__x = x

    def __repr__(self):
        return f'Point({self.__x})'

    def __str__(self):
        return f'Point: {self.__x}'

    @property
    def x(self):
        print('Getter is called!')
        return self.__x

    @x.setter
    def x(self, x):
        print('Setter is called!')
        self.__x = x

    @x.deleter
    def x(self):
        print('Deleter is called!')
        self.__x = None


p1 = Point(10)
print(p1.__str__())
print(p1.__repr__())
print(p1.x)

p1.x = 100
print(p1.x)

del p1.x

print(p1.x)
