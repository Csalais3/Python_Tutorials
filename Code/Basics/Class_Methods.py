# Class Methods: Allows operations related to the class itself
#                Takes (cls) as the first parameter, which represents the class itself

class Student:
    
    count = 0
    total_gpa = 0
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    # INSTANCE METHOD
    def get_info(self): 
        
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        
        return f"Total Number of Students: {cls.count}"

    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0

        return f"{cls.total_gpa / cls.count:.2f}"
    

print(Student.get_count()) # Starts as 0

student1 = Student("Spongebob", 3.2)
student1 = Student("Patrick", 2.0)
student1 = Student("Spongebob", 4.0)

print(Student.get_count()) # Becomes 3 as I 
print(Student.get_avg_gpa())
