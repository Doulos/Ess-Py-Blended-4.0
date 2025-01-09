def diamond(size=7):
    print(f"A diamond with size {size}:")
    for i in range(1, 2 * size):
        print(("*" * (2 * (size - abs(size - i)) - 1)).center(size * 2))


diamond(3)
diamond(5)
diamond(8)
