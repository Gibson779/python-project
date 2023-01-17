#Object-Oriented Programming in Python

class Dog:
    def __init__ (self, name, age):   # METHODS
        self.name = name
        self.age = age
    def get_age(self):
         return self.age
    def get_name(self):
        return self.name
    def set_age(self,age):
        self.age = age


d = Dog("Tim", 14)
print(d.get_age())
d2 = Dog("Bill", 7 )
print(d2.get_age ())
