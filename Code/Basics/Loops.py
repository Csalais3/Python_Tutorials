# While Loops: Executes code WHILE some condition remains true

# Example 1
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Hello {name}")

# Example 2
age = int(input("Enter your age: "))

while age < 0:
    print("Your age can't be negative")
    age = int(input("Enter your age: "))
    
print(f"You are {age} years old")

# Example 3
food = input("Input a food that you like (q to quit): ")

while food != "q":
    print(f"You like {food}")
    food = input("Input another food that you like (q to quit): ")

print("Bye!")

# Example 4
num = int(input("Enter a number between 1-10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1-10: "))
    
print(f"Your number is {num}")


# For loops: execute a block of code a fixed number of times.
#            You can iterate over a range, string, sequence, etc.

# Example 1
for counter in range(1, 11, -1): # Range parameters range(start, stop + 1, steps), starts at index 0 at default
    print(counter) 

print("HAPPY NEW YEAR!")

# Example 2
for x in range(1, 21):
    if x == 13: # Skips the 13th iteration
        continue
    else:
        print(x)


# Nested Loops: A loop that is inside another loop (outer, inner)
#               outer loop:
#                   inner loop:

# Example 1
for x in range(3):
    for y in range(1, 10): # make sure the counters are different between the loops
        print(y, end=", ") # Prints 1-9 seperated by a comma
    print() # Prints a new line
    

# Example 2
rows = int(input("Enter the amount of rows: "))
columns = int(input("Enter the amount of columns: "))
symbol = input("Input a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()