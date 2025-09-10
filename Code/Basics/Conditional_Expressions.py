# Conditional Expressions: A one-line shortcut for the if-else statement (ternerary operator)
#                          Print or assign one or two values based on a condition
#                          X if condition else Y

num = 5
a = 6
b = 7
age = 18
temperature = 30
user_role = "admin"


result1 = "Positive" if num > 0 else "Negative"
result2 = "Even" if num % 2 == 0 else "Odd"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "HOT" if temperature > 20 else "Cold"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(result1)
print(result2)
print(max_num)
print(min_num)
print(status)
print(weather)
print(access_level)

