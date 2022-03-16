class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_fullname(self):
        return self.last_name + ' ' + self.first_name

    @property
    def fullname(self):
        return self.last_name + ' ' + self.first_name

    def __str__(self):
        return self.last_name + ' ' + self.first_name
    
p = Person('An', 'Nguyen')
print(p.get_fullname())
print(p.fullname)
print(p)