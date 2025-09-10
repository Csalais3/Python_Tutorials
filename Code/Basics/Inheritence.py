# Inheritence: Allows a class to inherit attributes and methods from another class
#              Helps with code reusability and extensibility
#              class Child(Parent):

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is asleep")
        
    def speak(self):
        print("SPEAK")

class Dog(Animal):
    def speak(): # You can have different implementations of the 
        print("WOOF!") 
    def tailWag(): # Fuctions an also be defined within child classes for unique traits such as "tailWag"/
        print("The dog wags its tail!")

class Cat(Animal):
    def speak():
        print("MEOW!")

class Mouse(Animal):
    def speak():
        print("SQUEEK!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name) # Even though there is nothing in the class, we can see that the class inherits the attributes of the "Animal" class to allow for the creation of an animal object, with the name attributes and the is_alive status
print(dog.is_alive)
dog.eat()
dog.sleep()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
