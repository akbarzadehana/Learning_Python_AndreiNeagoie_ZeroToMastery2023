print(range(10))  # It is not tuple.

for number in range(10):
    print(number)

for _ in range(0, 10, 2):
    print(_)

for _ in range(10, 0, -1):
    print(_)

for _ in range(4):
    print(list(range(_)))
