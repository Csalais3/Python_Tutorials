# Variable = A container for a value (string, integer, float, boolean) <- introductory datatypes
#            A variable behaves as if it was the value that it contains

# Strings
# A string is a series of characters, and maybe numbers, but we will consider them as characters
first_name = "Christian"
food = "Pizza"
email = "Chrissal0604@gmail.com"

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

# Integers
# An integer is a whole number
age = 21
quantity = 3
num_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_students} students")

# Floats
# A float is a floating point integer, which is a number that containes a decimal portion
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is {price}")
print(f"Your GPA is {gpa}")
print(f"You ran {distance}km")

# Boolean
# A boolean is a true or false value, can also be represented as either a 1 (true) or 0 (false)
is_student = True
for_sale = True
is_online = True

print(f"Are you a student?: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")


if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")
    
if is_online:
    print("You are online")
else:
    print("You are offline")