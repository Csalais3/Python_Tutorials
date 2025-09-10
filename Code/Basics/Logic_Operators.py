# Logic Operators = Evaluate multiple conditions (Or, And, Not)
#                   Or = At least one of the conditions must be true
#                   And = Both conditions must be true
#                   Not = Inverts the conditions (not False = True, not True = False)

temp = 25
is_raining = False
is_sunny = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
    
    
if temp >= 28 and is_sunny:
    print("It's HOT outside!")
    print("It's Sunny!")
elif temp >= 28 and not is_sunny:
    print("It's HOT outside!")
    print("It's Cloudy!")
elif temp <= 0 and is_sunny: 
    print("It's COLD outside!")
    print("It's Sunny!")
elif temp <= 0 and not is_sunny: 
    print("It's COLD outside!")
    print("It's Cloudy!")
elif 0 < temp < 28 and is_sunny:
    print("It's WARM outside!")
    print("It's Sunny!")
elif 0 < temp < 28 and is_sunny:
    print("It's WARM outside!")
    print("It's Cloudy!")
  