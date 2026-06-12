

class myproperty:
    def __init__(self, fget):
        self.fget = fget
        self.fset = None

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def setter(self, func):
        self.fset = func
        return self


class User:
    def __init__(self):
        self._age = 0

    @myproperty
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must be positive")
        self._age = value

u = User()

u.age = 30
print(u.age)

u.age = -5   # raises ValueError

