# There is new syntax := that assigns values to variables as part of a larger expression.
a = "halloooooooooooo"

if (n := len(a)) > 10:
    print(f"too long {n} elements")

while (n := len(a)) > 1:
    print(n)
    a = a[:-1]

print(a)
