# List Comprehension: A concise way to create lists in python
#                     Compact and easier to read than other loops
#                     [expression for value in iterable of condition]


# Example 1:
doubles = []
for x in range(1, 11): # Long version
    doubles.append(x * 2)

print(doubles)

doubles2 = [x * 2 for x in range(1, 11)] # Shorter verion and easier to read
print(doubles2)

# Example 2:
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(triples)
print(squares)

# Example 3:
fruits = ["apple", "orange", "bannana", "coconut"]
print(fruits)

fruits = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruits)
print(fruit_chars)

# Example 4
numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num > 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 != 0]

print(numbers)
print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

# Example 5
grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
failing_grades = [grade for grade in grades if grade < 60]

print(passing_grades)
print(failing_grades)


