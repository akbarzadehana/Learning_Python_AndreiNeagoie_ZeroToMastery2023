# Scope - what variables do I have access to?
# Any time we create a variable if it's not inside of a function, then it is part of the global scope.

if True:
    x = 10


def some_func():
    total = 100
    print(x)


some_func()
print(x)
# print(total)

a = 1


def confusion():
    a = 5
    return a


# print(a)
# print(confusion())

print(confusion())
print(a)

# 1 - start with local
# 2 - parent local?
# 3 - Global
# 4 - built in python functions.
