spaces = "         "
stars = "*******************"
for i in range(10):
    print(spaces[0 : 9 - i] + stars[0 : i * 2 + 1])
for i in range(9, 0, -1):
    print(spaces[0 : 10 - i] + stars[0 : i * 2 - 1])
