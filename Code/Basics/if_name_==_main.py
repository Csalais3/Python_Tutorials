# if __name__ == '__main__': (this script can be imported or run standalone)
#                             Functions and classes within this module can be reused 
#                             without the main block of code executing
#
# Good Practice: (Code is modular, helps readability, leaves no global variables, avoid unintended execution)
#
# Ex. Library: Import library for functionality 
#              When running library directly, display a help page


print(dir()) # prints all of the built-in python attributes

def favourite_food(food):
    print(f"Your favourite food is {food}")

def main():
    print("this is a script")
    favourite_food("Pizza")
    print("Goodbye!")
    
if __name__ == '__main__': # If dunder (double underscore) name is equal to a string of dunder main. This means that the script can be imported or stand alone 
    main()
