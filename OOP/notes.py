# class Dog():
#
#     # Class Object Attribute
#     species = "mammal"
#
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name
#
# mydog = Dog(breed = "Lab", name = "John")
# otherdog = Dog(breed = "Huskie", name = "Jane")
# print(mydog.breed, mydog.name, mydog.species)
# print(otherdog.breed, otherdog.name, mydog.species)

class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return(self.radius ** 2 * Circle.pi)

    def set_radius(self, new_r):
        self.radius = new_r

myc = Circle(3)
print(myc.radius)
myc.set_radius(999)
print(myc.area())
