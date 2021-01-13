class Dog:
    # the dog class
    def _init_(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("WOLF!")

roger = Dog('Roger', 8)
print(roger.name)
print(roger.age)
roger.bark()

#Inheritance in Python
class Animal:
    def walk(self):
        print('Walking')

class Dog(Animal):
    def bark(self):
        print('WOF!')

# Modules
import dog => dog.bark()
from dog import bark => bark()

# To import from anothe folder called lib
# First create an empty file in that folder called '__init__.py'
from lib import dog => dog.bark()
from lib.dog import bark => bark()






