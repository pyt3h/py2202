class Person:
    def __init__(self, name, address):
        self._name = name
        self._address = address

    @property
    def name(self):
        # ...
        return self._name

    @name.setter
    def name(self, val):
        # ... validate
        self._name = val

p = Person('Nguyen Van A', 'Ha Noi')
print(p.name)
p.name = 'Nguyen Van B'
print(p.name)