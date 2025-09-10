# Object: A "bundle" of related attributes (variables) and methods (functions)
#         Ex. phone, cup, book
#         You need a "class" to create many objects

# Class: (blueprint) used to design the structure and layout of an object


# Example 1:
from car import Car # We can import our Car class and create objects that way

car1 = Car("Mustand", 2024, "Red", False)
car2 = Car("Corvet", 2025, "Blue", True)
car3 = Car("Charger", 2026, "Yellow", True)

print(car1) # Prints the memory address of the car object
print(car1.model) # The '.' is called the attribute access operatror, we use it to access any attribute of the object
print(car1.year)
print(car1.colour)
print(car1.for_sale)

print(car2)
print(car2.model)
print(car2.year)
print(car2.colour)
print(car2.for_sale)

print(car3)
print(car3.model)
print(car3.year)
print(car3.colour)
print(car3.for_sale)

car1.drive()
car2.drive()
car3.drive()

car1.stop()
car2.stop()
car3.stop()

car1.describe()
car2.describe()
car3.describe()