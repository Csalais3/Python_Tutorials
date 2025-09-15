

# Example 1:
class Dog: # Creating an object "Dog" and defining the operations that a 'dog' object is able to do
    
    def __init__(self, name): # Allows us to instanciate the method as soon as we call it, takes in any wanted arguements
        self.name = name # Creating an attribute of the class dog. Every 'Dog' has these attributes
    
    def bark(self):
        print("Bark")
    
    def meow(self):
        return "Meow"
    
    def add_one(self, x):
        return x + 1
        
d = Dog()
d.bark()
print(type(d)) # Prints <Class '__main__.Dog'> since its an object that is defined in the 'main' module

# Example 2: