# Collections: a single "Varible" that is used to store multiple values
# List: [] ordered and changeable, duplicate values are allowed 
# Set: {} unordered and immutable (size can't be changed), duplicate values are not allowed, can use add/remove 
# Tuple: () ordered and unchangable, duplicate values are allowed, FASTER
# Dictionaries: A collection of {Key: Value} Pairs
#               Ordered and changable (No duplicates allowed) 

# Lists:
fruits = ["Apple", "Orange", "Bannana", "Coconut"]
x = 1

print(fruits) # Prints the whole list
print(fruits[x]) # Prints a specific value in the list
print(fruits[:3:2]) # Prints every other specified value within the list

for fruit in fruits: #Each counter is the value within the list
    print(fruit)
    
print(dir(fruits)) # Gives all the methods that can be performed on the list 
print(help(fruits)) # Gives a description on all of the methods
print(len(fruits)) # Gives the amount of elements within the list

print("Apple" in fruits) # Returns boolean that checks whether a given element is within a list/other collections

print(fruits[0])
fruits[0] = "Pineapple" # Changes the value at a specified index to another value
print(fruits[0])

fruits.append("Pear") # Adds the specified value to the end of the list
print(fruits)
fruits.remove("Pear") # Removes the specified value from the end of the list
print(fruits)

fruits.insert("Pear, 2") # Adds the specified value to a specified index in the list 
print(fruits)

fruits.sort() # Sorts the list in alphabetical order
print(fruits)

fruits.reverse() # Reverses the current ordering of the list
print(fruits)

# To do reverse alphabetical order

print(fruits.index("Pineapple")) # Returns the index of the specified value

print(fruits.count("Pineapple")) # Returns the amount of times that a specified value appears within the list

fruits.clear() # Removes all of the elements of the list
print(fruits)


# Sets:
fruits = {"Apple", "Orange", "Bannana", "Coconut"} # Has a different order with each initialization
print(fruits)

# Same methods as list, gives same information
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("Pineapple" in fruits)

fruits.add("Pineapple") # Adds specified value to the set
print(fruits)

fruits.remove("Apple") # Removes specified value from the set
print(fruits)

fruits.pop() # Removes the first value in the set
print(fruits)

fruits.clear() # Removes all of the elements from the list
print(fruits)

# Tuples:
fruits = ("Apple", "Orange", "Bannana", "Coconut")
# Same methods as list and set, gives same information
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("Pineapple" in fruits)

print(fruits.index("Apple")) # Returns the index of the specified value within the tuple
print(fruits.count()) # Returns the number of occurrences of a specified value within the tuple

for fruit in fruits:
    print(fruit, end= ", ")
    

# 2-D Lists:
fruits = ["apple", "Orange", "Bannana", "Coconut"]
vegetables = ["Celery", "Carrots", "Potatoes"]
meats = ["Chicken", "Fish", "Turkey"]

groceries = [fruits, vegetables, meats]
print(groceries) 

print(groceries[0][2]) # Prints the individual items of the list [row, column] or [row] for the entire row

for collection in groceries: # Prints every row
    print(collection)
    
for collection in groceries: # Prints every element in the 2-D list
    for food in collection:
        print(food, end=" ")
    print()
    
groceries2 = [["apple", "Orange", "Bannana", "Coconut"], # Regular 2-D list
              ["Celery", "Carrots", "Potatoes"],
              ["Chicken", "Fish", "Turkey"]]

groceries3 = [("apple", "Orange", "Bannana", "Coconut"), # List with tuple elements
              ("Celery", "Carrots", "Potatoes"),
              ("Chicken", "Fish", "Turkey")]

groceries4 = [{"apple", "Orange", "Bannana", "Coconut"}, # List with set elements
              {"Celery", "Carrots", "Potatoes"},
              {"Chicken", "Fish", "Turkey"}]


# Dictionaries:
capitals = {"USA": "Washington D.C.", "India": "New Dheli", "China": "Beijing", "Russia": "Moscow"}

print(dir(capitals))
print(help(capitals))

print(capitals.get("USA")) # Returns the value of the given key, returns NONE if key is not there

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")
    
capitals.update({"Germany": "Berlin"}) # Adds a new entry to the dictionary
print(capitals)

capitals.update({"USA": "Detroit"}) # Updates the current key with a new value
print(capitals)

capitals.pop("China") # Removes the entry of the specified key
print(capitals)

capitals.popitem() # Removes the latest key-value pair that was inserted
print(capitals)

print(capitals.keys()) # Returns all of the keys for that specific dictionary
for key in capitals.keys():
    print(key)
    
print(capitals.values()) # Returns all of the values for that specific dictionary
for value in capitals.values():
    print(value)

print(capitals.items()) # Returns a dicitonary object that resembles a 2D list of tuples
for key, value in capitals.items():
    print(f"{key}: {value}")

capitals.clear()
print(capitals)


