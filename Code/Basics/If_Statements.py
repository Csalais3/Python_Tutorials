# If: Runs code only IF a specified condition is met 
#     Else: Runs some other code

# Example 1
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else: 
    print("You must be 18+ to sign up")
    
    
# Example 2
response = input("Would you like food? (Y/N): ").capitalize()

if response == "Y":
    print("Have some food!")
else: 
    print("No food for you!")
    
    
# Example 3
name = input("Enter your name: ").capitalize()

if name == "":
    print("YOU DIDN'T TYPE YOUR NAME!")
else:
    print(f"Hello {name}")
    

# Example 4
for_sale = False

if for_sale:
    print("This item is for sale")
else:
    print("This item is Not for sale")

    
# Example 5
online = True

if online:
    print("The user is online")
else:
    print("The user is offline")