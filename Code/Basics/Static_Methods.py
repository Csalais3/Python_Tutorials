# Static Methods: A method that belongs to a class rather than any object form that class (instance)
#                 Usually used for general utility functions
#
#                 Instance Methods: Best for operations on instances of the class (objects)
#                 Static Methods: Best for utility functions that do not need access to class data

class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        
        return position in valid_positions

Employee.is_valid_position("Cook") # for static methods, you just need the class and call what you need to call from that class, hence why its used as a general utility method
Employee.is_valid_position("Rocket Scientist")

employee1 = Employee("Eugine", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(employee1.get_info()) # For an instance method, you need the access to the specific object then call the instance method
print(employee2.get_info())
print(employee3.get_info())