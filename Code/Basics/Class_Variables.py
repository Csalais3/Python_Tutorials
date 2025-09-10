# Class Variables: Variables that are shared among all instances of a class
#                  Defined outside of the constructor
#                  Allows you to share data among all objects created in the class

class Student:
    class_year = 2024
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1 # You must access the variable by calling the class with the attribute access operator
        
student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(student1.name, student1.age)
print(student2.name, student2.age)
print(student3.name, student3.age)
print(student4.name, student4.age)
print(student1.class_year, student2.class_year, student3.class_year, student4.class_year) # Same value, since all objects of the class share the same value'
print(Student.class_year) # Clarifies that the variable is a class variable by accesing it through the class name
print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} Students")
print(student1.name, student2.name, student3.name, student4.name)


