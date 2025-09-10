# Exercise 5: Calculating the length of the hypotenuse of a right triangle
# Formula : C² = A² + B²
import math

a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The length of the hypotenuse of this triangle is {c}cm")

