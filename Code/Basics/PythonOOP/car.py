# For better organization, we can make the class its own file (Not Necessary)

class Car:
    def __init__(self, model, year, colour, for_sale): # Initializing the object with a constructor method. *Self means the object that we are creating
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale
    
    def drive(self):
        print(f"You drive the {self.colour} {self.model}")
    
    def stop(self):
        print(f"You stop the {self.colour} {self.model}")
        
    def describe(self):
        print(f"{self.year} {self.colour} {self.model}")
        