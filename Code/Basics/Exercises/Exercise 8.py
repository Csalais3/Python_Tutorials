# Exercise 8: Temperature Converstion Program

temperature = input("What is the current temperature?")
unit = input("What is the unit? (F/C): ")

if unit == "C":
    temperature = round((9 * temperature) / 5  + 32, 1)
    print(f"The temperature in Farenheit is {temperature}")
elif unit == "C":
    temperature = round((temperature - 32) * 5 / 9  + 32, 1)
    print(f"The temperature in Celcius is {temperature}")
else:
    print(f"{unit} is an invalid unit")
