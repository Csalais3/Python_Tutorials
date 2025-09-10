# Format Specifiers: {:flags} format a value based on what flags are inserted

price1 = 3.14159
price2 = -987.65
price3 = 12.34

# .(number)f = Round to that many decimal places (fixed point)
print(f"Price 1 is ${price1:.2f}")
print(f"Price 1 is ${price1:.2f}")
print(f"Price 1 is ${price1:.2f}")

# :(number) = To allocate that many spaces
print(f"Price 1 is ${price1:10}")
print(f"Price 1 is ${price1:10}")
print(f"Price 1 is ${price1:10}")

# :03 = To allocate and zero pad that many spaces
print(f"Price 1 is ${price1:010}")
print(f"Price 1 is ${price1:010}")
print(f"Price 1 is ${price1:010}")

# :< = Left Justify
print(f"Price 1 is ${price1:<10}")
print(f"Price 1 is ${price1:<10}")
print(f"Price 1 is ${price1:<10}")

# :> = Right Justify
print(f"Price 1 is ${price1:>10}")
print(f"Price 1 is ${price1:>10}")
print(f"Price 1 is ${price1:>10}")

# :^ = Center Allign
print(f"Price 1 is ${price1:^10}")
print(f"Price 1 is ${price1:^10}")
print(f"Price 1 is ${price1:^10}")

# :+ = Use a positive sign to indicate many positive values
print(f"Price 1 is ${price1:+}")
print(f"Price 1 is ${price1:+}")
print(f"Price 1 is ${price1:+}")

# := = Place a sign to leftmost position
print(f"Price 1 is ${price1:=}")
print(f"Price 1 is ${price1:=}")
print(f"Price 1 is ${price1:=}")

# : = insert a space before positive numbers
print(f"Price 1 is ${price1: }")
print(f"Price 1 is ${price1: }")
print(f"Price 1 is ${price1: }")

# :, = comma seperator
print(f"Price 1 is ${price1:,}")
print(f"Price 1 is ${price1:,}")
print(f"Price 1 is ${price1:,}")


# You can even mix them up
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 1 is ${price1:+,.2f}")
