# Pure functions has 2 rules : one is that given the same input, it will always return the same output. And the second point is this idea of a function should not produce any side effects.
# Side effects are things that a function does that affects the outside world.
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3]))
