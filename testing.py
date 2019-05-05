class A:
    def __init__(self, x):
        self._x = None
        self.x = x

    def getx(self):
        print('This is A getting x')
        return self._x

    def setx(self, value):
        print('This is A setting x')
        self._x = value

    def delx(self):
        print('This is A deleting x')
        del self._x

    x = property(getx, setx, delx, "This is the 'x' property")


class B(A):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @A.x.getter
    def x(self):
        print('This is B getting x')
        return super().getx()

    @x.setter
    def x(self, value):
        print('This is B setting x')
        super().setx(value)

    @x.deleter
    def x(self):
        print('This is B deleting x')
        super().delx()

print('Creating A')
a = A('hei')
print('Retrieving from A')
print(a.x)

print('Creating B')
b = B('hallo')
print('Retrieving from B')
print(b.x)
