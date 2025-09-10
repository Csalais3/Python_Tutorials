# Python File Detection
import os

file_path = "test.txt" # Relative file_path (if file is within the same folder) or Absolute File Path (If the file is somewhere else in the system)

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist")


# Writing Files

text_data = "I like pizza."
file_path = "output.txt"

with open(file_path, "w") as file:
    file.write(text_data)
    print(f"txt file {file_path} was created")
    
    
# Reading Files