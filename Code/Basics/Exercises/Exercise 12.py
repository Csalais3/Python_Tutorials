# Exercise 12: Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- Your Cart -----")

for i in range(len(foods)):
    print(f"{foods[i]} ${prices[i]}")
    total += prices[i]

print()
print(f"Total: ${total}")
