# Classes

# Creating a class - Like a template
class Dog:

    animal_kind = "canine" # class variable

    def bark(self): # class function = methods
        return "woof"

# print(Dog.animal_kind)
# print(Dog.bark(Dog))

# Instantiation of a class

fido = Dog()
lassie = Dog()

# Class attributes can be overwritten

fido.animal_kind = "Big Dog"
print(type(fido))
print(fido.animal_kind)
print(fido.bark())

