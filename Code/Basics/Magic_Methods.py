# Magic Methods: Dunder methods (double underscore) __init__, __str__, __eq__
#                They are automatically called by many of Pythong's built-int operations
#                They allow developers to define or customize the behavior of objects
# Allows for the defining/customization of objects

class Student:
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    
    def __str__(self):
        return f"name: {self.name} gpa: {self.gpa}"
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __gt__(self, other):
        return self.gpa > other.gpa

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
    
print(student1)
print(student1 == student2)
print(student1 > student2)
    
    
# Example 2
class Book:
    
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
        
    def __eq__(self, other): # Implementing the specific logic behind the equals operation and what counts as 'equal' 
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other): # Implementing the specific logic behind the < operator (what counts as 'less than')
        return self.num_pages < other.num_pages
    
    def __gt__(self, other): # Same as lt, but for greater than
        return self.num_pages > other.num_pages
    
    def __add__(self, other): # Used for adding logic
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword): # useful for 'in' logic
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "Author":
            return self.author
        elif key == "pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"
        
        

book1 = Book("The Hobbit", "J.R.R Tolkien", 310) # When calling the class of book and pass in the arguments, the init dunder method is automatically called, assigning the attributes
book2 = Book("Harry Potter and the Philosipher's Stone", "J.K Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S Lewis", 172)

print(book1) # Prints the memory address of book1 by itself, however, if we use the str dunder method, we can customize the returned information (returning a string representation of the object, when printing directly to the console)
print(book1 == book2) 
print(book1 < book3)
print(book1 + book2)
print("Lion" in book3)
print(book1['title'])
print(book1['author'])
print(book1['pages'])

    