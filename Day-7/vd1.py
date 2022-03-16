class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def say_hello(self):
        print(f'Xin chào, tên tôi là {self.name}')

    def update_address(self, new_address):
        self.address = new_address

person = Person('Nguyễn Văn An', 'Hà Nội')
person.say_hello()
person.update_address('TP. HCM')
print(f'{person.name} sống tại {person.address}')