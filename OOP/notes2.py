# Inheritance
class Animal():

    def __init__(self):
        print("Class Animal Created!")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof")

myAnimal = Animal()
myAnimal.whoAmI()
myAnimal.eat()

myDog = Dog()
myDog.whoAmI()
myDog.eat()
myDog.bark()
