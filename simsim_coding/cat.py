class Person():
    def __init__(self, name):
        self.name = name
    def get_name_upper(self):
        return self.name.upper()
print(Person.get_name_upper(Person('Park')))
p = Person('Park')
print(p.get_name_upper())
print(Person.get_name_upper(p))
