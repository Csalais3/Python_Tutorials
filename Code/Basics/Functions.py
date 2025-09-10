# Function: A block of reusable code
#           Place () after the name to invoke the function

# Example

def happy_birthday(name, age): # (parameter 1, parameter 2) Order of passed arguments matter
    print(f"Happy Birthday To {name}!")
    print(f"You Are {age} Old!")
    print("Happy Birthday To You!")
    print()
    
happy_birthday("Christian", 21) # We can pass any amount of arguments to the function, as long as the appropriate parameters are set up 

def display_invoice(user_name, amount, due_date):
    print(f"Hello {user_name}")
    print(f"Your bill of ${amount:.2f} is due on {due_date}")
    
display_invoice("csalais3", 42.50, "01/01")

# Return: Statement used to end a function and send a result back to the caller

def add(x, y):
    z = x = y
    return z

def sub(x, y):
    z = x - y
    return z

def mult(x, y):
    z = x * y
    return z

def div(x, y):
    z = x/y
    return z

print(add(1, 2))
print(sub(1, 2))
print(mult(1, 2))
print(div(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("christian", "salais")
print(full_name)


# Default Arguments: A default value for certain parameters
#                    Default is used when that argument is omitted
#                    Makes your functions more flexible, reduces # of arguments
#                    1. Positional, 2. DEFAULT, 3. Keyword, 4. Arbituary


# Example 1
def net_price(list_price, discount= 0, tax= 0.05): # Parameters have default values, however, can be overwritten by a new value being passed in
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))


# Example 2
import time

def count(end, start = 0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("Done!")

count(10)

# Keyword Arguments: An arguemnt that is preceded by an identifier
#                    Helps with readability
#                    Order of arguments does not matter
#                    1. Positional, 2. Default, 3. KEYWORD, 4. Arbituary


# Example 1:
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title= "Mr.", last= "Salais", first= "Christian") # Positional arguments must be before keyword arguments 


# Example 2:
for x in range(1, 11):
    print(x, end= " ") # end= "" is a keyword argument
    

# Example 3:
print("1", "2", "3", "4", "5", sep= "-") # sep= "-" is a keyword argument


# Example 4: 

def getphone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

my_phone = getphone(country= 1, area= 123, first= 456, last= 7890)
print(f"My Phone number is {my_phone}")


# *args :            allows you to pass multiple non-key arguments
# **kwargs :         allows you to pass multiple keyword arguments
#                    * : unpacking operator
#                    1. Positional, 2. Default, 3. Keyword, 4. ARBITUARY

# Example 1
def add(*nums): # Tuple of arguments *args is naming convention, but the parameter name can vary
    print(type(nums))
    
    total = 0
    for num in nums:
        total += num
    
    return total

print(add(1, 2, 3))

# Example 2
def display_name(*args):
    for arg in args:
        print(arg, end= " ")
    
display_name("Christian", "Salais")

# *Kwargs

def print_address(**kwargs):
    print(type(kwargs))
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
print_address(street="123 Fake St.",
              apt="100",
              city="Detroit", 
              state="MI", 
              zip="54321")

# Example 2
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end= " ")
    print()
    
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
         print(f"{kwargs.get('street')}")
         print(kwargs.get('pobox'))
    else:
         print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Doctor", "Spongebob", "Squarepants", "III", 
               street="123 Fake St.",
              apt="#100",
              city="Detroit", 
              state="MI", 
              zip="54321")