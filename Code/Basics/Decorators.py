# Decorator: A function that extends the behavior of another function
#            without modifying the base function
#            Pass the base function as an argument to the decorator
#
#            @add_sprinkles
#            get_ice_cream("Vanilla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs): #Wrapper is needed to make sure it is called only when we call that function
        print("*You add sprinkles*")
        func(*args, **kwargs)
        
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs): # Added to accept any amount of arguments/keyword arguments
        print("*You add fudge*")
        func(*args, **kwargs)
    
    return wrapper
    
@add_sprinkles # You can apply more than one decorator on a funciton
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream")

get_ice_cream("vanilla")