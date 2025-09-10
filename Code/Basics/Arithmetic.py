friends = 0

friends = friends + 1
print(friends)
friends += 1 # Augmented assignment operator
print(friends)

friends = 1
friends = friends - 2
print(friends)
friends -= 2
print(friends)

friends = 1
friends = friends * 3
print(friends)
friends *= 3
print(friends)

friends = 1
friends = friends / 2
print(friends)
friends /= 2
print(friends)

friends = 1
print(friends)
friends = friends ** 2
print(friends)
friends **= 2
print(friends)

friends = 10
remainder = friends % 3
print(remainder)

# Built-in math functions
x = 3.14
y = -4
z = 5

result = round(x) # Round the number to the nearest whole integer
print(result)

result = abs(y) # Returns the distance the numebr is away from zero
print(result)

result = pow(y, 3) # Returns a base raised to a given power (base, exponent)
print(result)

result = max(x, y, z) # Returns the minimum value between x, y, and z
print(result)

result = min(x, y ,z) # Returns the minimum value between x, y, and z
print(result)


# Math functions from MATH module
import math

x = 9.1

print(math.pi) # Gives the value of pi
print(math.e) # Gives the value of the exponential constant

result = math.sqrt(x) # Returns the square root of a given number
print(result)

result = math.ceil(x) # Always rounds up to the nearest whole integer
print(result)

result = math.floor(x) # Always rounds down to the nearest whole integer
print(result)