# Exercise 15: Concesssion Stand Program

menu = {"Pizza": 3.00,
        "Nachos": 4.50,
        "Popcorn": 6.00,
        "Fries": 2.50,
        "Chips": 1.00,
        "Pretzel": 3.50,
        "Soda": 3.00,
        "Lemonade": 4.25}

cart = []
total = 0

print("------- MENU -------")
for food, price in menu.items():
    print(f"{food:10}: ${price:.2f}")

print()

while True:
    food = input("Select a food item (q to quit): ").capitalize()
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += float(menu.get(food))
        print(f"Your current balance is {total:.2f}")
    else:
        print("Invalid food item")
        print(f"Your current balance is {total:.2f}")
    print()
        
print("----- Your Cart -----")

for item in cart:
    print(f"{item:10}: ${menu.get(item):.2f}")

print()
print(f"Total: ${total:.2f}")