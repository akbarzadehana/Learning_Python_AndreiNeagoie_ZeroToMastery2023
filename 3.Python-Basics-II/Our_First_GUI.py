picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for row in picture:
    for pixel in row:
        if pixel == 0:
            print(" ", end="")
        elif pixel == 1:
            print("*", end="")
    print("")  # need a new line after every row


print("----------")

# clean
# Readability
# predictability
# DRY
fill = "*"
empty = " "
for row in picture:
    for pixel in row:
        if pixel:
            print(fill, end="")
        else:
            print(empty, end="")
    print("")
