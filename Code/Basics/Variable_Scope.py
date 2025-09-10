# Variable Scope: Where a variable is visible and accessible
# Scope Resolution: (LEGB) Local -> Enclosed -> Global -> Built-in

# Local Scope: Variables that are defined within a function 
def func1(): 
    a = 1 # Variable 'a' is local to function 1
    print(a)
    
def func2():
    b = 2 # Varibale 'b' is local to function 2
    print(b)
    
func1()
func2()


# Functions can be nested and have multiple versions of the variable
def func1(): 
    x = 1 
    def func2():
        x = 2 
        print(x) # We would print 2 (the local version)
    func2()
    
func1()


# Enclosed Varables:
def func1(): 
    x = 1 
    def func2():
        print(x) # We would print 1 (the enclosed version)
    func2()

func1()


# Global Varibales: 
x = 3

def func1(): 
    x = 2
    print(x) #Prints the local variable x = 2
    
def func2():
    print(x) #Prints the global variable x = 3
    
func1()
func2()


# Built in
from math import e # the math version is a built-in variable

def func1():
    print(e)
    
e = 3 # This verison of e is global, which means that it is used in the funciton 

func1()

# The value of the variable that is used depends on the lowest scope that the variable has access to at that time.