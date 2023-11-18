# *args : this can accept any number of positional arguments like this.
def super_func(*args, **kwargs):
    print(kwargs)
    print(args)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))
# Rule: params, *args, default parameters, **kwargs
