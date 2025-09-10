# Exercise 9: Validating user inputs
#   1. Username must not be more than 12 Characters
#   2. Username must not contain spaces
#   3. Username must not contain digits

username = input("Please enter your username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters ")
elif username.find(" ") != -1: 
    print("Your username can't contain spaces")
elif not username.isalpha(): 
    print("Your username can't contain digits")
else:
    print(f"Welcome {username}!")

# String indexing: accessing elements of a sequence using [] (indexing operation)
#                  [start: end: step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) # First index starts at 0
print(credit_number[0:4]) # Prints the first 4 characters of the string
print(credit_number[5:9]) # Prints the next 4 characters of the string
print(credit_number[-1]) # Prints the last character of the string (negative indexes go backwards in the string)
print(credit_number[::2]) # Prints every 2nd character in the string

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

reversed = credit_number[::-1] #reverses the string
print(reversed)


 