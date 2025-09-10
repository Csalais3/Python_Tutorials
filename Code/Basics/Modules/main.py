# Module: A file containing code you want to include in your program
#         Use 'import' to include a module (build-in or your own)
#         Useful to break up a large program reusable seperate files

print(help("modules")) # Prints all of the modules available within the python standard library (you can put the name of any module within the help function to print the information of that module)

import math as m #creates an alias for the module instead of having to type it directly 
from math import pi # imports a specific part of the module

import example # imports the module made 

result = example.pi
print(result)

result = example.square(3)
print(result)

result = example.cube(3)
print(result)

result = example.circumfrence(3)
print(result)

result = example.area(3)
print(result)