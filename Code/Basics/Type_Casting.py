# Typecasting = The process of converting one variable from one datatype to another
#               str(), int(), float(), bool() <- examples

name = "Christian Salais"
age = 21
gpa = 3.2
is_student = True

type(name) # <- gets type of the variable
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa_i = int(gpa)
print(gpa_i)

age_f = float(age)
print(age_f)

age_s = str(age)
print(age_s)
print(type(age_s))

# age_s += 1 would cause an error
age += 1
age_s += "1"

print(age_s)

name_b = bool(name) # will always be true, will only be flase if the string was empty
print(name_b) 


