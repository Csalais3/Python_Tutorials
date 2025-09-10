# Exercise 4: Calculating the cirumfrence and area of a circle
# Formula : Circumfrence = 2 * Pi * Radius
# Formula : Area = Pi * Radius²
import math

radius = float(input("Input the radius of the circle"))

circumfrence = 2 * math.pi * radius
print(f"The circumfrence is: {round(circumfrence, 2)}cm") # The round function can be used to round to the nearest specified decicmal point

area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)}cm²")