# Multiple Inheritence: Inheritence from more than one Parent Class C(A, B)

# Multi-level Inheritence: Inherit from a parent that inherits from another parent C(B) <- B(A) <- A

class Animal:
    def __init_(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee() # Inherits the flee method from the prey class
hawk.hunt() # Inherits the hunt method from the predator class
fish.flee() # Inherits both the flee method from the prey class and the hunt method from the predator class
fish.hunt()

# We can then use the inherited methods of the inherited class' inherited class
rabbit.eat()
rabbit.sleep()
hawk.eat()
hawk.sleep()
fish.eat()
fish.sleep()