# Polymorphism: Greek word that means to "Have many forms"
#               Poly = Many
#               Morphe = Form
#
#               Two ways to achieve Polymorphism:
#               1) Inheritance: An obejct could be treated of the same type as a parent class
#               2) "Duck Typing": Object must have necessary attributes/methods

#### INHERITANCE
from abc import ABC, abstractmethod

class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        
        return 3.14 * self.radisu ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        
        return self.base * self.height * 0.5

class Pizza(Circle): # In the case where we have an unrelated class, where there is no inheritence: We can inherit from a child class that can be associated with the class
    def __init__(self, topping, radius):
        self.topping = topping
        self.radius = radius
        
shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("Pepperoni", 15)]   # Our circle is both a circle and a shape, thus having more than one form (two forms for this example)

for shape in shapes:
    print(f"{shape.area()}cm^2")
    
#### DUCK TYPING : Another way to achieve polymorphism besides Inheritance
#                  Object must have the minimum necessary attributes/methods
#                  "If it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")
    
class Cat(Animal):
    def speak(self):
        print("MEOW!")
        
class Car:
    alive = True
    def speak(self): # Renaming the method to the same method of the other classes, as it accomplishes the same thing
        print("HONK!")
        
animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)