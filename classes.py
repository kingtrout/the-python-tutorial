class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
# print(x.r, x.i)

z = MyClass()
print(z.f())


class Dog:

    kind = 'canine'             # class variables unique to each class

    def __init__(self, name):
        self.name = name        # instance variables unique to each instance


h = Dog('Jagger')
p = Dog('Leo')


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


class Employee:
    pass

john = Employee()

john.name = 'John Doe'
john.department = 'Science'
john.salary = '1000'
