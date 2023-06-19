# OOP - Object oriented Programming

Turning code into objects which can then be manipulated. The name of a class should be capitalized and camel case.

A class variable is a variable in the scope of the class. Not a global variable. Class functions are called methods.

When you create a class it is like a blueprint or template. 

Class creation example:
```python
class Dog:

    animal_kind = "canine" # class variable

    def bark(self): # class function = methods
        print(self.animal_kind)
        return "woof"
```

`self` refers to the current class so in this case it is Dog.

!["Dog classes image"](C:\Users\elena\PycharmProjects\tech241\python_oop\classes_dog_img.png)

### Instantiation 

This means to create an instance of the class. So for the example you will make a dog using the template.

```python
fido = Dog()
lassie = Dog()
```

The type of fido is `<class '__main__.Dog'>`. A class. So fido and lassie have access to the same methods and variables that Dog() has. They are separate entities.

!["Dog phase 1 image"](C:\Users\elena\PycharmProjects\tech241\python_oop\stage1_dog_class.png)

Class variables **can** be overwritten.
Be careful of class variables. 

!["Dog phase 2 img"](C:\Users\elena\PycharmProjects\tech241\python_oop\stage2_dog_class.png)