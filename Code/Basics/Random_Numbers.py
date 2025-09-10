import random

print(help(random))

low = 1
high = 100

number = random.randint(low, high) # Gives a random integer within the give range (lower, upper) * Is inclusive
print(number)
number = random.random() # Gives a random float within the given range
print(number)

options = ("Rock", "Paper", "Scissors")
move = random.choice(options)
print(move)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]
random.shuffle(cards) # Shuffles the list that is given
print(cards)


