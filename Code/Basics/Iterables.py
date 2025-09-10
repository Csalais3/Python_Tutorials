# Iterables: An Object/Collection that can return its elements one at a a time
#            allowing it to be iterated over in a loop

# Lists
numbers = [1, 2, 3, 4, 5] # the variable 'numbers' is iterable because the variable can be iterated upon (since it can contain more than one element)

for number in numbers: 
    print(number, end= " ")
    
for number in reversed(numbers):
    print(number, end= " ")
    
#Tuples
numbers = (1, 2, 3, 4, 5) # the variable 'numbers' is iterable for the same reason as the list variable

for number in numbers: 
    print(number, end= " ")
    
for number in reversed(numbers):
    print(number, end= " ")
    

# Sets
fruits = {"apple", "orange", "bannana", "coconut"}  # the variable 'numbers' is iterable for the same reason as the list and tuple variables

for fruit in fruits:
    print(fruit)
    

# Strings
name = "Christian" # The name is a variable since the characters of the string can be iterated upon

for char in name:
    print(char)

for char in name:
    print(char, end= "")
    

# Dictionaries
my_dictionary = {"A": 1, "B": 2, "C": 3} # When you iterate over a dictionary, you iterate over the keys rather than the values 

for key in my_dictionary:
    print(key)

for value in my_dictionary.values(): # Use the values() method to iterate over the values
    print(value)
    
for key, value in my_dictionary.items(): # You can use the items() method to iterate over both keys and values
    print(f"{key}: {value}")