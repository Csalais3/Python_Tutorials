# Built-in string methods/functions

name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")

# Length function
result = len(name) # Gives the number of characters a string is (integer)
print(result)

# Find method
result = name.find("B") # Finds and returns the index of the first occurrance of a specified character, if it can't find the character, a -1 is returned
print(result)

# Reverse find method
result = name.rfind("B") # Finds and returns the index of the last occurrance of a specified character, if it can't find the character, a -1 is returned
print(result)

# Capitalized method
result = name.capitalize() # Capitalizes the first letter of the string
print(result)

# Upper method
result = name.upper() # Capitalizes all the letters in the string
print(result)

# Lower method
result = name.lower() # Lowercases all the letters in the string
print(result)

# Is digit method
result = name.isdigit() # Checks if the string contains ONLY digits
print(result)

# Is alpha method
result = name.isalpha() # Checks if the string contains ONLY alphabetical characters, spaces count as non-alphabetical characters
print(result)

# Count method
result = phone_number.count("-") # Counts the amount of a specified character in a given string
print(result)

# Replace method
result = phone_number.replace("-", " ") # Replaces any given character with a different character
print(result)

# Help function:
print(help(str)) # Displays and explains all of the string methods
