# Membership Operators: Used to test whether a value or variable is found in a sequence 
#                       (string, list, tuple, set, or dictionary)
#                       1: in
#                       2: not in 

# In: Checks whether a value/variable is within some collection or string
# Not in: Check whether a value/variable is within some collection or string and negates the result (basically checks if something is not in a colleciton or string)

# Example 1:
word = "Apple"

letter = input("Guess a letter in the secret word: ")

if letter in word: # Returns a boolean value of whether the letter is in the word or not
    print(f"There is a {letter}")
else: 
    print(f"{letter} was not found")
    
    
# Example 2:
students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ").capitalize()

if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")
    
    
# Example 3:
grades = {"Sandy": "A",
          "Squidward": "B", 
          "Spongebob": "C", 
          "Patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")
    

# Example 4:
email = "chrissal0604@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")
    

    